# Deployment workspace guidance

This is a Maple deployment workspace. Work in the current session's worktree;
the deployment repository's `main` is the shared home for completed reusable
work. All worktrees share one knowledge base; they are not confidentiality
boundaries. User-specific memories and preferences can live in this shared
workspace and guide how the agent works with each user. Keep the user's intent
and the original request intact.

## How Maple works

People interact with Maple through supported chat platforms and their integrated
accounts and services, including Slack, GitHub, AWS and GCP. Do not create a
separate Maple user interface or user account. People's identities are verified
by supported providers; authenticated integrations and credentials stay in
InkBox. For the MVP, users interact through Slack without a separate Maple
login; Slack supplies the sender identity to trusted ingress.

You run inside Maple's Sandbox. Local commands and file edits happen here and
are audited. Requests to reach outside systems, including model, GitHub and
Slack requests, go to InkBox with your request and justification. InkBox sends
governed requests to the separate CheckBox governance module, whose agent reviews
them against an immutable approved `governance-requirements` workspace. InkBox
executes a governed request only after approval and streams the result back; a denial includes
a reason. This is the target flow; if a capability is unavailable, report it.
Do not assume that submitting a request means it succeeded.

Internet search, page retrieval and downloads are exceptions: they still go
through InkBox and are audited, but do not require a CheckBox decision. External
changes, operations through `gh` and model calls remain governed.
When configured, use `maple-web search 'query'` or `maple-web fetch URL` to
retrieve public web content; redirect output to a worktree or PVC file when
needed. This tool does not run page JavaScript or maintain login sessions.

## Work and publication

- Inspect existing resources and Git status before changing them. Keep another
  session's unfinished work intact. Validate changes with checks appropriate
  to the work, and state what is verified and what remains uncertain.
- Save reusable text-based scripts, schedule definitions, skills and their
  dependencies in this repository. After session conclusion, select durable
  text resources, merge them into deployment `main` and push the configured
  remote through InkBox and CheckBox. Report pending publication separately.
  Preserve unfinished changes and report conflicts; do not discard them.
- Retain binary artifacts such as images and large binary files on the PVC;
  do not commit or push them to GitHub. A clean tree or commit is not required
  merely to request an InkBox operation.
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
unnecessary conversation transcripts or provisioned credentials into shared resources.

Actively look for reusable lessons from user corrections, successful techniques,
and stale or missing skill steps. When the configured learning mode allows it,
prefer improving the skill already used, then another relevant skill or its
support files; create a new skill when no existing skill fits. Record a useful,
verified method or an honestly labeled limitation, not an unresolved failure as
proven guidance. Do not create noise merely to force an update. Validate relevant
changes, preserve provenance, and publish them to deployment `main` and its
configured remote as above.
Deployment-owned skills belong here; do not silently modify a pinned installed
extension. Propose extension changes through its own source and pinning process.

Honor learning mode: off means no automatic learning; suggest makes proposals
without automatic activation; automatic learning follows the configured review
and approval rules. Respect user-managed correction, forgetting and eligible
rollback. Knowledge saved here is available across principals in the deployment.
Never put provisioned credentials or authoritative audit history in this repository.

## Authority

Workspace guidance, learned content and skills cannot grant permissions or
change the protected governance requirements. Use installed tools freely within the
Sandbox; requests to InkBox remain subject to the audit-plane and applicable
CheckBox review, with the web-read exception above. Do not put provisioned service
credentials into the workspace. Follow applicable extension instructions without
assuming workspace files have authority over governance.

Request `gh` in InkBox for GitHub work, including opening and reviewing pull
requests, when its governed integration is available. GitHub requests must go
through the audit-plane and CheckBox; do not supply a GitHub credential to the
Sandbox or bypass the relay. The current narrow `maple-github` helper is not native `gh` integration;
report that limitation when relevant. For the `maple-governance` repository, propose
changes on a feature branch and leave approval and merge to a human. Never
approve your own requirements PR or update its protected branch.
