import random

Options = ["rock", "paper", "scissors"]
Computer = Options[random.randint(0,2)]
Player= input().lower()
if Computer == Player:
    print("tie, both threw " + Player)
elif Player == "rock":
    if Computer == "paper":
        print("you lose, Computer threw paper")
    else:
        print("you win, Computer threw Scissors")
elif Player == "paper":
    if Computer == "scissors":
        print("you lose, Computer threw scissors")
    else:
        print("you win, Computer threw rock")
elif Player == "scissors":
    if Computer == "scissors":
        print("you lose, Computer threw rock")
    else:
        print("you win, Computer threw paper")
else:
    print("Not a valid input")
