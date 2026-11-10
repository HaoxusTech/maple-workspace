# Maple GitHub tools

When configured, `refs/maple/workspace-main` is a locally retained shared
revision and may be stale. Verify remote state through InkBox when publication
needs it, and preserve local work, including ignored files.

## Workspace PRs

When configured, the Sandbox `gh` command runs supported operations through a
real isolated `gh` executable, InkBox and CheckBox. For the configured
workspace repository, stage selected text changes with `maple-github-publish
--branch-only --socket /relay/github.sock --owner HaoxusTech --repository maple-workspace
--title TITLE --path README.md` (replace `README.md` with a changed file or
directory; repeat `--path` for additional paths). `--path` is not a branch name.
Run the publisher from a committed Git worktree, not an empty temporary Git
repository. If the remote base is unavailable locally, check the configured
InkBox workspace object refresh. If changes overlap, reconcile them against the
verified remote base in a temporary detached Git worktree; preserve the session
worktree and verify the remote changes before publishing. This does not require
another agent session.
The publisher creates the remote branch; no local commit or push is needed.
Keep its printed publication ID and verified branch. Then use
`MAPLE_GH_PUBLICATION_ID=ID gh pr create --head BRANCH --base main
--title TITLE --body TEXT`. Use `gh pr review NUMBER --comment --body TEXT` to
comment on a PR. `--approve` and
`--request-changes` are also supported; comments and change requests need a
body. Supported `gh api` repository REST requests remain available. Each
external request is governed and audited; never supply GitHub credentials to
the Sandbox or bypass the relay.

If staging is interrupted, resume it with `maple-github-publish --socket
/relay/github.sock --resume --run-id ID`; it remains branch-only. The `gh`
command prints a separate request ID. If its outcome is unconfirmed, preserve
the same input and publication ID and use `MAPLE_GH_REQUEST_ID=ID` to reconcile
it; a retry may repeat an external effect. Creation reviews the staged text and observed branch refs;
those observations are point-in-time and can be reused on retry. Interactive
PR commands and native Git network operations are unavailable. Report an
unavailable capability rather than claiming success.

When the corresponding socket is configured, stage protected proposals from
the workspace root with the changed path relative to that submodule:

- Governance, only when clearly necessary or requested: `maple-github-publish
  --branch-only --socket "$MAPLE_RULES_SOCKET" --workspace "$PWD/governance-requirements"
  --owner HaoxusTech --repository maple-governance --title TITLE --path PATH`.
- Reusable public skills, strongly encouraged when useful: `maple-github-publish
  --branch-only --socket "$MAPLE_SKILLS_SOCKET" --workspace "$PWD/.agents/shared-skills"
  --owner HaoxusTech --repository maple-shared-skills --title TITLE --path PATH`.

Keep the printed publication ID and branch, then run `MAPLE_GH_PUBLICATION_ID=ID
 gh pr create --repo HaoxusTech/REPOSITORY --head BRANCH --base main --title TITLE
 --body TEXT` for that repository. Replace the placeholders with the actual values.
Both repositories are public, so do not include nonpublic information or binary
artifacts. Leave review and merge to a human; never approve or merge your own
proposal or update the protected `main` branch. If a socket is unavailable,
record the pending proposal and report the limitation.
