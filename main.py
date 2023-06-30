import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired length of the password: "))
random_password = generate_random_password(password_length)
print("Randomly generated password:", random_password)
