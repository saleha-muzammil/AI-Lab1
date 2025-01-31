
is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")

print("Enter a string:")
s = str(input())

if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")