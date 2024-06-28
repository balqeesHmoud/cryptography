# Cryptography

This lab demonstrates how to use a Caesar cipher to encrypt and decrypt messages. A Caesar cipher is a type of substitution cipher in which each character in the plaintext is shifted by a fixed number of positions down the ASCII table.

## How It Works

1. **Encrypt Function**:
    - The `encrypt` function takes a plaintext string and a key (the number of positions to shift each character).
    - It shifts each character in the plaintext by the key value. Characters wrap around if they reach the end of the printable ASCII range.
    - For example, encrypting "Hello, World!" with a key of 3 shifts each character three positions forward in the ASCII table.

2. **Decrypt Function**:
    - The `decrypt` function takes a ciphertext string and a key (the number of positions each character was shifted during encryption).
    - It shifts each character in the ciphertext back by the key value. Characters wrap around if they reach the beginning of the printable ASCII range.
    - For example, decrypting the encrypted message with the same key restores the original plaintext.

## Usage Example

1. Define a message and a shift key.
2. Use the `encrypt` function to encode the message.
3. Use the `decrypt` function to decode the encrypted message back to the original plaintext.

This example demonstrates the simplicity and effectiveness of the Caesar cipher for basic encryption and decryption tasks.


## Installation

Create a virtual environment and install dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

from module_name.name import encrypt, decrypt
