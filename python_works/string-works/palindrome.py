
def is_palindrome(word):
    
    flag=True
    
    if word !=word[::-1]:
        
        flag=False
        
    return flag

print(is_palindrome("MADAM"))

print(is_palindrome("man"))
