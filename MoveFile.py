
# do not run this


import os 
src = "test1.txt"
des = "dupe.txt"

try:
    os.replace(src,des)
    print("Source was moved!")
except FileNotFoundError:
    print("Source was not found!")