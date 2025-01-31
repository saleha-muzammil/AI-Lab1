def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1
    
    while(start < end):
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def main():
    user_input = input("Enter a string: ")  
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")

if __name__ == "__main__":
    main()