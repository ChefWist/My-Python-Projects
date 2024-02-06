# Changes a loops execution rrom its normal squence

# break = used to terminate the loop
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder
while True:
    name = input("Enter Your Name: ")
    if name != "":
        break

phone = "733-737-8373"

for i in phone:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)