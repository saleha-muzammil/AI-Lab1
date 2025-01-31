import sys


def is_positive_integer(number):
    return number.isdigit() and int(number) > 0

def main():
    number = input("Enter a number: ")
    if not is_positive_integer(number):
        print("Please enter a positive integer.")
        sys.exit(1)
        
    number = int(number)

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")

if __name__ == "__main__":
    main()