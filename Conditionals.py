# Conditionals: asking and answering questions that will execute code

'''
> greater than
>= greater than or equal to
< lesser than
<= lesser than or equal to
== equality
!= not equal to
'''

# If: if this is true then do this
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("X is less than Y")
if x > y:
    print("X is greater than Y")
if x == y:
    print("X is equal to Y")

# Else if (elif): depends on if prev question was T or F
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("X is less than Y")
elif x > y:
    print("X is greater than Y")
elif x == y:
    print("X is equal to Y")

# Else
x = int(input("What is X? "))
y = int(input("What is Y? "))

if x < y:
    print("X is less than Y")
elif x > y:
    print("X is greater than Y")
else:                                # No need to ask, only logical remaining option
    print("X is equal to Y")

if x < y or x > y:
    print("X is not equal to Y")
else:
    print("X is equal to Y")

# Could my code be even better? Ask fewer questions (using != and ==)
if x != y:
    print("X is not equal to Y")
else:
    print("X is equal to Y")

if x == y:
    print("X is equal to Y")
else:
    print("X is not equal to Y")

# And (multiple questions)
# See grade.py