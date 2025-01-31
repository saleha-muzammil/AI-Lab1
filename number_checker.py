def is_even(number) -> bool:
    return number % 2 == 0

def check_number(number: int) -> str:
    if number > 0:
        return f"{number} is positive"
    if number < 0:
        return f"{number} is negative"
    return f"{number} is zero"

def main():
    number = int(input("Enter number: "))
    print(check_number(number))
    print(f"{number} is {'even' if is_even(number) else 'odd'}")
    
if __name__ == "__main__":
    main()