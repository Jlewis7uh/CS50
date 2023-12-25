# Calculator app
x = input("What is the X value? ")
y = input("What is the Y value? ")

z = int(x) + int(y)  # Need to convert from str (def) to int

print("Answer = " + str(z))  # Need to convert z to str if adding text and int

# Another way
first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

print(first + second)
print("Answer = " + str(first + second))

# Floats: numbers ***with decimal points***
first = float(input("What is the first number? "))
second = float(input("What is the second number? "))

print(first + second)
print("Answer = " + str(round((first + second))))
print(round(first + second))

z = round(first + second)
print(f"{z:,}")  # this will make 1000 --> 1,000

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

b = round(num1 / num2, 2)  # Round to 2 digits

print(b)

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

b = (num1 / num2)  # Round to 2 digits

print(f"{b:.2f}")  # Round to 2 digits

# Using main()
def main():
    x = int(input("What is X? "))
    print("X Squared is " + str(square(x)))

def square(n):
    return n * n

main()





















