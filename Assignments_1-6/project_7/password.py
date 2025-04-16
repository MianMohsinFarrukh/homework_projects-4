import random
import string

def generate_password(length):
    """Generate a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        #  user inputs
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password (maximum 10): "))

        # Validate inputs
        if num_passwords < 1 or length < 1:
            print("Please enter positive numbers for both inputs.")
            return
        if length > 10:
            print("Error: Password length cannot exceed 10.")
            return

        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"Password {i + 1}: {generate_password(length)}")

    except ValueError:
        print("Please enter valid numbers.")

# Run the password generator
password_generator()
