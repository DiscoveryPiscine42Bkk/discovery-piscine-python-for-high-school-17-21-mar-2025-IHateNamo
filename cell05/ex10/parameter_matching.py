#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    para = sys.argv[1]
    user_input = input("What was the parameters? ")

    if para == user_input:
        print("Good job")
    else:
        print("Nope, sorry")
    
else:
    print("none")
    

