# Performing sum of list.
# Creating user-defined functions.
def Sumelem(lst):
    Sum=0
    for a in lst:
        Sum = Sum+a
    return Sum
# Getting list of numbers from the user.
a=[]
n=int(input("Enter how many numbers entered in list:"))
for i in range(1,n+1):
    b=int(input(f"Enter a number {i}:"))
    a.append(b)
# Calling the function inside the print statement.
print("Sum of the given list:",Sumelem(a))    
    
