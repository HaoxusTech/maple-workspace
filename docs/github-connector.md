# GitHub repository metadata

This Maple deployment can read its configured workspace repository metadata with:

```sh
gh api repos/HaoxusTech/maple-workspace --jq '{default_branch: .default_branch, private: .private, visibility: .visibility}'
```

The response reports the default branch and visibility; `private: false` and
`visibility: "public"` indicate a public repository. This read-only command does
not change the repository.

GitHub requests pass through InkBox and CheckBox using the configured relay;
credentials remain outside the Sandbox. Check the returned result before
claiming success. If a request fails or is denied, report the error and retain
its request ID rather than assuming the metadata was retrieved.
