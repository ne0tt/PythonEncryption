import os
from cryptography.fernet import Fernet
from time import sleep
from tqdm import tqdm

# Load the encryption key from a file
def load_key(key_path):
    with open(key_path, 'rb') as key_file:
        return key_file.read()
    
def count_all_files(directory):
    total_files = 0
    for root, dirs, files in os.walk(directory):
        total_files += len(files)
    return total_files

# Encrypt a file
def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Encrypt all files in a directory (and its subdirectories)
def encrypt_directory(directory_path, fernet):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, fernet)

def main():
    target_directory = input("Enter the target directory to encrypt: ")

    if not os.path.isdir(target_directory):
        print("The provided path is not a directory")
        return
    
    key_path = 'encryption_key.key'  # Path to save the encryption key

    fileCount = count_all_files(target_directory)

    # Load the encryption key
    key = load_key(key_path)
    fernet = Fernet(key)
    
    # Encrypt the directory
    encrypt_directory(target_directory, fernet)
    
    print (str(fileCount) +  " Files Encrypted")

if __name__ == '__main__':
    main()
