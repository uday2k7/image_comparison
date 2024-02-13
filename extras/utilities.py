import hashlib

def encrypt_password(password):
    password_bytes = password.encode('utf-16')
    hash_object = hashlib.sha256(password_bytes)
    password = hash_object.hexdigest()  

    return password