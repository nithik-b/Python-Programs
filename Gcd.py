def gcd(x,y):
  rem=x%y
  if(rem==0):
    return y
  else:
    return gcd(y,rem)
n=int(input("Enter the number1:"))
m=int(input("Enter the number2:"))
print("The gcd is",gcd(n,m))
