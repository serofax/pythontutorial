while True:
    try:
        x = int(input("I want a number: "));
        break
    except ValueError:
        print ("A NUMBER!!!!");


print (x)

raise ValueError("hehe")

