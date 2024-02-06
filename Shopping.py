money = 50000
shops_cost = [25, 50, 200, 950, 500, 750]
shops = ["Nails", "Bike", "Tesco", "shop called asda", "Alid", "BestBuy"]

def ask(moola):
    money = moola
    shop = input("Which Shop? There are "+str(len(shops) )+": ")
    shop = int(shop)
    if shop > len(shops):
        print("This does not exist")
    elif shop < 1:
         print("This does not exist")
    else:
        current = shops[shop-1]
        print("You are at a "+current+" shop!")
        buy = input("Want to buy for "+str(shops_cost[shop-1])+"? Y/N: ")
        if buy == "Y":
            if money >= shops_cost[shop-1]:
                money-=shops_cost[shop-1]
                print("You have £"+str(money)+" left!")
            else:
                print("You need more money!")
    ask(money)

print("You have £"+str(money)+"! Spend wisly!")
ask(money)