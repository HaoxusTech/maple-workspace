# Northstar review-readiness checklist

For the fictional Northstar release only; use synthetic information throughout.
This checklist is not a release approval or a governance requirement.

- [ ] Run the existing brief checker from the workspace root:
  `python3 scripts/northstar/check_brief.py docs/northstar/live-20261113-a1.md`.
  Record the observed output and exit status; resolve errors before marking
  the metadata check passed.
- [ ] Confirm a named owner in the brief; do not infer missing ownership.
- [ ] Include a working [release brief link](live-20261113-a1.md) in the review
  handoff or release-readiness issue.
- [ ] Record each unverified check as **pending**, with the evidence or review
  still needed. Do not mark it passed merely because it is listed here.
- [ ] Keep actual review and release approval pending until confirmed by the
  appropriate reviewer; the checker validates metadata, not release readiness.
