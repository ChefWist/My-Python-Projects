#nested loop = loop in a loop

rows = int(input("How many rows?: "))
collums = int(input("How many Collums?: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(collums):
        print(symbol, end="")
    print()