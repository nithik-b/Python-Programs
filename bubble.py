def bubble(n,b):
    for i in  range(n):
        for j in range(0,n-1):
            if b[j]>b[j+1]:
                 b[j],b[j+1]=b[j+1],b[j]
b=[]
n=int(input("How many numbers to be in list:"))
for i in range(1,n+1):
    a=int(input(f"Enter a number {i}:"))
    b.append(a)
print("The list given by the user:",b)
bubble(n,b)
print("The list after sorted:",b)
