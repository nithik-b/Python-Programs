n=int(input("Enter a number:"))
Sum=0
while(n!=0):
  d=n%10
  Sum= Sum+d
  n=n//10
print("The sum of the digits is",Sum)
