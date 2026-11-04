"""Check that Claude Code's settings.json is valid JSON with no repeated keys.

Part of Quota Keeper, token-saving tactics by Jaber Neto (JN Softworks).
Copyright (c) 2026 Jaber Neto (JN Softworks). SPDX-License-Identifier: MIT (full text in the guide's LICENSE.md).

Usage:
    python check_settings.py [path]     (default: settings.json in the config folder)

The config folder is CLAUDE_CONFIG_DIR if that variable is set, otherwise ~/.claude.

A repeated key (two "hooks" or two "env" blocks) is valid JSON, but only the last one counts,
so the hooks or settings in the first one silently stop working.
"""

import json
import os
import sys


def no_repeats(pairs):
    keys = [k for k, _ in pairs]
    repeated = sorted({k for k in keys if keys.count(k) > 1})
    if repeated:
        raise ValueError(f"repeated key {', '.join(repeated)}: only the last one counts; merge them into one")
    return dict(pairs)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    base = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(base, "settings.json")
    try:
        with open(path, encoding="utf-8-sig") as fh:
            json.load(fh, object_pairs_hook=no_repeats)
    except FileNotFoundError:
        print(f"not found: {path} (nothing to check)")
        return 0
    except ValueError as e:
        print(f"PROBLEM in {path}: {e}")
        return 1
    print(f"ok: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
