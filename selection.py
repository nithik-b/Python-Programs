n=int(input("How many numbers to be entered in list:"))
a=[ ]
for i in range(1,n+1):
    b=int(input(f"Enter a number {i}:"))
    a.append(b)
print("unsorted list:",a)    
def selection(b,n):
     for i in range(n):
         min_index=i
         for j in range(i+1,n):
              if(a[j]<a[min_index]):
                  min_index=j
                  a[i],a[min_index]=a[min_index],a[i]
selection(b,n)                
print("Sorted array list:",a)
