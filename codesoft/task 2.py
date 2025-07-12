#password generator
import random
import string

# User Input: Prompt the user to specify the desired length of the password
length = int(input("Enter the desired password length: "))

# Generate Password: Use a combination of random characters to generate a password of the specified length
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

# Display the Password: Print the generated password on the screen
print("Generated Password:",password)