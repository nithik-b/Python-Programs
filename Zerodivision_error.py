num = int(input("Enter the numerator:"))
deno = int(input("Enter the denominator:"))
try:
    quo = num/deno
    print("QUOTIENT",quo)
expect ZeroDivisionError:
    print("Denominator cannot be zero")
