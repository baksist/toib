import random
import string

def generator(length = 8):
    alphabet = string.ascii_letters + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

try:
    length = int(input("Enter password length or leave blank for default: "))
    password = generator(length)
except ValueError:
    password = generator()

print(f"Your password is: {password}")
