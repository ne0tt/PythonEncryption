#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
from time import sleep
from tqdm import tqdm

# Load the encryption key from a file
def load_key(key_path):
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def count_all_files(path):
    if os.path.isfile(path):
        return 1
    elif os.path.isdir(path):
        total_files = 0
        for root, dirs, files in os.walk(path):
            total_files += len(files)
        return total_files
    return 0

# Decrypt a file
def decrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Decrypt all files in a directory (and its subdirectories)
def decrypt_directory(directory_path, fernet):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, fernet)

def main():
    target_path = input("Enter the target file or directory to decrypt: ").strip()
    
    # Expand user path (handles ~ on Unix and %USERPROFILE% on Windows)
    target_path = os.path.expanduser(target_path)
    
    # Normalize path separators for the current OS
    target_path = os.path.normpath(target_path)

    if not os.path.exists(target_path):
        print("The provided path does not exist")
        return

    key_path = 'encryption.key'  # Default path to the encryption key
    
    # Check if the default key file exists, if not ask user for key path
    if not os.path.exists(key_path):
        key_input = input("Encryption key file not found. Enter the path to your encryption key file: ").strip()
        key_path = os.path.expanduser(key_input)
        key_path = os.path.normpath(key_path)
        
        if not os.path.exists(key_path):
            print("The provided key file does not exist")
            return

    fileCount = count_all_files(target_path)

    try:
        # Load the encryption key
        key = load_key(key_path)
        fernet = Fernet(key)
    except Exception as e:
        print(f"Error loading encryption key: {e}")
        return

    # Decrypt based on whether it's a file or directory
    try:
        if os.path.isfile(target_path):
            decrypt_file(target_path, fernet)
            print("1 File Decrypted")
        elif os.path.isdir(target_path):
            decrypt_directory(target_path, fernet)
            print(f"{fileCount} Files Decrypted")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == '__main__':
    main()
