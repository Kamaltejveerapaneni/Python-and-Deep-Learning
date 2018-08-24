x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
value=input("enter your choice")
z=x%y
a=x/y
t=x+y
s=x*y
g=x-y
if(value== 'a'):
 print("Quotient is: ", int(a))
elif(value=='z'):
 print("Remainder is: ", int(z))
elif(value=='t'):
 print("Sum is: ",int(t))
elif(value=='s'):
 print("Product is: ",int(s))
elif(value=='g'):
 print("Difference is: ",int(g))
