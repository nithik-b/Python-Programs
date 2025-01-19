# Importing the math module.
# Getting input from the user.
import math
n=int(input("Enter the number:"))
a=abs(n)                                 # Absolute function.
print("The absolute value is:",a)
print("The square root of the number:",math.sqrt(a))      # Square root of the number using math module.
def cube(n):                               # User-defined functions.
  return n**3
# Calling the function in the print statement.
print("The cube of a number:",cube(n))






