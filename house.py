# Match
name = input("What's your name? ")

if name == "Harry":
    print("Your home is: Gryffindor")
elif name == "Hermione":
    print("Your home is:Hermione")
elif name == "Ron":
    print("Your home is:Gryffindor")
elif name == "Draco":
    print("Your home is:Slytherin")
else:
    print("Who??")

# Refine code
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Your home is: Gryffindor")
elif name == "Draco":
    print("Your home is:Slytherin")
else:
    print("Who??")

# Match actually
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who??")