import string
from password.new_password import generate_password

def test_password_characters():
    """Testing that only valid characters are used during generation"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Generating a long password for more secure verification
    for char in password:
        assert char in valid_characters

"""
Write another test from the suggested ones below. Alternatively, you can come up with a test of your own!
If you can write more tests, that would be really awesome!

1. Test that the password length matches the specified length
2. Test that two consecutively generated passwords are different
"""
