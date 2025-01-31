#q1
# name=input("input name:")
# age=input("input age:")
# print(f"hi,{name},you are {age} yearsb old")


#q2
# user_input = input("Enter something: ")
# try:
#         user_input = int(user_input)
#         print(f"The input is an integer: {user_input}")
# except ValueError:
#         try:
#             user_input = float(user_input)
#             print(f"The input is a float: {user_input}")
#         except ValueError:
#             print(f"The input is a string: {user_input}")

#q3

# my_list = ['apple', 'banana', 'lime']
# my_list.append('orange')
# my_list.remove('apple')
# for item in my_list:
#         print(item.upper())


#q4

# my_tuple = (10, 15, 20)
# first, second = my_tuple[:2]
# print(f"First element: {first}, Seco1nd element: {second}")

#q5

# students = {
#         'Adil': 69,
#         'Babar': 90,
#         'Head': 78,
#         'Kohli': 92,
#         'Fakhar': 88
#     }
# print(students)

#q6

# l1 = list(map(int, input("Enter first list of integers: ").split()))
# l2 = list(map(int, input("Enter second list of integers: ").split()))
# s1 = set(l1)
# s2 = set(l2)
# print(f"Union: {s1.union(s2)}")
# print(f"Intersection: {s1.intersection(s2)}")
# print(f"Difference (set1 - set2): {s1.difference(s2)}")

#q7

# n= int(input("Enter an integer: "))
# if n> 0:
#         print("Positive")
# elif n < 0:
#         print("Negative")
# else:
#         print("Zero")

# if (n%2==0) :
#         print("even")

# else:
#         print("odd")

#q8
# i=int(input("enter integer between 1 and 50"))
# for n in range(1, 51):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

#q9

# number = int(input("Enter a non-negative integer: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"Factorial of {number} is {factorial}")

# #q10

# number = int(input("Enter a number: "))
# is_prime = True
# if number <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
# print(f"{number} is {'prime' if is_prime else 'not prime'}")

# #q11

# numbers = list(map(int, input("Enter a list of integers: ").split()))
# squares = [x**2 for x in numbers]
# print("Squares:", squares)

# #q12

# dict1 = {'e': 1, 'f': 2}
# dict2 = {'g': 3, 'h': 4}
# merged_dict = {**dict1, **dict2}
# print("Merged Dictionary:", merged_dict)

# #q13

# numbers = list(map(int, input("Enter a list of integers: ").split()))
# unique_numbers = []
# seen = set()
# for num in numbers:
#     if num not in seen:
#         unique_numbers.append(num)
#         seen.add(num)
# print("List without duplicates:", unique_numbers)

# #q14

# string = input("Enter a string: ")
# cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
# is_palindrome = cleaned_string == cleaned_string[::-1]
# print(f"'{string}' is {'a palindrome' if is_palindrome else 'not a palindrome'}")

# #q15
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fib_sequence = [0, 1]
# while len(fib_sequence) < n:
#     fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
# print("Fibonacci Sequence:", fib_sequence[:n])

# #q16

# numbers = []
# while True:
#     user_input = input("Enter a number (or 'done' to finish): ")
#     if user_input.lower() == 'done':
#         break
#     try:
#         numbers.append(float(user_input))
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# if numbers:
#     print(f"Average: {sum(numbers) / len(numbers)}")
# else:
#     print("No numbers entered.")

# #q17
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()

# #q18
# users = {}

# # Registration
# username = input("Enter a username: ")
# password = input("Enter a password: ")
# users[username] = password
# print("Registration successful!")

# # Login
# login_username = input("Enter your username: ")
# login_password = input("Enter your password: ")
# if login_username in users and users[login_username] == login_password:
#     print("Login successful!")
# else:
#     print("Invalid username or password.")

# #q19

# words = input("Enter a list of words: ").split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print("Word Count:", word_count)

# #q20
# choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()
# if choice == 'C':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit}°F is {celsius}°C")
# elif choice == 'F':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = celsius * 9/5 + 32
#     print(f"{celsius}°C is {fahrenheit}°F")
# else:
#     print("Invalid choice.")