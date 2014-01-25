'''
Created on Jun 5, 2011

@author: Rhys
'''

def ispalindrome(x):
    palindrome = ''
    temp = x
    multiplier = 10
    for ctr in range(0,len(str(x))):
        lastDigit = temp%10
        temp = x/multiplier
        multiplier *= 10
        palindrome += str(lastDigit)
    if(palindrome == str(x)):
        return True
    else:
        return False

num1 = num2 = 999
product = 0
biggestPalindrome = 0
for ctr in range(num2,0,-1):
    for ctr2 in range(num1,0,-1):
        product = ctr * ctr2
        if(ispalindrome(product)):
            biggestPalindrome = max(product, biggestPalindrome)
print( str(biggestPalindrome) )