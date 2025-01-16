m=int(input())
n=int(input())
m1=[]
m2=[]
print("Enter elements in first mateix:")
for i in range(m):
    row=[int(input())for j in range(n)]
    m1.append(row)
print("Enter elements in second matrix:")
for j in range(m):
    row=[int(input())for j in range(n)]
    m2.append(row)
res=[[m1[i][j]+m2[i][j] for i in range(n)]for j in range(m)]
print("The resultant matrix:")
for row in res:
    print(res)
    break
