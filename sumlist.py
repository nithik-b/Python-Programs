def Sumelem(lst):
    Sum=0
    for a in lst:
        Sum = Sum+a
    return Sum
a=[]
n=int(input("Enter how many numbers entered in list:"))
for i in range(1,n+1):
    b=int(input(f"Enter a number {i}:"))
    a.append(b)
print("Sum of the given list:",Sumelem(a))    
    
