import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

player_choice = input("Choose rock, paper, or scissors: ")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors.")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock.")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats paper.")
else:
    print("Sorry, you lose. The computer chose", computer_choice + ".")
