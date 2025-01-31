is_palindrome = lambda s: ''.join(s.lower().split()) == ''.join(s.lower().split())[::-1]

print(is_palindrome("Racecar"))                   
print(is_palindrome("Hello World"))                 