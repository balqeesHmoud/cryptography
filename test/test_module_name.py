import unittest
from module_name.name import encrypt, decrypt

class TestCryptography(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt('abc', 1), 'bcd')

    def test_encrypt_with_wraparound(self):
        self.assertEqual(encrypt('xyz', 1), 'yza')

    def test_encrypt_with_non_ascii(self):
        self.assertEqual(encrypt('Hello, World!', 3), 'Khoor/#Zruog$')

    def test_decrypt_basic(self):
        self.assertEqual(decrypt('bcd', 1), 'abc')

    def test_decrypt_with_wraparound(self):
        self.assertEqual(decrypt('yza', 1), 'xyz')

    def test_decrypt_with_non_ascii(self):
        self.assertEqual(decrypt('Khoor/#Zruog$', 3), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
