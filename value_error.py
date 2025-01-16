try:
    num=int(input("Enter a number:"))
    if num >= 0:
        print(num)
    else:
        raise ValueError("Negative number not allowed")
except ValueError as e:
    print(e)
