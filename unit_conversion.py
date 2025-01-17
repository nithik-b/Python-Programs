# Performing the unit conversion which input given by the user.
# Basic conversions which is to be assigned.
conversion=(                                  
    ("meter","kilometer", 0.001),               # Nested tuple
    ("kilometer","meter", 1000),
    ("centimeter","meter",0.01),
    ("meter","centimeter", 100),
    ("centimeter","kilometer", 0.00001),
    ("kilometer","centimeter",100000),
    )
# Creatig the function with the parameter of value, from and to 
def con(val,fr,to):
    for i in conversion:
        if i[0] == fr and i[1] == to:             # Check the condition if correct the block executes
            return val*i[2]
        if fr==to:
            return val
# Getting input from the user
val=float(input("Enter the value to convert:"))
fr=input("Enter the unit to convert from(meter,centimeter,kilometer):")
to=input("Enter the unit to convert to(meter,centimeter,kilometer):")
# Callling the function
res=con(val,fr,to)
# Printing the solutions
print(f"{val} {fr} is equal to {res} {to}")
