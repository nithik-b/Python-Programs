"""import math
n=int(input("Enter the number:"))
a=abs(n)
print("The absolute value is:",a)
print("The square root of the number:",math.sqrt(a))
def cube(n):
  return n**3
print("The cube of a number:",cube(n))

file_name = input("Enter a file name:")
line_count= 0
word_count= 0
char_count= 0
with open(file_name,"r") as file:
  for line in file:
    line_count+=1
    word_count+=len(line.split())
    char_count+=len(line)
print(f"Number of lines:{line_count}")
print(f"Number of words:{word_count}")
print(f"Number of character:{char_count}")

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
output_file = "new2.txt"
f1 = open(file1, 'r')
f2 = open(file2, 'r')
with open(output_file, 'w') as f3:
    f3.write(f1.read() + f2.read())
print("Files concatenated to",output_file)

file_name = input("Enter the file name: ")
with open(file_name, 'r') as file:
    content = file.read()
    print("Split content:", content.split(','))

input_file = input("Enter input file name: ")
output_file = "new2.txt"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    while chunk := infile.read(50):
        outfile.write(chunk)

print("File copied to", output_file)

number = int(input("Enter a number: "))
print(f"Octal: {oct(number)}, Hexadecimal: {hex(number)}")"""

f1= input("Enter the input file name: ")
f2 = "new1.txt"

with open(f1, 'r') as infile:
    content = infile.read()

with open(f2, 'w') as outfile:
    outfile.write(content[::-1])

print("Reversed content written to", f2)





