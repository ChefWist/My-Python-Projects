import os 

path = "test1.txt"
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
    
    