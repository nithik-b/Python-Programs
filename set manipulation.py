set_A=set()

n=int(input("How many number of elements in set_A:"))

for i in range(1,n+1):

    val=int(input(f"Enter a number {i}:"))

    set_A.add(val)

print(set_A)

set_B=set()

n=int(input("How many number of elements in set_B:"))

for i in range(1,n+1):

    val=int(input(f"Enter a number {i}:"))

    set_B.add(val)

print(set_B)

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

        choice = input("Enter the number of the operation: ")

        if choice == '1':

            print("Union:", set_A | set_B)

        elif choice == '2':

            print("Intersection:", set_A & set_B)

        elif choice == '3':

            print("Difference (A - B):", set_A - set_B)

        elif choice == '4':

            print("Symmetric Difference:", set_A ^ set_B)

        elif choice == '5':

            print("Is set_a a subset of set_b?", set_A.issubset(set_B))

        elif choice == '6':

            element = int(input("Enter element to add: "))

            set_A.add(element)

            print("Updated set_a:", set_A)

        elif choice == '7':

            element = int(input("Enter element to remove: "))

            set_A.discard(element)

            print("Updated set_a:", set_A)

        elif choice == '8':

            if set_A:

                popped_element = set_A.pop()

                print(f"Popped element: {popped_element}")

                print("Updated set_A:", set_A)

            else:

                print("set_A is empty.")

        elif choice == '9':

            print("Sorted set_A:", sorted(set_A))

        elif choice == '10':

            print("Exiting the program.")

            break

        else: 

            print("Invalid choice, try again.")
