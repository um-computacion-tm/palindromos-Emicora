import unittest

from palindrome import palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)
    def test_palindrome_simple2(self):
        result = palindrome('agita falsos usos la fatiga')
        self.assertEqual(result, True)
    def test_palindrome_simple3(self):
        result = palindrome('hola como omoc aloh')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()