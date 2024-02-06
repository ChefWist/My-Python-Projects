import random as r

def guess():
    trys = 3
    min = r.randint(1,10)
    max = r.randint(1,100)
    target = r.randint(min,max)
    nOfGuess = 0
    for x in range(trys):
        print("Guess a number from {min} to {max}!".format(min=min,max=max))
        guess = int(input("You have {guess} guesses left: ".format(guess=trys-nOfGuess)))
        if guess > target:
            print("Too High!")
        elif guess < target:
            print("Too Low!")
        else:
            print("Correct!")
            print("It took you {trys} trys!".format(trys=nOfGuess))
            return True
        nOfGuess+=1
    print("You lost! The number was {}!".format(target))
    return False
    
print("Guess A Number Game - In python")
amount = int(input("How many Games do you want to play?: "))
for i in range(1,amount+1):
    guess()