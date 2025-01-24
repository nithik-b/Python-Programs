# Getting input from the user.
n = int(input("Enter the number:"))
Sum=0
temp=n  # Assign temp as n
# Check if the number is armstrong using while loop.
while(temp>0):
  d=temp%10
  Sum=Sum+d**3
  temp=temp//10
# Checking if n is equal to sum.
if (n==Sum):
  print(n,"is armstrong number")
else:
  print(n,"is not an armstrong number")
