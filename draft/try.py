


a=False
b=False

while a==False:
    print("part 1")
    enter=input(":")
    if enter== "1":
        print ("1-1")
        a=True
    else:
        print("part 1-2")
        while b==False:
            print ("part 2")
            enter=input(":")
            if enter== "1":
                print("PART 2-1")
                print ("Enter")
                b=True
                a=True
            else:
                print("PART 2-2")
                print ("no")
                a=True
                b=True