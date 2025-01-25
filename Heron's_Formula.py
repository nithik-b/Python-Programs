# Performing heron's formula for area of triangle.
# Getting input from the user.
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
# Heron's formula.
s=(a+b+c)/2
area=((s*(s-a)*(s-b)*(s-c))**(1/2))
# Printing the area.
print("The area of the triangle",area)
