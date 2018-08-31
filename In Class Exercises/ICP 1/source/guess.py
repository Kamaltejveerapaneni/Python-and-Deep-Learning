from random import randint
#selecting arandom number we use randint where we can get random integers
x=randint(0,9)
for x in range(9):
    y=int(input("Enter a number a single digit number:"))
    if(x== y):
        print("Your answer is PERFECT!! Congratulations!!")
        break
    elif x > y:
        print("Your answer is low than required")
    else:
        print("Your answer is high than required")




print(x)