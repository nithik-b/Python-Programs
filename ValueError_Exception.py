# performing the ValueErrror exceptions.
try:
    # Getting input from the user.
    num=int(input("Enter a number:"))
    if num >= 0:                    # Checking the given number is greater than or equal to zero.
        print(num)
    else:                           # Else raise exception ( ValueError )
        raise ValueError("Negative number not allowed")
except ValueError as e:
    print(e)                        # Print the exception.
