

1

# name = input("Enter your name  ")
# age = int(input("Enter your age "))
# print(f"Hello {name}. your age is {age}")
#
# # --------------------------------------------------------
#
2
# number = input("Enter your number ")
#
# if number.isnumeric():
#     print(f"you have entered a integer number ")

# -----------------------------------------------------------
3
# elements = ["Talal", "Umair", "Talha"]
# for element in elements:
#     print(element)
# elements.append("Taaha")
# print()
# elements.remove("Talha")
# for element in elements:
#     print(element.upper())

# ------------------------------------------------------
#
4
# my_list = (12, 15, 167)
# (a, b) = my_list[:2]
# print(a, b)

# --------------------------------------

#
5
# students = {
#     "Talal": "A",
#     "Umair": "B",
#     "Talha": "C"
# }
# for val in students:
#     print(val, students[val])
#-----------------
6
from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = set(parse_list(input("Enter list of integers (separated by comma): ")))
user_input_2 = set(parse_list(input("Enter list of integers (separated by comma): ")))

union = user_input_1.union(user_input_2)
print("Union", union)

intersection = user_input_1.intersection(user_input_2)
print("Intersection", intersection)

difference = user_input_1.difference(user_input_2)
print("Difference", difference)



# ----------------------------------------
#
7
# num = int(input("Enter a number"))
# if num == 0:
#     print("your number is zero ")
# elif num > 0:
#     print("{num} is Positive number")
# elif num < 0:
#     print("{num} is negative number")
#
# if num % 2 == 0:
#     print("number is even ")
# else:
#     print("number is odd")
# ---------------------------------------------
#
8
# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# -----------------------------------------------

9
#
# def factorial(num):
#     if num < 2:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# number = int(input("Enter a positive number "))
# num = factorial(number)
# print(num)
#--------------------
10
# user_input = input("Enter integer: ")
#
#
# def is_num(s):
#     if s.startswith('-'):
#         s = s[1:]
#     return s.isdigit()
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#
#     for i in range(2, int(num / 2) + 1):
#         if num % i == 0:
#             return False
#
#     return True
#
#
# if not is_num(user_input):
#     print("Enter integer")
#     exit(1)
# else:
#     user_input = int(user_input)
#     print("Is prime?", is_prime(user_input))
#

# ------------------------------------------------------
#
11
# my_list = [10, 12, 14, 15]
# new_list = [i ** 2 for i in my_list]
# # () = TUPLE
# # [] = LIST
# # {} = DICTIONARY
#
# print(new_list)
# -----------------------------------------------------------
#
12
# students_A = {
#     "Talal": "A",
#     "Umair": "B",
#     "Talha": "C"
# }
# students_B = {
#     "Taaha": "D",
#     "Umair": "F"
# }
#
# students_A.update(students_B)
#
# print(students_A)
#

# ---------------------------------------------------------
#
13
# items = [1, 2, 0, 1, 3, 2]
# newlist = []
#
# for num in items:
#     if num not in newlist:
#         newlist.append(num)
#
# print(newlist)
# -----------------------------------------------------------------
#
14
# def isPalindrome(str):
#     # Run loop from 0 to len/2
#     for i in range(0, int(len(str) / 2)):
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     return True
#
#
# str = "hooooook"
# result = isPalindrome(str)
#
# if (result):
#     print("Yes")
# else:
#     print("No")


# ------------------------------------------------------------------
#
15
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibo(n - 1) + fibo(n - 2))
#
#
# num= int(input("Enter your number"))
#
# # check if the number of terms is valid
# if num <= 0:
#     print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     print(fibo(num))
#

#-----------------------------
16
from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = parse_list(input("Enter list of integers (separated by comma): "))


print(f"Average {sum(user_input_1) / len(user_input_1)}")
# # __________________________________
17
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

#----------------------------------------------
18
#
# users = {}
#
#
# def register():
#     user = input("Enter username: ")
#     pass_ = input("Enter password: ")
#     users[user] = pass_
#
#
# def login():
#     user = input("Enter username: ")
#     pass_ = input("Enter password: ")
#     print("Login done"
#           if users.get(user) == pass_
#           else "Login not done")
#
#
# print("Register:")
# register()
#
# print("Login:")
# login()
#-----------------------------------------------------
19
user_input = input("Enter input")
words = user_input.lower().split(" ")

d = dict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)

#------------------------------------------
20
def convert_temp():
    user_input = float(input("Enter int: "))
    unit = input("C or F: ").upper()
    print(user_input * 9 / 5 + 32 if unit == 'F' else (user_input - 32) * 5 / 9)


convert_temp()

#-----------------------------------------------------------------
