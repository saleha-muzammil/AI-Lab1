# q1 Write a program that asks the user for their name and age, then prints a greeting message.
def get_user_info():
    name = input("Enter your name:")
    age = input("Enter your age:")
    print("Hello", name, "!", "You are", age, "years old.")


# q2 Create a program that takes user input and determines its data type, handling conversions to int or float when possible.
def determine_data_type():
    value = input("Enter a number: ")
    try:
        if "." not in value:
            converted_value = int(value)
        else:
            converted_value = float(value)
        print(f"Converted type: {type(converted_value)}")
    except ValueError:
        print(f"Original type: {type(value)}")


# q3 Initialize a list with specific elements, modify it by adding and removing items, and print each element in uppercase.
# traversing list
def modify_list():
    items = ["a", "b", "c", "d", "e"]
    print("Traversing list:", items)
    items.append("f")
    print("After adding:", items)
    items.remove("a")
    print("After removing:", items)
    for i, n in enumerate(items):
        items[i] = items[i].upper()
    print("Uppercase list:", items)


# q4 Unpack the first two elements of a given tuple into separate variables and print them.
def unpack_tuple():
    my_tuple = ("a", "b", "c", "d", "e")
    a, b, *c = my_tuple
    print(a, b, c)


# q5 Create a program to store five student names and their grades in a dictionary and then print the dictionary.
def store_student_grades():
    students = {"John": 90, "Doe": 80, "Jane": 70, "Smith": 60, "Doe": 50}
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    for key in students:
        print(key, ":", students[key])


# q6 Take two lists of integers from the user, convert them to sets, and display their union, intersection, and difference.
def set_operations():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    set_1 = set(list_1)
    set_2 = set(list_2)
    new_set = set_1.union(set_2)
    print("union of ", set_1, " and ", set_2)
    print(new_set)
    new_set = set_1.intersection(set_2)
    print("intersection of ", set_1, " and ", set_2)
    print(new_set)
    new_set = set_1.difference(set_2)
    print("difference of ", set_1, " and ", set_2)
    print(new_set)


# q7 Ask the user to enter an integer and determine if it is positive, negative, or zero, and whether it is even or odd.
def check_number():
    number = input("Enter number: ")
    try:
        number = int(number)
        if number > 0:
            if number % 2 == 0:
                print("Positive ", " Even")
            else:
                print("Positive ", " Odd")

        elif number < 0:
            if number % 2 == 0:
                print("Neg ", " Even")
            else:
                print("Neg ", " Odd")

        else:
            print("zero")

    except:
        print("An exception occurred")


# q8  Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with "Buzz", and multiples of both with "FizzBuzz".
def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# q9 Calculate factorial
def factorial_rec(number):
    if number == 1:
        return 1
    else:
        factorial_of_number_less_1 = factorial_rec(number - 1)
        return number * factorial_of_number_less_1


def factorial():
    number_for_factorial = int(input("Enter number: "))
    print(factorial_rec(number_for_factorial))


# q10 Create a function to check if a number is prime and use it to verify a user-entered number.


def check_prime():
    number_prime = int(input("Enter number "))
    flag = 1
    for i in range(2, number_prime - 1):
        if number_prime % i == 0:
            flag = 0
            break

    if flag == 1:
        print(number_prime, "is a prime number")
    else:
        print(number_prime, "is not a prime number")


# q11 Write a function that takes a list of integers and returns a new list with the squares of each number using list comprehension.


def square_lists(list__1, list__2):
    new_list = []
    for i in range(len(list__1)):
        new_list.append(list__1[i] ** 2)
    for i in range(len(list__2)):
        new_list.append(list__2[i] ** 2)

    return new_list


def square_for_lists():

    list__1 = [1, 2, 3, 4, 5]
    list__2 = [6, 7, 8, 9, 10]
    print(square_lists(list__1, list__2))


#  q12 Merge two dictionaries into one, with the second dictionary's values overwriting the first's in case of duplicate keys
def merge_dictionaries():
    dict_1 = {"a": 1, "b": 2}
    dict_2 = {"b": 3, "c": 4}

    dict_1.update(dict_2)
    print(dict_1)


# q13Remove Duplicates from a List  Write a function that removes duplicates from a list of integers while preserving the original order.
def remove_duplicates():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    new_list = list(dict.fromkeys(numbers))
    print(new_list)
    return new_list


# q14 Palindrome Checker Create a function to check whether a given string is a palindrome, ignoring case and spaces.

is_palindrome = lambda s: (
    s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1]
)


# q15  Write a function that generates the first n numbers in the Fibonacci sequence based on user input.
def generate_fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    if n <= 0:
        return [0]  # Return the first n elements if n is 1 or 2
    elif n <= 2:
        return fib_sequence[:n]
    else:
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

        return fib_sequence


def fibonacci():
    num_term = int(input("Enter the number of Fibonacci terms to generate: "))
    fibonacci_numbers = generate_fibonacci(num_term)
    print(fibonacci_numbers)


# q16 write a function to calculate avg of numbers of user
def calculate_average():
    numbers = []
    while True:
        try:
            num_str = input("Enter a number (or 'done' to finish): ")
            if num_str.lower() == "done":
                break  # Exit the loop if the user enters 'done'
            num = float(num_str)  # Convert the input to a float
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if numbers:
        average = sum(numbers) / len(numbers)
        print("The average is:", average)
    else:
        print("No numbers were entered.")


# q17 Generate and print a multiplication table from 1 to 10 using nested loops.
def print_multiplication_table():
    for i in range(1, 11):
        print("Table of ", i)
        for j in range(1, 11):
            print(i * j)


# q18 Implement a simple registration and login system using a dictionary to store user credentials.
def register_user(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try a different one.")
        return

    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")


def login_user(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")


def Registration_System():
    users = {}

    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# q19 Counting Elements with a Dictionary Take a list of words from the user and count the frequency of each word using a dictionary.
def count_word_frequency():
    words = input("Enter a list of words separated by spaces: ")
    words = words.split(" ")
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    print("Word frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")


# q20 Create a function to convert temperatures between Celsius and Fahrenheit based on user choice.
def convert_temperature():
    choice = input(
        "Choose conversion: \n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: "
    )

    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")


def main():
    while True:
        print("\nChoose a program to run:")
        print("1. Get User Info")
        print("2. Determine Data Type")
        print("3. Modify List")
        print("4. Unpack Tuple")
        print("5. Store Student Grades")
        print("6. Set Operations")
        print("7. Check Number")
        print("8. FizzBuzz")
        print("9. Factorial")
        print("10. Check Prime")
        print("11. Square Lists")
        print("12. Merge Dictionaries")
        print("13. Remove Duplicates")
        print("14. Palindrome Checker")
        print("15. Generate Fibonacci")
        print("16. Calculate Average")
        print("17. Multiplication Table")
        print("18. Registration System")
        print("19. Word Frequency Counter")
        print("20. Convert Temperature")
        print("21. Exit")

        choice = input("Enter your choice (1-21): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            determine_data_type()
        elif choice == "3":
            modify_list()
        elif choice == "4":
            unpack_tuple()
        elif choice == "5":
            store_student_grades()
        elif choice == "6":
            set_operations()
        elif choice == "7":
            check_number()
        elif choice == "8":
            fizz_buzz()
        elif choice == "9":
            factorial()
        elif choice == "10":
            check_prime()
        elif choice == "11":
            square_for_lists()
        elif choice == "12":
            merge_dictionaries()
        elif choice == "13":
            remove_duplicates()
        elif choice == "14":
            string = input("Enter a string: ")
            print(
                "It's a palindrome!" if is_palindrome(string) else "Not a palindrome."
            )
        elif choice == "15":
            fibonacci()
        elif choice == "16":
            calculate_average()
        elif choice == "17":
            print_multiplication_table()
        elif choice == "18":
            Registration_System()
        elif choice == "19":
            count_word_frequency()
        elif choice == "20":
            convert_temperature()
        elif choice == "21":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 21.")


if __name__ == "__main__":
    main()
