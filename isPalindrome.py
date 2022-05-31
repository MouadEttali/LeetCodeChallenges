def isPalindrome(x):
    strx = str(x)
    return strx == strx[::-1]



print(isPalindrome(121))
print(isPalindrome(10))
