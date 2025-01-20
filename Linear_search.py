# Performing Linear search.
# Creating the user-defined function
def lin(c):
    for i in range(n):
        if a[i]==c:
            print(f"The value {c} is present in the index [{i}]")
            break
    else:
        print("Element not found")
# Getting list of numbers from the user.
a=[]
n=int(input("Enter how many numbers in list:"))
for i in range(1,n+1):
    b=int(input(f"Enter the number {i}:"))
    a.append(b)
print("The list:",a)
c=int(input("Enter the value to be searched:"))
# Calling the function
lin(c)
