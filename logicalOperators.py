# (and,or,not) = used to check if 2 or more conditinal statements are True
temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp<= 30):
        print("The temperature is bad today!")
        print("Stay indoors!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")