import unittest

def palindrome(word):
    inversa = ""
    aux = ""

    for i in range(0,len(word)):
        if word[i] != " ":
            aux += word[i] 
            print(aux)

    for i in range(len(aux)-1,-1,-1):
        if aux[i] != " ":
            inversa += aux[i] 
    
    if (inversa == aux):
        return True
    else:
        return False
    
if __name__ == '__main__':
    unittest.main()
