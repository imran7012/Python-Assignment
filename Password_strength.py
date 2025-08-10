def check_password_strength(password):
    # Check for the password should be at least 8 characters long
    if len(password) < 8:
        return False

    # Define special characters
    special_characters = "!@#$%"

    # Check all conditions using any()
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in special_characters for char in password)

    # Final decision
    if upper and lower and digit and special:
        return True
    else:
        return False

user_password = input("Enter your password to check strength: ")

if check_password_strength(user_password):
    print(" Password is strong!")
else:
    print(" Password is weak. Make sure it:")
    print("- The password should be at least 8 characters long")
    print("- Contains both uppercase and lowercase letters atleast one character for each case")
    print("- Contains atleast one digit (0-9)")
    print("- Contains a special character like !, @, #, $, %")
