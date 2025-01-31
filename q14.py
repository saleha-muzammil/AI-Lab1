is_palindrome = lambda s: ''.join(e for e in s if e.isalnum()).lower() == ''.join(e for e in s if e.isalnum()).lower()[::-1]


string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")