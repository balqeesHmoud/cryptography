# # Cryptography

This project contains functions for encrypting and decrypting text using a simple Caesar cipher technique.

## Installation

Create a virtual environment and install dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

from module_name.name import encrypt, decrypt

# Example usage
plaintext = "Hello, World!"
key = 3

encrypted = encrypt(plaintext, key)
print("Encrypted:", encrypted)  # Output: Encrypted: Khoor/#Zruog$

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)  # Output: Decrypted: Hello, World!

