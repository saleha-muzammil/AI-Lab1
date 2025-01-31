# Write a program that asks the user for their name and age, then prints a greeting
# message.

name=input("enter name")
age=input("enter age")
print(" Hello ",name," your age is : ",age)

# Create a program that takes user input and determines its data type, handling
# conversions to int or float when possible

var=input("enter string : ")
print(type(var))
num=int(input("enter a number : "))
print(type(num))
floatnum=float(input("enter float number: "))
print(type(floatnum))
variable=input("enter anything : ")
if variable.isnumeric() or variable.isdigit():
    print("num")
elif variable.isalnum() or variable.isalpha():
  print("str")

# Initialize a list with specific elements, modify it by adding and removing items, and print
# each element in uppercase.
arr=["1,2,3,4"]
choice=input("enter 1 for add and 2 for remove and any number for exit : ")
if choice==1:
  num=input("enter number to add : ")
  arr.append(num)
  print(arr)
elif choice==2:
  num=input("enter number to remove : ")
  arr.remove(num)
  print(arr)
else:
  print("exit")

# Unpack the first two elements of a given tuple into separate variables and print them.
tupl = ("AI", "LAB", "1")
var1=tupl[0]
var2=tupl[1]
print(var1)
print(var2)

# Create a program to store five student names and their grades in a dictionary and then
# print the dictionary.
std = {}
for i in range(5):
  name = input("enter student name : ")
  grade = input("enter student grades : ")
  std[name] = grade
print(std)

# Set Operations
# ● Take two lists of integers from the user, convert them to sets, and display their union,
# intersection, and difference.

l1 = list(map(int, input("Enter integers for the first list separated by spaces: ").split()))
l2 = list(map(int, input("Enter integers for the second list separated by spaces: ").split()))

s1 = set(l1)
s2 = set(l2)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

# Conditional Statements: Number Checker
# ● Ask the user to enter an integer and determine if it is positive, negative, or zero, and
# whether it is even or odd.
number = int(input("Enter an integer: "))
if number > 0:
  print("positive.")
elif number < 0:
  print(" negative.")
else:
  print(" zero.")

if number % 2 == 0:
  print(" even.")
else:
  print("odd.")

# FizzBuzz
# ● Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with
# "Buzz", and multiples of both with "FizzBuzz".

for i in range(1, 51):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
# Function: Factorial Calculator
# ● Define a function to calculate the factorial of a non-negative integer using a loop.

def factorial(n):
  num = 1
  for i in range(1, n + 1):
    num *= i
  return num
temp=int(input("enter number to calc fact : "))
print(factorial(temp))

# Prime Number Checker
# ● Create a function to check if a number is prime and use it to verify a user-entered
# number.
def prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
temp=int(input("enter number to check prime : "))
print(prime(temp))

# List Comprehension: Squares
# ● Write a function that takes a list of integers and returns a new list with the squares of
# each number using list comprehension.

def square(lst):
  for i in range(len(lst)):
    lst[i] = lst[i] ** 2
  return lst

lst = [1,2,3,4,5]
print(square(lst))

# Merge Dictionaries
# ● Merge two dictionaries into one, with the second dictionary's values overwriting the first's
# in case of duplicate keys.

dict1 = {"hel": 1, "hello": 2}  
dict2 = {"AI": 3, "AI2": 4}
dict1.update(dict2)
print(dict1)

# Remove Duplicates from a List
# ● Write a function that removes duplicates from a list of integers while preserving the
# original order.

def rmv_dup(lst):
  for i in range(len(lst)):
    if lst.count(lst[i]) > 1:
      lst.remove(lst[i])

lst = [1,2,2,5,5,3,4]
print(rmv_dup(lst))

# Palindrome Checker
# ● Create a function to check whether a given string is a palindrome, ignoring case and
# spaces.

def pali(s):
  t=s.remove(" ")
  if t==t[::-1]:
    return True
s=input("enter str to check palindrome : ")
print(pali(s))

# Fibonacci Sequence Generator
# ● Write a function that generates the first n numbers in the Fibonacci sequence based on
# user input.
def fib(n):
  a=0
  b=1
  for i in range(n):
    print(a)
    a=b
    b=a+b

n=int(input("enter number to generate fibonacci : "))
fib(n)

# Average Calculator with Validation
# ● Develop a program that takes a series of numbers from the user, validates the input, and
# calculates the average.

def calc_avg(lst):
  s=0
  for i in lst:
    s+=i
  return s/len(lst)

lst = [1,2,3,4,5]
print(calc_avg(lst))

# Nested Loops: Multiplication Table
# ● Generate and print a multiplication table from 1 to 10 using nested loops.

for i in range(1, 11):
  print()
  print("table ",i)
  for j in range(1, 11):
    print(i * j,end=" ")

  
# User Registration System
# ● Implement a simple registration and login system using a dictionary to store user
# credentials.

dict1 = {}
name = input("enter name : ")
password = input("enter password : ")
dict1[name] = password
print(dict1)

# Counting Elements with a Dictionary
# ● Take a list of words from the user and count the frequency of each word using a
# dictionary.

dict1 = {}  
lst = list(map(str, input("Enter words separated by spaces: ").split()))
for i in lst:
  dict1[i] = lst.count(i)
print(dict1)

# Temperature Converter
# ● Create a function to convert temperatures between Celsius and Fahrenheit based on
# user choice

def temp_conv(temp, unit):
  if unit == "C":
    return (temp * 9/5) + 32
  elif unit == "F":
    return (temp - 32) * 5/9
temp=int(input("enter temp : "))
unit=input("enter unit : ")
print(temp_conv(temp, unit))
