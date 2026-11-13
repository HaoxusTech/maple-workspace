# Maple deployment workspace

The first MVP is a working Slack-to-Codex agent with persistent per-user sessions
and web/GitHub access through InkBox. An embedded terminal, reaction polish and
live-progress polish are enhancements, not MVP gates. An unsent terminal draft
may be lost on restart or disconnect; active work must not be interrupted.

This repository holds reusable work for one Maple deployment: scripts, skills,
schedule definitions and their dependencies. Each principal works in a separate
session worktree from this repository. Selected reusable text resources are
merged to `main` and pushed to the configured remote after session conclusion.
Binary artifacts stay on the persistent volume, outside GitHub.

Internet search and public page retrieval go through InkBox and are audited.

The worker's operating guidance is in [AGENTS.md](AGENTS.md). Deployment-owned
skills live under `.agents/skills/`; installed extensions remain separate,
pinned resources. Schedule definitions are not active merely because they exist:
Maple must install and confirm them after their dependencies are published.

The `governance-requirements/` submodule makes the protected
[maple-governance](https://github.com/HaoxusTech/maple-governance) repository
readable to the worker. CheckBox independently verifies its own immutable
approved revision; this checkout does not activate policy. The
`.agents/shared-skills/` submodule points to the public
[maple-shared-skills](https://github.com/HaoxusTech/maple-shared-skills)
repository, where reusable learned skills are proposed through human-reviewed
pull requests. Initialize them through the configured InkBox routes as described
in [Maple operations](docs/maple-operations.md).

This public test workspace is not the authoritative audit or transaction store.
Keep nonpublic memories on the PVC, and never put credentials, databases,
runtime histories or temporary outputs in Git.

See the [GitHub connector guide](docs/github-connector.md) for reading workspace repository metadata through the governed relay.
