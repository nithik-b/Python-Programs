# Performing the cube of numbers in dictionary.
# Getting the input from the user.
n=int(input("Enter a number:"))
# Creating the empty dictionary to store the numbers.
ch={}
i=1
for i in range(1,n+1):
  a=i**3    
  ch[i]=a    # Assign numbers to the value(Cube).
print(ch)
