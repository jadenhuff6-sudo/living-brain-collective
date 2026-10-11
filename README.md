# Living Brain

This is the open research behind the Circle of Light show, Mastering the Matrix. It is a living map of theories, claims, people, institutions and sources, and a place where you can help build it.

The goal is simple: a theory of everything that anyone can check, challenge and add to. Every claim should point to where it came from, so you can see what is documented, what is only reported, and what is one person's idea.

## What is in here

- `viewer/`: the interactive brain map. Open `viewer/index.html` in a browser. It works on its own and needs no setup.
- `content/`: the research pages behind the show. Theory of Everything map claims and entities, research briefs, the 13 Families series prep, trending dockets, and notes on sources we pulled live on stream.
- `tools/`: the script that refreshes `content/` from the private vault with the same safety filter each time.
- `EXPORT-MANIFEST.md`: the exact list of files in `content/`, and what the privacy filter removed.

## How you can help

Open an issue using one of three forms:

1. **Theory**: a theory or connection you think belongs on the map.
2. **Cover this on the show**: a topic you want looked at on a stream.
3. **Critique of a narrative**: a place where a claim on the map, or a claim in the media, does not hold up.

You can also open a pull request with a new or corrected page. Pull requests are welcome.

## The rules

**Sources are required.** A theory or critique without a source will be closed. A source can be a document, a court record, a paper, a book with page numbers, or a recording with a timestamp. "Everyone knows" is not a source.

**Say what kind of claim it is.** Documented (a record shows it), reported (someone credible says it, and you can name them), or theory (an idea or an inference). Mixing them up is the most common mistake.

**No private information.** Do not post anyone's home address, phone number, email, workplace complaints or health details. Do not post private messages. Public figures are discussed through their public record only.

**Be fair to people.** Critique the claim and the evidence, not the person. No harassment, no slurs, no calls for harm.

**One claim at a time.** Short and specific beats long and sweeping.

## Nothing merges without approval

Every issue and pull request is read by Jaden before anything changes. The `main` branch is protected, so nothing can be merged without his review. Being rejected is not personal. It usually means a source is missing or the claim is not clear yet.

If an idea is accepted, it goes into the map with your source attached, and it may be discussed on a stream.

## How the content is kept clean

`content/` is a filtered copy. The original notes are private and stay private. The export is allow-list only, so a note is copied only if it is on the approved list. It then goes through a scan for emails, phone numbers, keys and a private list of names that must never appear. A file that fails is left out, not patched. See `tools/export_from_vault.py`.

If you spot something in here that should not be public, open an issue titled "Privacy" without repeating the sensitive detail, and it will be removed quickly.

## License

Research text and the map: CC BY 4.0, so you can reuse it with credit. Code in `tools/` and `viewer/`: MIT.
