def display_menu():
    print("\nChoose an operation:")
    print("1. Append")
    print("2. Insert")
    print("3. Sort")
    print("4. Count")
    print("5. Remove or Pop")
    print("6. Length")
    print("7. Exit")

def main(a):
    while True:
        display_menu()
        n= int(input("Enter your choice (1-7): "))
        
        if n == 1:
            book = input("Enter the book title to append: ")
            a.append(book)
            print(f"{book} has been added to the library.")
        
        elif n == 2:
            index = int(input(f"Enter the position (index) to insert the book (0 to {len(library)}): "))
            book = input("Enter the book title to insert: ")
            a.insert(index, book)
            print(f"'{book}' has been inserted at position {index}.")
        
        elif n == 3:
            a.sort()
            print("The library items have been sorted.")
        
        elif n == 4:
            book = input("Enter the book title to count: ")
            count = library.count(book)
            print(f"'{book}' appears {count} time(s) in the library.")
        
        elif n == 5:  
            s = input("Do you want to 'remove' or 'pop' a book? (remove/pop): ")
            if s.lower() == 'remove':
                book = input("Enter the book title to remove: ")
                if book in a:
                    a.remove(book)
                    print(f"'{book}' has been removed from the library.")
                else:
                    print(f"'{book}' not found in the library.")
            elif action.lower() == 'pop':
                index = int(input(f"Enter the index to pop (0 to {len(library) - 1}): "))
                if 0 <= index < len(a):
                    popped_book = a.pop(index)
                    print(f"'{popped_book}' has been popped from the library.")
                else:
                    print("Invalid index.")
        
        elif n == 6:
            print(f"The number of books in the library: {len(a)}")
        
        elif n == 7:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
        print(f"Current Library Items: {a}")
a=[]
n=int(input("Enter how many numbers in list:"))
for i in range(1,n+1):
    b=input("Enter the book name:")
    a.append(b)
main(a)
