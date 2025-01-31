#Write a program that asks the user for their name and age, then prints a greeting message.
def helloPython():
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    print(f"Welcome {name} with age {age}")



#Create a program that takes user input and determines its data type, handling conversions to int or float when possible.
def dataTypeIdentification():
    user_input = input("Please enter something: ")
    try:
        int_value = int(user_input)
        print(f"The input is of type 'int': {int_value}")
    except ValueError:
        try:
            float_value = float(user_input)
            print(f"The input is of type 'float': {float_value}")
        except ValueError:
            print(f"The original input is a string: '{user_input}'")



#Initialize a list with specific elements, modify it by adding and removing items, and print each element in uppercase.
def listOperations():
    fruits=["apple","kewi","mango"]
    print("Original fruits: ",fruits)
    fruits.append("grape")
    fruits.remove("kewi")
    print("Modified fruits in upperCase: ")
    for fruit in fruits:
        print(fruit.upper())

#Unpack the first two elements of a given tuple into separate variables and print them.
def tupleUnpacking():
    my_tuple = (1, 2, 3, 4, 5)
    first_element, second_element = my_tuple[0], my_tuple[1]
    print("First element:", first_element)
    print("Second element:", second_element)



#Create a program to store five student names and their grades in a dictionary and then print the dictionary.
def dictionaryManagement():
    student_grades = {}
    for i in range(5):
        name = input(f"Enter the name of student {i + 1}: ")
        grade = input(f"Enter the grade of {name}: ")
        student_grades[name] = grade

    print("\nStudent Grades:")
    print(f"{student_grades}")

#Take two lists of integers from the user, convert them to sets, and display their union, intersection, and difference.
def setOperations():
    list1 = input("Enter integers for the first list separated by space: ").split()
    list2 = input("Enter integers for the second list separated by space: ").split()

    list1 = [int(x) for x in list1]
    list2 = [int(x) for x in list2]

    # remove duplicates by converting to set
    set1 = set(list1)
    set2 = set(list2)

    # Union:---->simply add all elements of set 1 and than add only those elements from set2 which are not in union set already
    union_set = set1.copy()
    for item in set2:
        if item not in union_set:
            union_set.add(item)
    print(f"Union: {union_set}")

    # Intersection:---->add an item if present in both sets
    intersection_set = set()
    for item in set1:
        if item in set2:
            intersection_set.add(item)
    print(f"Intersection: {intersection_set}")

    # Difference (set1 - set2) : Remove same elements
    difference_set1 = set1.copy()
    for item in set2:
        if item in difference_set1:
            difference_set1.remove(item)
    print(f"Difference (set1 - set2): {difference_set1}")

    # Difference (set2 - set1): Removing elements of set2 present in set1
    difference_set2 = set2.copy()
    for item in set1:
        if item in difference_set2:
            difference_set2.remove(item)
    print(f"Difference (set2 - set1): {difference_set2}")


#Program to determine if an integer is positive, negative, or zero, and even or odd
def numberChecker():
    user_input = input("Please enter an integer: ")

    try:
        number = int(user_input)
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with "Buzz", and multiples of both with "FizzBuzz".
def fizz_buzz():
    for number in range(1, 51):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

#Define a function to calculate the factorial of a non-negative integer using a loop.
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def mainForFactorial():
    while True:
        try:
            user_input = int(input("Please enter a non-negative integer: "))
            if user_input >= 0:
                result = calculate_factorial(user_input)
                print(f"The factorial of {user_input} is {result}.")
                break  # Exit the loop after successful calculation
            else:
                print("The number must be non-negative. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Create a function to check if a number is prime and use it to verify a user-entered number.
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it's prime

def mainForPrime():
    while True:
        try:
            user_input = int(input("Please enter a positive integer: "))
            if user_input > 0:
                if is_prime(user_input):
                    print(f"{user_input} is a prime number.")
                else:
                    print(f"{user_input} is not a prime number.")
                break  # Exit the loop after successful verification
            else:
                print("The number must be positive. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Write a function that takes a list of integers and returns a new list with the squares of each number using list comprehension
def square_numbers(numbers):
    # Using list comprehension to create a new list with squares
    return [x ** 2 for x in numbers]
def mainForSquares():
    input_numbers = [1, 2, 3, 4, 5]
    squared_numbers = square_numbers(input_numbers)
    print("Original numbers:", input_numbers)
    print("Squared numbers:", squared_numbers)

# Merge two dictionaries into one, with the second dictionary's values overwriting the first's in case of duplicate keys.

# Write a function that removes duplicates from a list of integers while preserving the original order.
def remove_duplicates(original_list):
    unique_list = []
    seen = set() # Create a set to track seen elements
    
    for number in original_list:
        # Check if the number has already been seen
        if number not in seen:
            # If not, add it to both the unique list and the seen set
            unique_list.append(number)
            seen.add(number)
    
    return unique_list

# Example usage of the function
def mainForDuplicatesRemover():
    # Sample list with duplicates
    input_list = [1, 2, 3, 2, 4, 1, 5, 3]
    
    # Call the function to remove duplicates
    result = remove_duplicates(input_list)
    
    # Print the original and the result lists
    print("Original list:", input_list)
    print("List after removing duplicates:", result)

# Create a function to check whether a given string is a palindrome, ignoring case and spaces.
def is_palindrome(s):
    # Normalize the string: remove spaces and convert to lowercase
    normalized_str = ''.join(s.split()).lower()
    return normalized_str == normalized_str[::-1]

def mainForPalindrome():
    test_strings = [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw?",
        "No lemon, no melon",
        "Hello, World!",
        "Racecar"
    ]
    
    for test in test_strings:
        result = is_palindrome(test)
        print(f'"{test}" is a palindrome: {result}')

# Write a function that generates the first n numbers in the Fibonacci sequence based on user input.
def fibonacciGenerator(n):
    fibonacci_sequence = []
    for i in range(n):
        if i == 0:
            fibonacci_sequence.append(0)  # First number
        elif i == 1:
            fibonacci_sequence.append(1)  # Second number
        else:
            next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

def mainForFibonacci():
    while True:
        try:
            user_input = int(input("Enter a positive integer to generate Fibonacci sequence: "))
            if user_input > 0:
                result = fibonacciGenerator(user_input)
                print(f"The first {user_input} numbers in the Fibonacci sequence are: {result}")
                break
            else:
                print("Please enter a positive integer.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Develop a program that takes a series of numbers from the user, validates the input, and calculates the average.
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def mainForAverage():
    numbers = []
    
    print("Enter a series of numbers to calculate the average.")
    print("Type 'done' when you are finished.")

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break

        try:
            # Attempt to convert the input to a float
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")

    average = calculate_average(numbers)
    print(f"The average of the entered numbers is: {average}")

# Generate and print a multiplication table from 1 to 10 using nested loops.
def multiplication_table():
    for i in range(1, 11):  # Loop through numbers 1 to 10
        for j in range(1, 11):  # Loop through numbers 1 to 10
            product = i * j
            print(f"{product:4}", end=" ")  # Print the product with formatting
        print()  # New line after each row
# Implement a simple registration and login system using a dictionary to store user credentials.
def loginRegistration():
    user_credentials = {}

    while True:
        print("\nWelcome to the Registration and Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ")

        if choice == '1':
            # Registration
            username = input("Enter a username: ")
            if username in user_credentials:
                print("Username already exists. Please choose a different username.")
            else:
                password = input("Enter a password: ")
                user_credentials[username] = password
                print(f"User '{username}' registered successfully!")

        elif choice == '2':
            # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in user_credentials and user_credentials[username] == password:
                print(f"Welcome back, {username}!")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Take a list of words from the user and count the frequency of each word using a dictionary.
def count_word_frequency():
    # Dictionary to store word frequencies
    word_frequency = {}

    print("Enter words one by one. Type 'done' when you are finished.")

    while True:
        word = input("Enter a word: ").strip()  # Get user input and remove leading/trailing spaces

        if word.lower() == 'done':
            break 
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print("\nWord Frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

# Create a function to convert temperatures between Celsius and Fahrenheit based on user choice.
def convert_temperature():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Please choose an option (1 or 2): ")

    if choice == '1':
        # Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    elif choice == '2':
        # Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    else:
        print("Invalid choice. Please select 1 or 2.")


# helloPython()
# dataTypeIdentification()    
# listOperations()
# tupleUnpacking()
# dictionaryManagement()
# setOperations()
# numberChecker()
# fizz_buzz()
# mainForFactorial()
# mainForPrime()
# mainForSquares()
# mainForDuplicatesRemover()
# mainForPalindrome()
# mainForFibonacci()
# mainForAverage()
# multiplication_table()
# loginRegistration()
# count_word_frequency()
# convert_temperature()
