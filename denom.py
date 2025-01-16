try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Invalid age! You must be at least 18 years old to vote.")
    print("You are eligible to vote!")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Thank you for using the voter eligibility checker.")
