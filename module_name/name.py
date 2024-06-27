def encrypt(plaintext, key):
    def shift(char, key):
        if 32 <= ord(char) <= 126:
            new_char = 32 + (ord(char) - 32 + key) % 95
            return chr(new_char)
        return char

    ciphertext = ''.join(shift(char, key) for char in plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    def unshift(char, key):
        if 32 <= ord(char) <= 126:
            new_char = 32 + (ord(char) - 32 - key) % 95
            return chr(new_char)
        return char

    plaintext = ''.join(unshift(char, key) for char in ciphertext)
    return plaintext
