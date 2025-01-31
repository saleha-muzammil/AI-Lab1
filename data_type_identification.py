def main():
    user_input = input("Enter something: ")
    if user_input.isdigit():
        if type(user_input) == float:
            print("You entered a float.")
        else:    
            print("You entered an integer.")
    elif user_input.isalpha():
        print("You entered a letter.")
    else:
        print("You entered a mix of letters and numbers.")


if __name__ == "__main__":
    main()