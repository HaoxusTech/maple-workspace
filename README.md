# Maple deployment workspace

This repository holds reusable work for one Maple deployment: scripts, skills,
schedule definitions and their dependencies. Each principal works in a separate
session worktree from this repository. Selected reusable text resources are
merged to `main` and pushed to the configured remote after session conclusion.
Binary artifacts stay on the persistent volume, outside GitHub.

The worker's operating guidance is in [AGENTS.md](AGENTS.md). Deployment-owned
skills live under `.agents/skills/`; installed extensions remain separate,
pinned resources. Schedule definitions are not active merely because they exist:
Maple must install and confirm them after their dependencies are published.

This repository is distinct from this deployment's protected governance
requirements repository, `maple-governance`. It is not the authoritative audit
or transaction store. Never put credentials, databases, runtime histories or
temporary outputs in Git.
