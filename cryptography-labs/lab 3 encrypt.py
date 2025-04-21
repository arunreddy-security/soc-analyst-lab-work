from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(input_file, encrypted_file, key, iv):
    with open(input_file, 'r') as file:
        plaintext = file.read().encode('utf-8')

    # Ensure the plaintext is a multiple of 16 bytes (AES block size)
    while len(plaintext) % 16 != 0:
        plaintext += b' '

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(plaintext) + encryptor.finalize()

    with open(encrypted_file, 'wb') as file:
        file.write(encrypted_data)

# Generate a secure 32-byte key and 16-byte IV for AES encryption
key = os.urandom(32)  # AES-256 key
iv = os.urandom(16)   # Initialization Vector (IV)

# Save key and IV for the decryption process
with open('key_iv.txt', 'wb') as file:
    file.write(key + iv)

# Input/Output files
encrypt_file('plaintext.txt', 'encrypted.txt', key, iv)
print("Encryption complete! Encrypted data written to 'encrypted.txt'")
