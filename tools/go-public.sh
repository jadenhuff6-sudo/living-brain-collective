#!/bin/sh
# Run ONLY after the owner has reviewed the file list and privacy scan and said go.
# Flips the repo public, then turns on branch protection (needs 1 approving review from the owner).
set -e
R=jadenhuff6-sudo/living-brain-collective
gh repo edit "$R" --visibility public --accept-visibility-change-consequences
gh api -X PUT "repos/$R/branches/main/protection" --input - <<'J'
{"required_status_checks":null,"enforce_admins":false,"required_pull_request_reviews":{"required_approving_review_count":1,"require_code_owner_reviews":true},"restrictions":null,"allow_force_pushes":false,"allow_deletions":false}
J
gh api -X PUT "repos/$R/vulnerability-alerts" >/dev/null 2>&1 || true
echo "public, main protected"
