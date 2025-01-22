# Performing fibonacci series.
# Creating user-defined functions.
def fib(n):
  if n==0:
    return 0        # Base case.
  elif n==1:
    return 1        # Base case.
  else:
    return fib(n-1) + fib(n-2)        # Recursive case.
# Getting input from the user.
n=int(input("Enter a number:"))
# Printing the value by using the for loop.
for i in range(0,n+1):
  print("Fibonacci(",i,"):",fib(i))
