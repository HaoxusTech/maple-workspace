"""Check required metadata in fictional Northstar Markdown release briefs."""

import argparse
from pathlib import Path
import re
import sys


def check_brief(text):
    errors = []
    for field in ("Demo ID", "Owner"):
        values = re.findall(
            rf"^[ \t]*(?:[-*+][ \t]+)?{re.escape(field)}:[ \t]*(.*)$",
            text,
            flags=re.MULTILINE,
        )
        if not values:
            errors.append(f"{field}: missing field")
        elif len(values) != 1:
            errors.append(f"{field}: expected exactly one field")
        else:
            value = values[0].strip().strip("`*_ ").strip()
            if not value or value.casefold() == "unknown":
                errors.append(f"{field}: must be nonempty and not unknown")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path, help="Synthetic Northstar Markdown brief")
    arguments = parser.parse_args()
    try:
        text = arguments.brief.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"ERROR: cannot read {arguments.brief}: {error}", file=sys.stderr)
        return 1
    errors = check_brief(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {arguments.brief} has Demo ID and Owner values (synthetic metadata only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
