print("Python")
def text_star():
    for row in range(7):
        for col in range(4):
            if col==0 or (col==3 and (row==1 or row==2)) or ((row==0 or row==3) and (col>0 and col<3)):
                print("*", end="")
            else:
                print(end=" ")

        print()
text_star()


