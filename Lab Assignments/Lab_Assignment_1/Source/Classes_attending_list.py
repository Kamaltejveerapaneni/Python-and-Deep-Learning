x = input("enter the students list for python.Enter none to halt entering")
i = 0
l1 = []
while(x!="none"):
    l1.append(x)
    i = i+1
    x = input("enter next student details in python class")
print(l1)
y = input("enter the students list for web development .Enter none to halt entering")
j = 0
l2 = []
while(y!="none"):
    l2.append(y)
    j = j+1

    y = input("enter next student details in python class")
print(l2)
print("Hello_2")
l3 = [x for x in l1 if x not in l2]
print(l3)
print("hello3")



