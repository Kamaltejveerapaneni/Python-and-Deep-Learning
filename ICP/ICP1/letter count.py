x=input("enter a string")
count1=0
count2=0
count3=0
for i in x:
    if(i.isdigit()):
        count1=count1+1
    elif(i.isalpha()):
        count2=count2+1
    elif(i.isspace()):
        count3+=1

print("digits is")
print(count1)
print("letters")
print(count2)
print("space count")
print(count3)