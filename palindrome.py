import unittest

def palindrome(word):
    inversa = " "
    for i in range(len(word),1,-1):
        inversa += word[i] 
        
    if inversa == word:
        return True
    else:
        return False

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()