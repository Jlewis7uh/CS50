name = input("What's your name? ")
# name = input("What's your name? ").strip().title() would complete the following steps in one line
print("Hello, " + name + ":)")

name = name.strip()  # Remove whitespace from str, the (.) brings up a "method"
name = name.capitalize()  # Capitalize the first character
name = name.title()  # Cap first letter of each word
name = name.strip().title()  # Do both at the same time
'''

Anything between the three (') is a comment

'''
print("Hello, ", end="")  # \n creates a new line
print(name)
print("Hello,", name, sep=" ")

print('hello, "friend"')
print("hello, \"friend\"")
print(f"hello, {name}")

# About to create a new variable for name (name_2) and will split up the result
name_2 = input("What's your name? ").strip().title()
first, last = name_2.split(" ")
print(f"Hello, {first}")

# Integers (int): numbers ***without decimal points***
'''
+ addition
- subtraction
* multiplication
/ divison
% modulo (gives you the remainder)
'''
