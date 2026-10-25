#30.Student Email and Identifier Validation.
email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
