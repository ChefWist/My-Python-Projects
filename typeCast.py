#Convert the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #str


x, y, z = float(x), str(y), int(z)

#x = float(x)
#y = str(y)
#z = int(z)

print("X is " + str(x))
print("Y is " + str(y))
print("Z*3 is " + str(z*3))