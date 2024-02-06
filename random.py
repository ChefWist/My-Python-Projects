import random as r

x = r.randint(1,6)
y = r.random()

options = ['rock','paper','scissors']
z = r.choice(options)

cards = [1,2,3,4,5,"J","Q","K","A"]
r.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)