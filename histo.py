f=open("file.txt",'r')
d={}
r=f.read()
r=r.split()
for i in r:
    if i not in d and i.isalpha():
        d[i]=r.count(i)
for i,j in d.items():
    print(f"{i} : {j}")
f.close()
    
