import os
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
def save_key(key, key_path):
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def main():
    key_path = 'encryption_key.key'  # Path to save the encryption key

    # Generate and save the encryption key
    key = generate_key()
    save_key(key, key_path)
    
if __name__ == '__main__':
    main()