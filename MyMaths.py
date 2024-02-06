class math:
    amount_of_functions = 4
    functions = ["Multiply","divide","add","takeAway"]
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x/y
    def add(x,y):
        return x+y
    def takeAway(x,y):
        return x-y
        
import random as r
x = r.randint(1,100)
y = r.randint(1,100)
print(x,y)
print(math.add(x,y))
print(math.takeAway(x,y))
print(math.multiply(x,y))
print(math.divide(x,y))