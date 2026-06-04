username = input("Enter your username: ")
email = input("Enter your email: ")

valid_user = username or "User"

# if valid_email:
#     print(f"Hello {valid_user}, your email is {email}")
# else:
#     print(f"Hello {valid_user}, please enter your email.")

print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please enter your email.")))