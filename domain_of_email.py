# Seperation of domain and username in email id 
# Creating the user-defined function.
def email(n):
    username,domain=n.split('@')
    return username, domain
# Getting input from the user
n=input("Enter an email address:")
# Calling the function
username,domain=email(n)
print(f"Username: {username}")
print(f"Domain: {domain}")
