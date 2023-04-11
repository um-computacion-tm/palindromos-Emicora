import unittest

def palindrome(word):
    inversa = ""

    for i in range(len(word)-1,-1,-1):
        inversa += word[i] 
    
    if (inversa == word):
        return True
    else:
        return False
    
if __name__ == '__main__':
    unittest.main()
