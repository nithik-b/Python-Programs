def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1) + fib(n-2)
n=int(input("Enter a number:"))
for i in range(0,n+1):
  print("Fibonacci(",i,"):",fib(i))
