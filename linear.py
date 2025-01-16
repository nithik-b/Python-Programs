def lin(c):
    for i in range(n):
        if a[i]==c:
            print(f"The value {c} is present in the index [{i}]")
            break
    else:
        print("Element not found")
a=[]
n=int(input("Enter how many numbers in list:"))
for i in range(1,n+1):
    b=int(input("Enter the number:"))
    a.append(b)
c=int(input("Enter the value to be searched:"))
lin(c)
