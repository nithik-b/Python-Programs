n=int(input("How many numbers to be entered in list:"))
a=[ ]
for i in range(1,n+1):
    b=int(input(f"Enter a number {i}:"))
    a.append(b)
print("unsorted list:",a)
def insertion(b,n):
     for i in range(1,len(a)):
         key=a[i]
         for j in range(i,0,-1):
            if a[j-1]>key:
                a[j]=a[j-1]
            else:
                a[j]=key
                break
insertion(n,a)        
print("sorted array:",a) 
