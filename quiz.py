#Quiz Game
#----------------------

def newGame():
    guesses = []
    correctGuesses = 0
    questionNum = 1
    
    for key in questions:
        print("----------------------")
        print(key)
        print(" ")
        for i in options[questionNum-1]:
            print(i)
        guess = input("Enter (a,b or c): ").lower()
        guesses.append(guess)
        
        correctGuesses+=CheckAnswer(questions.get(key),guess)
        questionNum+=1
    displayScore(correctGuesses,guesses)

def CheckAnswer(answer,guess):
    if answer == guess:
        print("Correct! ")
        return 1
    else:
        print("Wrong!")
        return 0

def displayScore(correctGuesses,guesses):
    print("----------------------")
    print("Result: ")
    print("----------------------")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
        
    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int((correctGuesses / len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    
    response = input("Do you eant to play again: (yes/no): ").lower()
    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: ":"a",
    "What year was python created?: " : "b",
    "Python is tributed to which comedy group?: ":"c"
}
options = [
    ["a. Guido van Rossum", "b. Elon Musk", "c. Bill Gates"],
    ["a.1989","b.1991","c.733"],
    ["a.Loney","b.Mosh","c.Monty Python"]]

newGame()
while play_again():
    newGame()
print("See You soon (Date: Tue 6 Febuary 2024)")