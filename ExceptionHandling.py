try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("ERROR 1-CAN'T DIVIDE BY 0")
except ValueError as e:
    print(e)
    print("ERROR 2-Enter Numbers!")
except Exception as e:
    print("ERROR 0-unknown")
else:
    print("'Cop! This one is good!' You did not have an error!")
    print(result)
finally:
    print("This will always be here:)")