def buy_stall(pounds, cost):
    if pounds > (cost - 1):
        pounds = pounds - cost
        print("You have £" + str(pounds) + " left.")
    else:
        print("You Need More Money")
    return pounds

def select_stall(current, length):
    stall = int(input("Which shop would you like to visit? There are " + str(total_stalls) + " Shops. "))
    if stall > length:
        stall = length
    elif stall < 1:
        stall = 1
    stall = stall - 1
    selected = mall[stall]
    cost = prices[stall]
    print("You are at a " + selected + " Shop, which costs £" + str(cost) + ".")
    change = input("Would you like to shop here? (y/n) ")
    if change == "y":
        left = buy_stall(money, cost)
        return left
    else:
        left = current
        return left
mall = ["Fruit", "Bike", "cube", "bed", "nail salon", "toy", "dealership"]
prices = [5, 20, 10, 14, 2, 12, 100]
total_stalls = len(mall)
money = 750
while True:
    print("You are at a mall, you have £" + str(money) + " to spend")
    money = select_stall(money, total_stalls)
