import random
import string

def generate_password(length=12):
    """Generating a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

# An example of use
password_length = 12  # You can choose any password length
print("Your new password:", generate_password(password_length))
