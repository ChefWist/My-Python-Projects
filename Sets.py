# collection is unordered, unindexed and no duplicates

PencilCase = {"pen","pen","pencil","ruler"}
dishes = {"bowl","plate","cup", "pen"}

PencilCase.update(dishes)
PencilCase.add("Hilighter")
PencilCase.remove("ruler")
#PencilCase.clear()
School = PencilCase.union(dishes)

for x in School:
    print(x)
    
print(PencilCase.difference(dishes))
print(dishes.difference(PencilCase))
print(PencilCase.intersection(dishes))