#!/usr/bin/env python3
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
    # Ask user where to save the key
    key_input = input("Enter the path to save the encryption key (or press Enter for 'encryption.key'): ").strip()
    
    # Use default if no path provided
    if not key_input:
        key_path = 'encryption.key'
    else:
        # Expand user path (handles ~ on Unix and %USERPROFILE% on Windows)
        key_path = os.path.expanduser(key_input)
        # Normalize path separators for the current OS
        key_path = os.path.normpath(key_path)
    
    # Create directory if it doesn't exist
    key_dir = os.path.dirname(key_path)
    if key_dir and not os.path.exists(key_dir):
        try:
            os.makedirs(key_dir)
            print(f"Created directory: {key_dir}")
        except OSError as e:
            print(f"Error creating directory {key_dir}: {e}")
            return
    
    # Check if key file already exists
    if os.path.exists(key_path):
        overwrite = input(f"Key file '{key_path}' already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite not in ['y', 'yes']:
            print("Key generation cancelled.")
            return
    
    try:
        # Generate and save the encryption key
        key = generate_key()
        save_key(key, key_path)
        print(f"Encryption key generated and saved to: {os.path.abspath(key_path)}")
    except Exception as e:
        print(f"Error generating or saving key: {e}")

if __name__ == '__main__':
    main()