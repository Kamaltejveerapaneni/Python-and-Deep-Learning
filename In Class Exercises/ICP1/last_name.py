#
x= input("First name : ")
z= input("Last name: ")
y=[]
f=[]
y=x.split(" ")#splitting name
f=z.split(" ")
print(y)#original
print(f)


rev_firstname=''.join(x[::-1]) #joining again
print(rev_firstname)

rev_lastname=''.join(z[::-1])
print(rev_lastname)


#