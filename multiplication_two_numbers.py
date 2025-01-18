# Multiplication of two numbers using user-defined functions.
# Getting inputs from ther user.
a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
# Creating the user-defined functions.
def mul(a,b):
    return a*b
# Calling the function inside the print statement
print("The product of two numbers is",mul(a,b))
