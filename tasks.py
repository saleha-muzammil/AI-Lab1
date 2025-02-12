# #Task 1
# name = input("What is your name? ")

# age = input("How old are you? ")

# print(f"Hello, {name}! You are {age} years old. Nice to meet you!")

# #Task 2
# def determine_type(user_input):
#     try:
#         value = int(user_input)
#         return value, "int"
#     except ValueError:
#         try:
#             value = float(user_input)
#             return value, "float"
#         except ValueError:
#             return user_input, "str"
# def main():
#     user_input = input("Enter a value: ")

#     value, data_type = determine_type(user_input)

#     print(f"Original input: {user_input}")
#     print(f"Converted value: {value}")
#     print(f"Data type: {data_type}")

# if __name__ == "__main__":
#     main()

# #Task 3
# def main():
#     my_list = ["apple", "banana", "cherry"]
#     print("Initial list:", my_list)

#     my_list.append("date")
#     print("After adding 'date':", my_list)

#     my_list.remove("banana")
#     print("After removing 'banana':", my_list)

#     print("Elements in uppercase:")
#     for item in my_list:
#         print(item.upper())

# if __name__ == "__main__":
#     main()

# #Task 4
# my_tuple = (10, 20, 30, 40, 50)

# first_element = my_tuple[0]  
# second_element = my_tuple[1] 

# print("First element:", first_element)
# print("Second element:", second_element)


# #Task 5
# student_grades = {
#     "Alice": 85,
#     "Bob": 90,
#     "Charlie": 78,
#     "Diana": 92,
#     "Eve": 88
# }

# print("Student Grades:")5
# print(student_grades)

# #Task 6
# list1 = input("Enter the first list of integers (separated by spaces): ").split()
# list1 = [int(num) for num in list1]  

# list2 = input("Enter the second list of integers (separated by spaces): ").split()
# list2 = [int(num) for num in list2] 

# set1 = set(list1)
# set2 = set(list2)

# union = set1 | set2  
# intersection = set1 & set2  
# difference = set1 - set2  

# print("Union:", union)
# print("Intersection:", intersection)
# print("Difference (set1 - set2):", difference)

# #Task7
# num = int(input("Enter an integer: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# #Task 8
# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# #Task 9
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Example usage
# num = int(input("Enter a non-negative integer: "))
# print(f"The factorial of {num} is {factorial(num)}")

# #Task 10
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# #Task 11
# def square_numbers(numbers):
#     return [num**2 for num in numbers]

# # Example usage
# input_list = [1, 2, 3, 4, 5]
# squared_list = square_numbers(input_list)
# print("Original list:", input_list)
# print("Squared list:", squared_list)

# #Task 12
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# dict1.update(dict2)
# print(dict1)

# #Task 13
# def remove_duplicates_preserve_order(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# input_list = [3, 5, 2, 3, 8, 5, 1, 2]
# output_list = remove_duplicates_preserve_order(input_list)
# print(output_list)

# #Task 14
# def is_palindrome(s):
#     cleaned_string = s.replace(" ", "").lower()
#     return cleaned_string == cleaned_string[::-1] 
# print(is_palindrome("racecar"))                    
# print(is_palindrome("hello"))                         

# #Task 15
# def generate_fibonacci(n):
#     fibonacci_sequence = [0, 1]
    
#     for i in range(2, n):
#         next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_number)
    
#     return fibonacci_sequence[:n]

# n = int(input("Enter how many Fibonacci numbers you want to generate: "))

# fibonacci_numbers = generate_fibonacci(n)
# print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

# #Task 16
# def get_valid_numbers():
#     numbers = []
#     while True:
#         user_input = input("Enter a number (or 'done' to finish): ")
#         if user_input.lower() == 'done':
#             break
#         try:
#             number = float(user_input)  
#             numbers.append(number)
#         except ValueError:
#             print("Invalid input! Please enter a valid number.")
#     return numbers

# def calculate_average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)

# print("Welcome to the Average Calculator!")
# numbers = get_valid_numbers()

# if numbers:
#     average = calculate_average(numbers)
#     print(f"The average of the numbers is: {average}")
# else:
#     print("No valid numbers were entered.")

# #Task 17
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}", end="\t")
#     print()

# #Task 18
# user_credentials = {}

# def register():
#     print("--- Registration ---")
#     username = input("Choose a username: ")
#     if username in user_credentials:
#         print("Username already exists! Please choose a different one.")
#         return
#     password = input("Choose a password: ")
#     user_credentials[username] = password
#     print("Registration successful!")

# def login():
#     print("--- Login ---")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username in user_credentials and user_credentials[username] == password:
#         print("Login successful! Welcome,", username)
#     else:
#         print("Invalid username or password. Please try again.")

# def main():
#     while True:
#         print("\n1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option (1/2/3): ")
#         if choice == "1":
#             register()
#         elif choice == "2":
#             login()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

# #Task 19
# def count_word_frequency(words):
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency

# def main():
#     user_input = input("Enter a list of words separated by spaces: ")
#     words = user_input.split()  

#     word_frequency = count_word_frequency(words)

#     print("\nWord Frequency:")
#     for word, count in word_frequency.items():
#         print(f"{word}: {count}")

# if __name__ == "__main__":
#     main()

# #Task 20
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def temperature_converter():
#     print("Temperature Converter")
#     print("1. Celsius to Fahrenheit")
#     print("2. Fahrenheit to Celsius")
#     choice = input("Choose an option (1 or 2): ")

#     if choice == "1":
#         celsius = float(input("Enter temperature in Celsius: "))
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(f"{celsius}°C is {fahrenheit:.2f}°F")
#     elif choice == "2":
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         celsius = fahrenheit_to_celsius(fahrenheit)
#         print(f"{fahrenheit}°F is {celsius:.2f}°C")
#     else:
#         print("Invalid choice. Please try again.")

# temperature_converter()
