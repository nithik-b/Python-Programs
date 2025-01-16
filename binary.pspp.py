def binary(a,b):
    low=0
    high=n-1
    while(low<=high):
        mid=(high+low)//2
        if a[mid]==b:
            return mid
        elif a[mid]>b:
            high=mid-1
        else:
            low=mid+1

n=int(input("Enter how many numbers in list:"))
a=[]
for i in range(1,n+1):
    b=int(input(f"Enter the number {i}:"))
    a.append(b)
    a.sort()
print(a)
c=int(input("Enter a number to be found:"))
print("The value",b,"is found at index",binary(a,b))
