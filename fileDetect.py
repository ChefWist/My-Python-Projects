import os 

path = "test1.txt"

if os.path.exists(path):
    print("This Location Exists")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That Location Does not exist!")

    