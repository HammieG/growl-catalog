#!/usr/bin/env python3
"""Check the files added or changed in a pull request.

Fails if a pull request adds
  * a data file (HDF5, archives, numpy/pickle dumps, ...), or
  * any file larger than MAX_MB.

Usage:
    python scripts/check_pr_files.py <base-ref>        # e.g. origin/main
"""
import os
import subprocess
import sys

MAX_MB = 10
DATA_EXTENSIONS = (
    ".h5", ".hdf5", ".he5",
    ".tar", ".tar.gz", ".tgz", ".zip", ".gz",
    ".npy", ".npz", ".pkl", ".pickle", ".fits", ".dat",
)


def changed_files(base):
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AM", f"{base}...HEAD"],
        check=True, capture_output=True, text=True,
    ).stdout
    return [line for line in out.splitlines() if line]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    problems = []
    for path in changed_files(sys.argv[1]):
        if path.lower().endswith(DATA_EXTENSIONS):
            problems.append(f"{path}: data files must not be committed (keep them on the GROWL server).")
            continue
        if os.path.isfile(path):
            size_mb = os.path.getsize(path) / 1e6
            if size_mb > MAX_MB:
                problems.append(
                    f"{path}: {size_mb:.1f} MB is larger than {MAX_MB} MB. "
                    "Clear large notebook outputs or save figures as small PNGs."
                )
    if problems:
        print("This pull request adds files that do not belong in git:\n")
        print("\n".join(f"  - {p}" for p in problems))
        sys.exit(1)
    print("File check passed.")


if __name__ == "__main__":
    main()
