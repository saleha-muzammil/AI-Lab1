palindrome = lambda x: x.lower().replace(" ", "")== x[::-1].lower().replace(" ", "")

str=input("Enter a string: ")
print("The string is: ",str)

if palindrome(str):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
   