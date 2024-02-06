text = ""
while True:
    user = input("Type A Line!: (type done to finish): (type new to make a new one): ")
    text+=(user+"\n")
    if user.lower() == "done":
        break
    elif user.lower() == "new":
        text = ""
        break
    
with open("CreateAFileTest.txt",'w') as file:
    file.write(text)