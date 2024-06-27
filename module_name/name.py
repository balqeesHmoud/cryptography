def encrypt(plaintext, key):
    """
    Encrypts the given plaintext using a Caesar cipher.

    Args:
        plaintext (str): The string to be encrypted.
        key (int): The number of positions to shift each character.

    Returns:
        str: The resulting ciphertext after encryption.
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
    Decrypts the given ciphertext using a Caesar cipher.

    Args:
        ciphertext (str): The string to be decrypted.
        key (int): The number of positions each character was shifted during encryption.

    Returns:
        str: The resulting plaintext after decryption.
    """
    def unshift(char, key):
        if 32 <= ord(char) <= 126:
            new_char = 32 + (ord(char) - 32 - key) % 95
            return chr(new_char)
        return char

    plaintext = ''.join(unshift(char, key) for char in ciphertext)
    return plaintext
