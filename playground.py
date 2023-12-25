# If the user says "Hello": give $20
# If the user doesn't say "Hello": give $0
# If the user's input contains H/h: give $5

greet = input("What is your greeting? ")

if greet == "Hello" or greet == "hello":
    print("Good job, here's $20")
elif "H" in greet or "h" in greet:
    print("Your greeting contains an H/h, so here is $5")
else:
    print("You didn't say hello, and your greeting contains no H/h, $0 awarded")


