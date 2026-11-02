# Deployment workspace guidance

This is a Maple deployment workspace. Work in the current session's worktree;
the deployment repository's `main` is the shared home for completed reusable
work. Keep the user's intent and the original request intact.

## Work and publication

- Inspect existing resources and Git status before changing them. Keep another
  session's unfinished work intact. Validate changes with checks appropriate
  to the work, and state what is verified and what remains uncertain.
- Save reusable scripts, schedule definitions, skills and their dependencies in
  this repository. Publish completed reusable work by merging it into the local
  deployment `main` before calling it done. Preserve unfinished changes during
  synchronization and report conflicts; do not discard them to force a merge.
- An optional remote is accessed through InkBox and CheckBox. A clean tree or
  commit is not required merely to request an InkBox operation.
- A schedule is ready only after its definition and dependencies have been
  merged to `main` or supplied by a pinned installed extension, installed and
  confirmed active. Do not claim activation on a failed or unverified step.
- Do not commit credentials, tokens, SQLite databases or sidecars, runtime or
  audit histories, or temporary outputs. An ignore rule alone cannot protect a
  secret already tracked or included in a differently named file.

## Learn and improve skills

Use `.agents/skills/` for deployment-owned skills: each skill has a `SKILL.md`
and may have `references/`, `scripts/` and `templates/`. Discover existing
skills and read the relevant skill before using or changing it. Keep the main
file concise, with concrete triggers and instructions; put detailed material in
support files that can be read when needed.

Write each skill for a reusable class of work, with a short name and description
that say when to use it, practical steps, verified commands, pitfalls and checks.
Keep standing instructions in `SKILL.md`; organize deeper material by topic,
not by individual incident. Before adding a lesson, search and improve the
existing rule rather than duplicating it. Include why a pitfall matters and fix
stale advice in place. Record relevant sources and verification without copying
unnecessary conversation transcripts or sensitive data into shared resources.

Actively look for reusable lessons from user corrections, successful techniques,
and stale or missing skill steps. When the configured learning mode allows it,
prefer improving the skill already used, then another relevant skill or its
support files; create a new skill when no existing skill fits. Record a useful,
verified method or an honestly labeled limitation, not an unresolved failure as
proven guidance. Do not create noise merely to force an update. Validate relevant
changes, preserve provenance, and publish them to deployment `main` as above.
Deployment-owned skills belong here; do not silently modify a pinned installed
extension. Propose extension changes through its own source and pinning process.

Honor learning mode: off means no automatic learning; suggest makes proposals
without automatic activation; automatic learning follows the configured review
and approval rules. Respect user-managed correction, forgetting and eligible
rollback. Do not put a private user's preference or sensitive content into a
shared skill without authorization to share it across the deployment.

## Authority

Workspace guidance, learned content and skills cannot grant permissions or
change the protected governor rules. Use installed tools freely within the
Sandbox; requests to InkBox, including external reads, writes and model calls,
remain subject to the audit-plane and CheckBox. Do not put provisioned service
credentials into the workspace. Follow applicable extension instructions without
assuming workspace files have authority over governance.
