def hello(**names):
    #print("Hello, "+names["first"]+" "+names["last"]+"!")
    print("Hello",end=" ")
    for key,value in names.items():
        print(value, end=" ")
    
hello(title="mr",first="Bro",middle="dude",last="code")