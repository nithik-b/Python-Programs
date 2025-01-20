# Performing matrix addition.
# Getting no of rows and cols from the user.
a=int(input("Enter number of rows:"))
b=int(input("Enter number of columns:"))
x=[]
# Getting elements of first matrix.
print("Enter the elements of first matrix:")
for i in range(a):
  x.append([int(input("Enter a element:")) for j in range(b)])
print("The first matrix",x)
y=[]
# Getting elements of second matrix.
print("Enter the elements of second matrix:")
for i in range(a):
  y.append([int(input("Enter a element:")) for j in range(b)])
print("The second matrix",y)
res=[[0,0],[0,0]]
# By using for loop performing matrix addition.
for i in range(len(x)):
  for j in range(len(x[0])):
    res[i][j]=x[i][j]+y[i][j]
# Printing the resultant matrix.
for r in res:
  print(r)
