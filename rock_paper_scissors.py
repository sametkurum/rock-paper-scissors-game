# ROCK, PAPER, SCISSORS GAME

import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)

def main():
    player = input("Rock, paper, scissors?: ")

    if player not in choices:
        print("you wrote wrong")
        main()

    elif computer == player:
        print("Tie!")

    elif computer == "paper":
        if player == "rock":
            print("Computer won")
        elif player == "scissors":
            print("You won")

    elif computer == "scissors":
        if player == "paper":
            print("Computer won")
        elif player == "rock":
            print("You won")

    print(f"computer made: {computer}")
    print("-------------------------")

def askAgain():
    check_again = input("Do you wanna play again (Yes or no): ")
    

    if check_again == "yes":
        main()
    elif check_again == "no":
        print("Good bye!")
    else:
        print("What do you mean?")
        askAgain()

main()
askAgain()
