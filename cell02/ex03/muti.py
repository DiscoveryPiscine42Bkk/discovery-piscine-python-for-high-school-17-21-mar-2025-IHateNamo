#!/usr/bin/env python3
first_num = int(input('Enter the first number: '))
sec_num = int(input('Enter the second number: '))
Multi_kan = first_num * sec_num

print(str(first_num) + " x " + str(sec_num) + " = " , Multi_kan)

if Multi_kan > 0:
    print("The result is positive. ")
elif Multi_kan < 0:
    print("The result is negative. ")
elif Multi_kan == 0:
    print("The result is positive and negative. ")
else:
    print("ERROR Enter number again .")
