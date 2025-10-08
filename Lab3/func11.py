def is_palindrome(s):
    s = s.replace(" ", "").lower()   
    if s == s[::-1]:
        return True
    return False    

print(is_palindrome("madam"))        
print(is_palindrome("hello"))        
print(is_palindrome("A man a plan a canal Panama"))  
