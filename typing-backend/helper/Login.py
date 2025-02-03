import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()