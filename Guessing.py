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

guess(10)

# Guess the number (user has computer guess)
import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess2 = random.randint(low, high)
        else:
            guess = low                         # doesn't matter could be high
        feedback = input(f"Is {guess2} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess2 - 1
        elif feedback == 'l':
            low = guess2 + 1

    print(f'Yay, Great job Computer! You correctly guessed {guess2}')

computer_guess(25)
