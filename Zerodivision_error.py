num = int(input("Enter the numerator:"))    # Getting numberator from the user
deno = int(input("Enter the denominator:"))  #Getting denominator from the user\
try:                             # Try block
    quo = num/deno               # Finding Quotient 
    print("QUOTIENT",quo)
expect ZeroDivisionError:          # Except block executes when it throw the expection
    print("Denominator cannot be zero")
