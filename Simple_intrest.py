# Performing simple intrest calculation. 
p = float(input("Enter the principle amount:"))
n = float(input("Enter the time in years:"))
r = float(input("Enter the annual intrest rate(in percentage):"))/100
simp_intr=p*n*r     # Formula for simple intrest.
# Printing simple intrest on following with two floating points.
print(f"The simple intrest is {simp_intr:.2f}")
