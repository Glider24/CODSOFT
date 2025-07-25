import random
import string

print("Password Generator")
print("------------------")

while True:
    length = input("Enter password length (0 to exit): ")
    if not length.isdigit():
        print("Please enter a number.")
        continue

    length = int(length)

    if length == 0:
        print("Goodbye!")
        break
    elif length < 4:
        print("Please choose a length of at least 4.")
        continue

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated password:", password)
