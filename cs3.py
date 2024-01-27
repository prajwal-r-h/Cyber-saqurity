'''3) Write a python program to check if a password meets the following criteria:
a) At Least 8 characters long.
b) Contains at least one uppercase letter, one lowercase letter, one digit and one
special character (!,@,#,$,%,^,&).
c) If the password meets the criteria print message that says “Valid Password”. If a
doesn’t meet the criteria print a massage that says “Password does not meet
requirements.'''
import re

def validate_password(password):
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    # If all the conditions are met, the password is valid
    return True

password = input("Input your password: ")
is_valid = validate_password(password)

if is_valid:
    print("Valid Password.")
else:
    print("Password does not meet requirements.")
