#!/usr/bin/env python3

import sys

if len(sys.argv) <3:
    print("none")
else:
    reverse_guy = sys.argv[1:]
    reverse_guy.reverse()

    for str in reverse_guy:
        print(str)


