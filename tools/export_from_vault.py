#!/usr/bin/env python3
"""Refresh the public copy from the private Obsidian vault with the same filter every time.

    python3 tools/export_from_vault.py --vault ~/Documents/Nexus-wiki [--dry-run]

Default-deny: only files matching an include glob in export-config.json are copied,
minus anything matching an exclude glob. Every copied file is then redacted (emails,
phone numbers, local paths, @handles of private people via the optional blocklist) and
scanned; a file that trips a hard rule (a secret/token) is dropped, not copied.

The private blocklist (names that must never appear: family, employers, guests) lives
OUTSIDE this repo at ~/.config/living-brain-export/blocklist.txt, one term per line,
case-insensitive. It is never committed. A file containing a blocklist term is dropped.

Writes: content/<vault-relative path>, EXPORT-MANIFEST.md (included + excluded counts,
scan result). Wikilinks to pages that are not exported are flattened to plain text.
"""
import argparse, fnmatch, json, os, re, subprocess, sys, time, pathlib, hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "tools" / "export-config.json").read_text())
BLOCKLIST_FILE = pathlib.Path(os.path.expanduser("~/.config/living-brain-export/blocklist.txt"))

HARD = [  # a match drops the whole file
    ("api-key", re.compile(r"\b(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[A-Za-z0-9-]{10,})")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}")),
    ("secret-assign", re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+=]{12,}")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
]
SOFT = [  # redacted in place
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[email removed]"),
    ("phone", re.compile(r"(?<![\d.])(\+?1[\s.-])?\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b(?![\d.])"), "[phone removed]"),
    ("local-path", re.compile(r"/(Users|Volumes)/[^\s)\]\"'`]+"), "[local path removed]"),
    ("icloud-path", re.compile(r"~/(Library|Documents|Downloads|Developer|\.config|\.local|\.claude)[^\s)\]\"'`]*"), "[local path removed]"),
]

def glob_match(path, pat):
    rx = re.escape(pat).replace(r"\*\*/", "(?:.*/)?").replace(r"\*\*", ".*").replace(r"\*", "[^/]*").replace(r"\?", "[^/]")
    return re.fullmatch(rx, path, flags=re.I) is not None

def allowed(rel):
    if any(glob_match(rel, p) for p in CFG["exclude_exceptions"]):
        pass
    elif any(glob_match(rel, p) for p in CFG["exclude"]):
        return False
    return any(glob_match(rel, p) for p in CFG["include"])

def materialize(p, tries=25):
    """iCloud may have evicted the file; ask for it and wait until readable."""
    for i in range(tries):
        try:
            with open(p, "rb") as f:
                return f.read()
        except OSError:
            if i == 0 or i % 8 == 0:
                subprocess.run(["brctl", "download", str(p)], capture_output=True)
            time.sleep(1)
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=os.environ.get("NEXUS_VAULT", os.path.expanduser("~/Documents/Nexus-wiki")))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    vault = pathlib.Path(a.vault).expanduser()
    blocklist = []
    if BLOCKLIST_FILE.exists():
        blocklist = [l.strip().lower() for l in BLOCKLIST_FILE.read_text().splitlines() if l.strip() and not l.startswith("#")]
    else:
        print("WARNING: no blocklist at", BLOCKLIST_FILE, "- name check skipped", file=sys.stderr)

    cands = []
    for dp, dn, fn in os.walk(vault):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), vault)
            if allowed(rel):
                cands.append(rel)
    cands.sort()
    keep = {pathlib.PurePosixPath(c).stem.lower(): c for c in cands}

    out = ROOT / "content"
    report = {"copied": [], "dropped": [], "redactions": {}}
    if not a.dry_run and out.exists():
        import shutil; shutil.rmtree(out)
    for rel in cands:
        src = vault / rel
        data = materialize(src)
        if data is None:
            report["dropped"].append((rel, "could not read (iCloud placeholder)")); continue
        if len(data) > CFG["max_file_bytes"]:
            report["dropped"].append((rel, f"too large ({len(data)//1024} KB)")); continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            report["dropped"].append((rel, "not text")); continue
        hit = next((n for n, rx in HARD if rx.search(text)), None)
        if hit:
            report["dropped"].append((rel, f"hard rule: {hit}")); continue
        low = text.lower()
        bl = next((t for t in blocklist if re.search(r"\b" + re.escape(t) + r"\b", low)), None)
        if bl:
            report["dropped"].append((rel, "blocklist term (private)")); print("  [local only] blocklist hit:", rel, "->", bl, file=sys.stderr); continue
        for sec in CFG.get("strip_sections", []):
            if glob_match(rel, sec["file"]):
                text = re.sub(r"(?ms)^" + re.escape(sec["heading"]) + r"\s*$.*?(?=^## |\Z)", "", text)
        for n, rx, rep in SOFT:
            text, c = rx.subn(rep, text)
            if c: report["redactions"][n] = report["redactions"].get(n, 0) + c
        def wl(m):
            target, _, label = m.group(1).partition("|")
            name = target.split("#")[0].split("/")[-1].strip()
            if name.lower() in keep:
                return m.group(0)
            return (label or name).strip()
        text, c = re.subn(r"\[\[([^\]]+)\]\]", wl, text)
        report["copied"].append(rel)
        if not a.dry_run:
            dst = out / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(text)

    lines = ["# Export manifest", "",
             f"Files copied: **{len(report['copied'])}**. Dropped by the safety scan: **{len(report['dropped'])}**.", "",
             "## Redactions applied", ""]
    lines += [f"- {k}: {v}" for k, v in sorted(report["redactions"].items())] or ["- none"]
    lines += ["", "## Never exported (policy)", "",
              "Personal and business notes, handoffs, logs, decisions, inbox items that are not research, finance,",
              "health, family, contacts, credentials, guest names and work details, client and employer details,",
              "full podcast transcripts, PDFs and zips, and the bulk Epstein email archive (only its small index is included).",
              "The export is allow-list only: a note is included only if it matches a rule in `tools/export-config.json`."]
    lines += ["", "## Dropped files", ""]
    lines += [f"- `{p}` — {why}" for p, why in report["dropped"]] or ["- none"]
    lines += ["", "## Copied files", ""] + [f"- `{p}`" for p in report["copied"]]
    if not a.dry_run:
        (ROOT / "EXPORT-MANIFEST.md").write_text("\n".join(lines) + "\n")
    print(f"copied {len(report['copied'])}, dropped {len(report['dropped'])}, redactions {report['redactions']}")
    for p, why in report["dropped"]: print("  dropped:", p, "-", why)

if __name__ == "__main__":
    main()
