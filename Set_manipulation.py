set_A=set()
# Getting set_A from the user.
n=int(input("How many number of elements in set_A:"))
for i in range(1,n+1):
    val=int(input(f"Enter a number {i}:"))
    set_A.add(val)
print(set_A)
set_B=set()
# Getting  set_B from the user.
n=int(input("How many number of elements in set_B:"))
for i in range(1,n+1):
    val=int(input(f"Enter a number {i}:"))
    set_B.add(val)
print(set_B)
# Srt the while loop as true ( It will always executes).
while True:
        print("\nSelect a set operation:")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference (A - B)")
        print("4. Symmetric Difference")
        print("5. Subset Check")
        print("6. Add an element to set_A")
        print("7. Remove an element from set_A")
        print("8. Pop an element from set_A")
        print("9. Sort set_A")
        print("10. Exit")
        # Asking the user to select the options.
        choice = input("Enter the number of the operation: ")
        if choice == '1':
            print("Union:", set_A | set_B)                        # Union of two sets.
        elif choice == '2':
            print("Intersection:", set_A & set_B)                 # Instersction of two sets.
        elif choice == '3':
            print("Difference (A - B):", set_A - set_B)           # Difference of two sets.
        elif choice == '4':
            print("Symmetric Difference:", set_A ^ set_B)         # Symmetric difference of two sets.
        elif choice == '5':
            print("Is set_a a subset of set_b?", set_A.issubset(set_B))    # Check it is subset or not fot the given input
        elif choice == '6':
            element = int(input("Enter element to add: "))
            set_A.add(element)                                    # Add the element given by the user.
            print("Updated set_a:", set_A)                        # Return the updated set.
        elif choice == '7':
            element = int(input("Enter element to remove: "))
            set_A.discard(element)                                # Discard the element given by the user.
            print("Updated set_a:", set_A)                        # Return the updated set.
        elif choice == '8':
            if set_A:
                popped_element = set_A.pop()                      # popping the element.
                print(f"Popped element: {popped_element}")        # Return the popped element.
                print("Updated set_A:", set_A)                    # Print the updated set
            else:
                print("set_A is empty.")
        elif choice == '9':
            print("Sorted set_A:", sorted(set_A))                 # Sorting the given set by using sorted() Function. 
        elif choice == '10':
            print("Exiting the program.")                         # Exiting the program.
            break
        else: 
            print("Invalid choice, try again.")                   # Error message.
