conversion=(
    ("meter","kilometer", 0.001),
    ("kilometer","meter", 1000),
    ("centimeter","meter",0.01),
    ("meter","centimeter", 100),
    ("centimeter","kilometer", 0.00001),
    ("kilometer","centimeter",100000),
    )
def con(val,fr,to):
    for i in conversion:
        if i[0] == fr and i[1] == to:
            return val*i[2]
        if fr==to:
            return val
val=float(input("Enter the value to convert:"))
fr=input("Enter the unit to convert from(meter,centimeter,kilometer):")
to=input("Enter the unit to convert to(meter,centimeter,kilometer):")
res=con(val,fr,to)
print(f"{val} {fr} is equal to {res} {to}")
