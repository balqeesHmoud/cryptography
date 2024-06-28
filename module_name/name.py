def encrypt(plaintext, key):
    """
    Encrypt the given plaintext using a Caesar cipher.

    The Caesar cipher shifts each character in the plaintext by a specified number of positions.
    Characters within the ASCII range 32 to 126 are shifted, wrapping around if necessary.

    Args:
        plaintext (str): The text to be encrypted.
        key (int): The number of positions to shift each character.

    Returns:
        str: The encrypted text.

    Example:
        >>> encrypt("Hello, World!", 3)
        'Khoor/#Zruog$'
    """
    def shift(char, key):
        if 32 <= ord(char) <= 126:
            new_char = 32 + (ord(char) - 32 + key) % 95
            return chr(new_char)
        return char

    ciphertext = ''.join(shift(char, key) for char in plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypt the given ciphertext using a Caesar cipher.

    The Caesar cipher shifts each character in the ciphertext back by a specified number of positions.
    Characters within the ASCII range 32 to 126 are shifted, wrapping around if necessary.

    Args:
        ciphertext (str): The text to be decrypted.
        key (int): The number of positions each character was shifted during encryption.

    Returns:
        str: The decrypted text.

    Example:
        >>> decrypt("Khoor/#Zruog$", 3)
        'Hello, World!'
    """
    def unshift(char, key):
        if 32 <= ord(char) <= 126:
            new_char = 32 + (ord(char) - 32 - key) % 95
            return chr(new_char)
        return char

    plaintext = ''.join(unshift(char, key) for char in ciphertext)
    return plaintext

# Usage example
if __name__ == "__main__":
    message = "Hello, World!"
    shift_key = 3

    encrypted_message = encrypt(message, shift_key)
    print(f"Encrypted: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift_key)
    print(f"Decrypted: {decrypted_message}")
