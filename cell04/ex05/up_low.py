user_input =input("enter string")

swapped_string = ""
for i in user_input:
    if i.islower():
        swapped_string += i.upper()
    elif i.isupper():
        swapped_string += i.lower()
    else:
        swapped_string += i
        
print(swapped_string)