import sys

def is_positive_integer(number: str) -> bool:
    return number.isdigit() and int(number) > 0

def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    number = input("Enter a number: ")
    if not is_positive_integer(number):
        print("Please enter a positive integer.")
        sys.exit(1)

    print("Prime" if is_prime(int(number)) else "Not prime")
        
if __name__ == "__main__":
    main()