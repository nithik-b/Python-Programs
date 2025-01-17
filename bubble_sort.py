# Performing bubble sort
def bubble(n,b):
    for i in  range(n):
        for j in range(0,n-1):
            # Swap elements if they are in the wrong order
            if b[j]>b[j+1]:
                 b[j],b[j+1]=b[j+1],b[j]
# Get list of numbers from the user
b=[]
n=int(input("How many numbers to be in list:"))
for i in range(1,n+1):
    a=int(input(f"Enter a number {i}:"))
    b.append(a)
print("The list given by the user:",b)
# Calling the function
bubble(n,b)
print("The list after sorted:",b)
