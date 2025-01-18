# Using of local and global variable
x=10
def func():
    x=5
    print("The value of x inside function is",x)   #use of local variable
# Calling the function
func()
print("The value of x outside the function",x)    #use of global variable
    
