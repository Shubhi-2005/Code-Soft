#Password generator
import random
import string

# User Input
length = int(input("Enter the desired password length: "))

# Generate Password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

# Display the Password
print("Generated Password:",password)