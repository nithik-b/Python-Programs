# Validating voter's age
# try block
try:
    age = int(input("Enter your age: "))
    # Check the condition if age is less than 18 
    # Raise exception if the conmdition is true
    if age < 18:
        raise ValueError("Invalid age! You must be at least 18 years old to vote.")
    print("You are eligible to vote!")
# Exception block
except ValueError as e:
    print(f"Error: {e}")
# It will excecutes at last of the program.
finally:
    print("Thank you for using the voter eligibility checker.")
