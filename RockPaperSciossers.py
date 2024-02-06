import random as r 

while True:
    choices = ["rock","paper","scissors"]

    ai = r.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock,Paper! or scissors?: ").lower()
    
    if player == ai:
        print("computer: "+ai)
        print("You: "+player)
        print("Tie!")
    elif player == "rock":
        if ai == "paper":
            print("computer: "+ai)
            print("You: "+player)
            print("You Lose!")
        if ai == "scissors":
            print("computer: "+ai)
            print("You: "+player)
            print("You Win!")
    elif player == "paper":
        if ai == "scissors":
            print("computer: "+ai)
            print("You: "+player)
            print("You Lose!")
        if ai == "rock":
            print("computer: "+ai)
            print("You: "+player)
            print("You Win!")
    elif player == "scissors":
        if ai == "rock":
            print("computer: "+ai)
            print("You: "+player)
            print("You Lose!")
        if ai == "paper":
            print("computer: "+ai)
            print("You: "+player)
            print("You Win!")
    play = input("Play? yes/no: ").lower()
    if play == "yes":
        break
print("Bye! Play again!")