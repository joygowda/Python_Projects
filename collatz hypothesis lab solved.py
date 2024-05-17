counter = 0
c0 = int(input("please enter a number: "))


while c0 <= 0:
    print("please enter a positive number: ")
    c0 = int(input("please enter a number: "))
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
            print(c0)
        elif c0 % 2 != 0:
            c0 = 3 * c0 + 1
            print(c0)
        counter += 1 
    else:
        print("steps =", counter)