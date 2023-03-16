# guess number game
import random

random_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))
while guess != random_number:
    if guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("You win!")