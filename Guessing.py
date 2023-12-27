# Guess the number
import random

def guess(x):
    random_number = random.randint(1, x)  # random number between 1 and x
    guess = 0                                # guess will never be 0, so it will keep going
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess again, too low!")
        elif guess > random_number:
            print("Sorry guess again, too high!")
        else:
            print(f"Great job, you found the number {random_number} correctly!!")

guess(34)