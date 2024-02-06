# changable unordered collection of unique key: value pairs
capitals = {'USA':'WashingTon DC','India':'New Dehli',"china":"beijing"}
capitals.update({'Germany':'berlin'})
capitals.update({'USA':'Los Vegas'})
capitals.pop('china')
#capitals.clear()
#print(capitals["India"])
#print(capitals.get('India'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
for key,value in capitals.items():
    print(key,value)