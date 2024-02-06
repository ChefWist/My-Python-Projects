# collection thats orders and you cant change them
student = ("Bro",25,"male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Bro" in student:
    print("Bro is here!")