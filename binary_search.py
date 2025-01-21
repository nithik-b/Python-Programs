#Performing binary search,
#Creating user-defined function (binary(a,b)),
def binary(a,b):
    low=0
    high=n-1
    # Check base case,
    while(low<=high):
        mid=(high+low)//2
        # If element is present at the middle itself,
        if a[mid]==b:
            return mid
        # If element is smaller than mid, then it can only be present in left subarray.
        elif a[mid]>b:
            high=mid-1
        # Else the element can only be present in right subarray,
        else:
            low=mid+1
    # Element is not present in the array,
    else:
        return -1
            
# Getting list of numbers from the user,
n=int(input("Enter how many numbers in list:"))        
a=[]
for i in range(1,n+1):
    b=int(input(f"Enter the number {i}:"))
    a.append(b)
    a.sort()
print(a)
# Getting the key value from the user.
c=int(input("Enter a number to be found:"))
# Founding the element by calling the function.
d=binary(a,c)
if d==-1:
    print("The element not found")
else:    
    print(f"The value {c} is found at index {d}")
