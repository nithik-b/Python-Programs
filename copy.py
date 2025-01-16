import sys
f1=open(sys.argv[2],"w")
with open(sys.argv[1])as f:
    for l in f:
        f1.write(l.upper())
print("Copied")
