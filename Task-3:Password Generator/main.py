import random
import string

def generate_password(length):
    """Generates a secure password of specified length."""
    if length < 4:
        print("Password length should be at least 4 characters for better security!")
        return
    
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    print(f"Generated Password: {password}")

try:
    length = int(input("Enter the desired password length: "))
    generate_password(length)
except ValueError:
    print("Invalid input! Please enter a number.")
