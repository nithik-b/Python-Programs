def num_to_roman(num):
  roman_map=[(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
  roman=""
  for value,symbol in roman_map:
    roman+=(num//value)*symbol
    num%=value
  return roman
n=int(input("Enter the number(1-3999):"))
if 1 <= n <= 3999:
    print(f"Roman numeral: {num_to_roman(n)}")
else:
    print("Please enter a valid number between 1 and 3999.")
