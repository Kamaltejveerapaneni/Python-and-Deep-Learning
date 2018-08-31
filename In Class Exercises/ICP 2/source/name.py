







def list_to_tuple():
    input1 = input("numbers list \n")
    l = list(input1)
    print(l)
    t = tuple(l)

    print("",tuple(t[0] + t[-1]))

list_to_tuple()