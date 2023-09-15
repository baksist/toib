import hashlib
import getpass

cleartext_password = getpass.getpass("Enter your password: ")
hashed_password = hashlib.sha256(cleartext_password.encode()).hexdigest()
print(f"SHA-256 hash of your password: {hashed_password}")