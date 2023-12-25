# Grade generator (and)
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F, you failed, re-test required")

# Tighten it up (more efficient, fewer questions)
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F, you failed, re-test required")

# Is a given number even or odd (parity with modulo %)
a = int(input("What is X? "))

if a % 2 == 0:  # If there is no remainder, it is an EVEN number (div/2 to find EVEN)
    print("This is an even number")
else:
    print("This is an odd number")


# Build function to find even or odd
def main():
    a = int(input("What is X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()

# Improve code
def main():
    x = int(input("What is X? "))
    if is_even2(x):
        print("Even")
    else:
        print("Odd")


def is_even2(n):
    return True if n % 2 == 0 else False

main()

# Match
# see house.py