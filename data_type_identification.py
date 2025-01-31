def main():
    user_input = input("Enter something: ")
    if user_input.isdigit():
        print("You entered a number.")
    elif user_input.isalpha():
        print("You entered a letter.")
    else:
        print("You entered a mix of letters and numbers.")


if __name__ == "__main__":
    main()