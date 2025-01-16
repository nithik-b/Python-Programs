def email(n):
    username,domain=n.split('@')
    return username, domain
n=input("Enter an email address:")
username,domain=email(n)
print(f"Username: {username}")
print(f"Domain: {domain}")
