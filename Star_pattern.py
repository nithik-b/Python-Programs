# Performing star pattern.
# Getting input from the user.
n = int(input("Enter the number of rows: "))
# By using for loop achieving star pattern. 
for i in range(1,n+1):
  print(" "*(n-i)+"*"*(2*i-1))
