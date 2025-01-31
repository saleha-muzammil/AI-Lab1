def is_palindrome(s):
  
    normalized_str = ''.join(s.split()).lower()
   
    return normalized_str == normalized_str[::-1]



test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "Hello World",
    "No lemon, no melon"
]


for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")