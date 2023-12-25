# Functions (def): inventing our own functions
def hello(to="world"):
    print("Hello, " + to)

hello()
name = input("What's your name? ")
hello(name)

# Or
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello, " + to)

main()

# Returns (see: calculator.py)
