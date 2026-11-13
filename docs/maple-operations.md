# Maple operations

Use these deployment-specific procedures when the corresponding InkBox route
is configured. External effects are governed and audited, except public web
reads, which are audited without a CheckBox decision. Do not supply credentials
to the Sandbox or bypass the relay.

## Public submodules

The target design supports multiple shareable and private skill repositories as
workspace submodules, with symlinks from `.agents/skills/` to their contents.
This deployment currently configures one public shared-skills route; additional
repository routes are not yet implemented.

From the workspace root, initialize the committed gitlink through InkBox:

```sh
maple-submodule rules governance-requirements
maple-submodule skills .agents/shared-skills
```

These operations preserve existing work and do not activate governance rules.
If a route is unavailable, find the pinned gitlink with
`git rev-parse <workspace-revision>:<submodule-path>`, using `HEAD` or the
retained workspace ref. Read a pinned file with
`maple-web read https://raw.githubusercontent.com/HaoxusTech/<repository>/<gitlink>/<file>`.
To discover files, use
`maple-web fetch https://api.github.com/repos/HaoxusTech/<repository>/git/trees/<gitlink>?recursive=1`
and check for a truncated listing. Find the repository in `.gitmodules`. This
fallback does not initialize Git or enable proposals; report unavailable files.

## Expose initialized skills to Codex

The tracked `.agents/skills/shared-skills` link points to the shared-skills
submodule. Codex discovers its skills directly after initialization; no Maple
skill loader or per-skill links are needed. New skills appear after the pinned
submodule revision is updated and Codex reloads its skills. The current pinned
revision may contain no skills; a link to an uninitialized or unavailable
submodule cannot provide them.

For each other configured skill repository, add one relative symlink under
`.agents/skills/` to its initialized workspace submodule. Do not overwrite
existing files or links, silently resolve duplicate skill names, or publish
private repository details in this public workspace. Record links intended for
future sessions in the workspace repository; changes to skill content still
require a reviewed PR to its own repository. The configured InkBox routes
determine which repositories can be initialized and receive proposals.

## Workspace pull requests

Run the branch publisher from a committed Git worktree, not an empty temporary
repository. Select changed files or directories with `--path`; it is not a branch
name, and may be repeated:

```sh
maple-github-publish --branch-only --socket /relay/github.sock \
  --owner HaoxusTech --repository maple-workspace --title TITLE --path PATH
MAPLE_GH_PUBLICATION_ID=ID gh pr create --head BRANCH --base main --title TITLE --body TEXT
```

The publisher creates the remote branch; no local commit or push is needed.
Keep its publication ID and verified branch for the `gh` command. If the remote
base is unavailable, check the workspace object refresh. Reconcile overlapping
changes against the verified remote base without discarding session work.

To resume an interrupted branch publication, use `maple-github-publish --socket
/relay/github.sock --resume --run-id ID`. If the `gh` outcome is unconfirmed,
preserve its input and publication ID and use `MAPLE_GH_REQUEST_ID=ID` to
reconcile the same request. A retry may repeat an external effect. Supported
`gh pr review` and repository REST operations also use the relay; interactive
PR commands and native Git network operations are unavailable.

## Protected proposals

From the workspace root, select a changed path relative to the submodule:

```sh
maple-github-publish --branch-only --socket "$MAPLE_RULES_SOCKET" \
  --workspace "$PWD/governance-requirements" --owner HaoxusTech \
  --repository maple-governance --title TITLE --path PATH
maple-github-publish --branch-only --socket "$MAPLE_SKILLS_SOCKET" \
  --workspace "$PWD/.agents/shared-skills" --owner HaoxusTech \
  --repository maple-shared-skills --title TITLE --path PATH
MAPLE_GH_PUBLICATION_ID=ID gh pr create --repo HaoxusTech/REPOSITORY \
  --head BRANCH --base main --title TITLE --body TEXT
```

Use the appropriate publication ID and branch. Governance proposals are only
for a clear need or request; useful public skill proposals are encouraged.
Both repositories are public. All skill-repository proposals require CheckBox
review against the governance requirements, including checks against disclosure
of sensitive or nonpublic information before publication. The stage-one
allow-all reviewer does not provide that assessment. Leave protected-branch
review and merge to a human; if a route is unavailable or review is not
requirements-aware, record the pending proposal and report it.
