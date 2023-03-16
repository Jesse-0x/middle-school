# guess number game
import random

random_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))
if guess == random_number:
    print("Yay! you guessed it right!")
else:
    print("Sorry, you guessed wrong!")
    print("The number was", random_number)