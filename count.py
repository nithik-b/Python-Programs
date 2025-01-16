file_path="coun.txt"
line_count=0
word_count=0
char_count=0
with open("coun.txt","r")as file:
    for line in file:
        line_count+= 1
        word_count+= len(line.split())
        char_count+= len(line)
print(f"Number of lines:{line_count}")
print(f"Number of words:{word_count}")
print(f"Number of characters:{char_count}")
