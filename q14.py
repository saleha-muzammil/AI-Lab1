def is_palindrome(s: str):
    s = s.replace(' ', '').lower()
    return s == s[::-1]


user_input = input("Enter string")
print(f"Is palindrome?", is_palindrome(user_input))
