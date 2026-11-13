# Session handoff

At explicit conversation end or after more than six hours of inactivity,
without interrupting active work, complete the retrospective even when learning
is off. Explain what happened, material decisions and their reasons, evidence,
results, failures and uncertainty. Distinguish observed facts from your account;
do not invent hidden reasoning. If a material reason is unknown, mark the
retrospective incomplete and leave it pending for recovery.

When `MAPLE_NOTE_SOCKET` and `MAPLE_INKBOX_UID` are configured, submit a JSON
object on standard input to `maple-decision-note`. The retrospective has `kind`
`retrospective`, `summary` and `outcome` strings, a `decisions` array with
`action`, `reason` and an `evidence` reference array for each decision, an
`uncertainties` string array, and `status` `complete` or `incomplete`. Use a
null reason only with `incomplete`. For a scheduled preservation goal include
its exact 32-character `goal_id`. Keep the printed note ID: a recorded response
with an audit sequence confirms receipt. Reconcile an unconfirmed result using
the same ID and exact content. If the tool is unavailable, report the pending
retrospective. Notes are the agent's account, not independently verified facts.
The latest five available same-session notes and recent chat may accompany
governance reviews when configured; authorized audit lookup may provide more.

Strongly consider preserving useful deployment-specific text and lessons in
workspace `main` and useful public skills through a human-reviewed
`maple-shared-skills` PR. No change is needed when nothing is appropriate.
Keep nonpublic memories and binary artifacts on the PVC, and never publish
credentials or raw audit history. Honor the configured learning mode and do
not silently modify pinned extensions.

For workspace publication, first check `maple-workspace-publish --help`: its
`--main-worktree` description must say that no checkout is modified. Older
publishers may require a separate clean `main` worktree; leave publication
pending if the safe version is unavailable. When configured, select changed
files or directories from the session worktree:

```sh
maple-workspace-publish --socket /relay/github.sock --owner HaoxusTech \
  --repository maple-workspace --title 'Preserve reusable work' --path PATH
```

Repeat `--path` as needed. Preserve the printed publication ID; on an
interrupted or unconfirmed run use `maple-workspace-publish --socket
/relay/github.sock --resume --run-id ID`. Reconcile a moved remote or failed
retention without losing local work. Report denials, conflicts and pending
results instead of claiming publication.

The publisher retains the confirmed revision but does not update this checkout.
At a safe point, decide whether to integrate that verified revision into your
own worktree. Check ancestry and preserve tracked, untracked and ignored work;
use `git merge --ff-only --no-overwrite-ignore` for a safe fast-forward. A newly
published untracked file can block it even when the contents match. Compare the
file and its type with the exact published revision first. If they match,
preserve that exact path in a named stash before integrating; do not stash
unrelated paths. If they differ, or the revision, worktree or result is
uncertain, leave the work intact and report the pending reconciliation.

Follow [Maple operations](maple-operations.md) for protected proposals, which
require human review and merge.
