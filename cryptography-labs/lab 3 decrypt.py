from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_file(encrypted_file, output_file, key, iv):
    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove any trailing spaces added during encryption
    decrypted_data = decrypted_data.rstrip(b' ')

    with open(output_file, 'w') as file:
        file.write(decrypted_data.decode('utf-8'))

# Read the saved key and IV from file
with open('key_iv.txt', 'rb') as file:
    key_iv = file.read()
    key = key_iv[:32]  # First 32 bytes are the AES key
    iv = key_iv[32:]   # Last 16 bytes are the IV

# Decrypt the file
decrypt_file('encrypted.txt', 'decrypted.txt', key, iv)
print("Decryption complete! Decrypted data written to 'decrypted.txt'")
