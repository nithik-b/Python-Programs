# Performing sum og digits.
# Getting the input from the user.
n=int(input("Enter a number:"))
Sum=0
# By using thw while loop we get the desired output.
while(n!=0):
  d=n%10
  Sum= Sum+d
  n=n//10
# Printing the value of sum.
print("The sum of the digits is",Sum)
