#!/usr/bin/env python3
num_input=input("gimme a number: ")

try:
    num = float(num_input)
    if num == int(num):
        print("This number is interger")
    else:
        print("This number is decimal")
except ValueError:
    print("Invaid input try again")