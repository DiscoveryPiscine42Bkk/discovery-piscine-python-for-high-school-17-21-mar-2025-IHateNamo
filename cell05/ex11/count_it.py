#!/usr/bin/env python3

import sys

args = sys.argv[1:]  # Exclude  script

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")