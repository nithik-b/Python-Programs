import sys
numbers = [int(arg) for arg in sys.argv[1:]]
max_num =numbers[0]
for num in numbers:
    if num > max_num:
        max_num=num
print("The maximum number in the list:",max_num)        
