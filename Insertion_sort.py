# Performing insertion sort.
# Getting list of numbers from the user.
n=int(input("How many numbers to be entered in list:"))
a=[ ]
for i in range(1,n+1):
    b=int(input(f"Enter a number {i}:"))
    a.append(b)
print("unsorted list:",a)
# Creating the user-defined functions
def insertion(b,n):
     # Iterate over the array starting from the second element.
     for i in range(1,len(a)):
         # Store the current element as the key to be inserted in the right position.
         key=a[i]
         for j in range(i,0,-1):
            if a[j-1]>key:
                a[j]=a[j-1]
            else:
                a[j]=key
                break
# Calling the function
insertion(n,a)        
print("sorted array:",a) 
