# Image Encryption/Decryption Tool

This is a simple Python script that encrypts and decrypts images using a pass phrase. The script reads an image from a specified directory, encrypts or decrypts it, and saves the new file in another specified directory.

## Requirements

To use this script, you will need:

- Python 3.x
- An image file to encrypt/decrypt

## Usage

1. Clone or download the repository to your local machine.
2. Open the terminal and navigate to the directory where the script is located.
3. Run the script using the command `python ImageEncryptor.py`.
4. Follow the instructions on the menu to encrypt or decrypt your image file.

## How It Works

The script uses a simple encryption algorithm that reverses a portion of the image data. The user enters a pass phrase, which is used to generate a random key that determines the portion of the image data that is reversed.

When encrypting an image, the script reads the original file, encrypts the data, and saves it to a new file. When decrypting an image, the script reads the encrypted file, decrypts the data, and saves it to a new file.

## Disclaimer

This script is intended for educational purposes only. It is not a secure encryption algorithm and should not be used to encrypt sensitive data.
