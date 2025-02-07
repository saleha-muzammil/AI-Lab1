# 1. Hello, Python!
def greet_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")

# 2. Data Type Identification
def identify_data_type():
    user_input = input("Enter something: ")
    try:
        converted = int(user_input)
        print(f"Integer: {converted}")
    except ValueError:
        try:
            converted = float(user_input)
            print(f"Float: {converted}")
        except ValueError:
            print(f"String: {user_input}")

# 3. List Operations
def list_operations():
    my_list = ["Fahad", "Taahaa", "ALi Abbas"]
    my_list.append("Subhann")
    my_list.remove("Fahad")
    print([item.upper() for item in my_list])

# 4. Tuple Unpacking
def tuple_unpacking():
    my_tuple = (55, 29, 72)
    first, second, _ = my_tuple
    print(f"First: {first}, Second: {second}")

# 5. Dictionary Management
def manage_dictionary():
    students = {"Fahad": 100, "Taaha": 85, "Ali": 88, "Subhan": 92, "Harris": 95}
    print(students)

# 6. Set Operations
def set_operations():
    set1 = set(map(int, input("Enter numbers for set1: ").split()))
    set2 = set(map(int, input("Enter numbers for set2: ").split()))
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

# 7. Conditional Statements: Number Checker
def number_checker():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
    print("Even" if num % 2 == 0 else "Odd")

# 8. FizzBuzz
def fizzbuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# 9. Factorial Calculator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 10. Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 11. List Comprehension: Squares
def squares(lst):
    return [x ** 2 for x in lst]

# 12. Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1

# 13. Remove Duplicates from a List
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# 14. Palindrome Checker
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 15. Fibonacci Sequence Generator
def fibonacci(n):
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 16. Average Calculator with Validation
def average_calculator():
    numbers = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if numbers:
        print(f"Average: {sum(numbers) / len(numbers)}")
    else:
        print("No numbers entered.")

# 17. Nested Loops: Multiplication Table
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()

# 18. User Registration System
def user_system():
    users = {}
    while True:
        action = input("Enter 'register' or 'login': ").lower()
        if action == 'register':
            username = input("Enter username: ")
            password = input("Enter password: ")
            users[username] = password
            print("User registered successfully.")
        elif action == 'login':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if users.get(username) == password:
                print("Login successful!")
            else:
                print("Invalid credentials.")
        else:
            break

# 19. Counting Elements with a Dictionary
def word_count():
    words = input("Enter words: ").split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    print(word_freq)

# 20. Temperature Converter
def convert_temperature():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C/F): ").upper()
    if unit == 'C':
        print(f"{temp}C is {(temp * 9/5) + 32}F")
    elif unit == 'F':
        print(f"{temp}F is {(temp - 32) * 5/9}C")
    else:
        print("Invalid unit")



if __name__ == "__main__":
    greet_user()
    identify_data_type()
    list_operations()
    tuple_unpacking()
    manage_dictionary()
    set_operations()
    number_checker()
    fizzbuzz()
    print(factorial(5))
    print(is_prime(7))
    print(squares([1, 2, 3, 4, 5]))
    print(merge_dictionaries({'a': 1}, {'b': 2}))
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    print(fibonacci(10))
    average_calculator()
    multiplication_table()
    user_system()
    word_count()
    convert_temperature()

