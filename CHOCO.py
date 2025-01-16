def choco(n,A):
    Sum = 0
    for i in range(n):
        Sum = Sum + A[i] * (i + 1) * (n - i)
    return Sum
n = int(input()) 
A = list(map(int,input().split()))  
print(choco(n,A))
