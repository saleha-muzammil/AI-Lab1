def task1():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    print(f"Hello, {name}, Your age is {age} years.")

def task2():
    input_data = input("Please enter something: ")
    try:
        int_value = int(input_data)
        print(f"The input is an integer: {int_value}")
    except ValueError:
        try:
            float_value = float(input_data)
            print(f"The input is a float: {float_value}")
        except ValueError:
            print(f"The input is a string: {input_data}")

def task3():
    my_list = ["Pancakes", "Brownies", "Cookies"]
    print("----->List Initialized: ")
    for item in my_list:
        print(item)
    my_list.append("Date")
    print("----->List after adding Date: ")
    for item in my_list:
        print(item)
    my_list.remove("Cookies")
    print("----->List after removing Cookies: ")
    for item in my_list:
        print(item.upper())

def task4():
    my_tuple = ("apple", "banana", "cherry")
    first, second = my_tuple[:2]
    print(f"First element: {first}")
    print(f"Second element: {second}")

def task5():
    students_grades = {
        "Ali": 85,
        "Taaha": 92,
        "Fahad": 78,
        "Talal": 70,
        "Saleha": 00
    }
    print("Student Grades List is as follows:")
    for student, grade in students_grades.items():
        print(f"{student}: {grade}")

def task6():
    list1 = input("Enter integers for the first list separated by space: ").split()
    list2 = input("Enter integers for the second list separated by space: ").split()
    list1 = [int(x) for x in list1]
    list2 = [int(x) for x in list2]
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    print(f"Union: {union_set}")
    print(f"Intersection: {intersection_set}")
    print(f"Difference (set1 - set2): {difference_set1}")
    print(f"Difference (set2 - set1): {difference_set2}")

def task7():
    number = int(input("Please enter an integer: "))
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

def task8():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def task9():
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    while True:
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers. Please enter a non-negative integer.")
        else:
            break
    print(f"The factorial of {num} is {factorial(num)}.")

def task10():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = int(input("Enter a number to check if it is prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

def task11():
    def square_list(numbers):
        return [x**2 for x in numbers]
    numbers = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
    print(f"Squares of the list: {square_list(numbers)}")

def task12():
    def merge_dicts(dict1, dict2):
        merged = dict1.copy()
        merged.update(dict2)
        return merged
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(f"Merged dictionary: {merge_dicts(dict1, dict2)}")

def task13():
    def remove_duplicates(listt):
        set_rmdup = set()
        result = []
        for item in listt:
            if item not in set_rmdup:
                set_rmdup.add(item)
                result.append(item)
        return result
    listt = list(map(int, input("Enter a list of integers separated by space: ").split()))
    print(f"List after removing duplicates: {remove_duplicates(listt)}")

def task14():
    def is_palindrome(s):
        s = ''.join(s.split()).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

def task15():
    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(f"First {n} numbers in the Fibonacci sequence: {fibonacci(n)}")

def task16():
    def calculate_average():
        numbers = []
        while True:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            try:
                numbers.append(float(num))
            except ValueError:
                print("Invalid input. Please enter a number.")
        if numbers:
            return sum(numbers) / len(numbers)
        else:
            return 0
    print(f"The average is: {calculate_average()}")

def task17():
    print("Multiplication Table:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end=" ")
        print()

def task18():
    def register_user(users):
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists.")
        else:
            password = input("Enter a password: ")
            users[username] = password
            print("User registered successfully.")
    def login_user(users):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if users.get(username) == password:
            print("Login successful.")
        else:
            print("Invalid username or password.")
    users = {}
    while True:
        choice = input("Do you want to register or login? (register/login/exit): ").lower()
        if choice == 'register':
            register_user(users)
        elif choice == 'login':
            login_user(users)
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please choose 'register', 'login', or 'exit'.")

def task19():
    words = input("Enter a list of words separated by space: ").split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print("Word frequency:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

def task20():
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    choice = input("Convert temperature from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").upper()
    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nChoose a task to run (1-20) or 0 to exit:")
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            task1()
        elif choice == 2:
            task2()
        elif choice == 3:
            task3()
        elif choice == 4:
            task4()
        elif choice == 5:
            task5()
        elif choice == 6:
            task6()
        elif choice == 7:
            task7()
        elif choice == 8:
            task8()
        elif choice == 9:
            task9()
        elif choice == 10:
            task10()
        elif choice == 11:
            task11()
        elif choice == 12:
            task12()
        elif choice == 13:
            task13()
        elif choice == 14:
            task14()
        elif choice == 15:
            task15()
        elif choice == 16:
            task16()
        elif choice == 17:
            task17()
        elif choice == 18:
            task18()
        elif choice == 19:
            task19()
        elif choice == 20:
            task20()
        else:
            print("Invalid choice. Please choose a number between 0 and 20.")

if __name__ == "__main__":
    main()