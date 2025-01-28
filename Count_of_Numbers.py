# Performing the count of positive,negative and zero from the user. 
neg=pos=zero=0
print("Enter -1 to exit")
while(1):
  n=int(input("Enter any number:"))
  if n==-1:
    break
  elif(n==0):        
    zero=zero+1
  elif(n>0):
    pos=pos+1
  else:
    neg=neg+1              
# Printing the count of numbers.
print("Count of positive numbers entered:",pos)
print("Count of negative numbers entered:",neg)
print("Count of zeroes entered:",zero)
