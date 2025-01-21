# Finding Gcd of two numbers.
def gcd(x,y):
  rem=x%y          # Finding the remainders.
  if(rem==0):
    return y              # Base case.
  else:
    return gcd(y,rem)          # Recursive case
# Get input two numbers from the user.
n=int(input("Enter the number1:"))
m=int(input("Enter the number2:"))
# Calling the function inside the print statement.
print("The gcd is",gcd(n,m))
