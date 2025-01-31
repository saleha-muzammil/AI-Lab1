
#(1)a program that asks the user for their name and age, then prints a greeting message.
name=input("Enter Name:")
age=int(input("Enter a Value:"))
#Print greetings
print("Hello",name,"Welcome!")

#(2)Create a program that takes user input and determines its data type, handling conversions to int or float when possible.
user_input = input("Please enter something: ")
try:
    converted_input = int(user_input)
    print(f"The data type of your input is: {type(converted_input).__name__} (int)")

except ValueError:
   
    try:
        converted_input = float(user_input)
        print(f"The data type of your input is: {type(converted_input).__name__} (float)")

    except ValueError:
        print(f"The data type of your input is: {type(user_input).__name__} (string)")

#(3) Initialize a list with specific elements, modify it by adding and removing items, and print each element in uppercase.
my_list = ['apple', 'banana', 'cherry']
my_list.append('date')
my_list.insert(1, 'blueberry')  

my_list.remove('banana')  
del my_list[0]  
for item in my_list:
    print(item.upper())

#(4)Unpack the first two elements of a given tuple into separate variables and print them. 
my_tuple = (10, 20, 30, 40)

a, b = my_tuple[:2]

print("First element:", a)
print("Second element:", b)

#(5)Create a program to store five student names and their grades in a dictionary and then print the dictionary.
students = {
    "Moeez": 85,
    "Anas": 90,
    "Ahmad": 78,
    "Ali": 92,
    "Umair": 88
}

print("Student Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

#(6) Take two lists of integers from the user, convert them to sets, and display their union, intersection, and difference.
list1 = list(map(int, input("Enter integers for the first list (space-separated): ").split()))
list2 = list(map(int, input("Enter integers for the second list (space-separated): ").split()))

# Converting lists to sets
set1 = set(list1)
set2 = set(list2)

union_set = set1 | set2  
intersection_set = set1 & set2 
difference_set = set1 - set2  

# Displaying results
print("\nUnion:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)

#(7)Ask the user to enter an integer and determine if it is positive, negative, or zero, and whether it is even or odd. 
num = int(input("Enter an integer: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#(8) Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with 
"Buzz", and multiples of both with "FizzBuzz". 
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#(9)Define a function to calculate the factorial of a non-negative integer using a loop.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i  
    
    return result

num = int(input("Enter a non-negative integer: "))
print(f"Factorial of {num} is {factorial(num)}")

#(10)Create a function to check if a number is prime and use it to verify a user-entered number. 
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False 

    for i in range(2, int(n ** 0.5) + 1):  =
        if n % i == 0:
            return False  

    return True 

num = int(input("Enter a number to check if it is prime: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#(11)Write a function that takes a list of integers and returns a new list with the squares of each number using list comprehension. 
def square_list(numbers):
    """Return a list with the squares of each number."""
    return [num ** 2 for num in numbers]

nums = list(map(int, input("Enter integers separated by spaces: ").split()))

squared_nums = square_list(nums)

print("Squared numbers:", squared_nums)

#(12) Merge two dictionaries into one, with the second dictionary's values overwriting the first's in case of duplicate keys. 
def merge_dicts(dict1, dict2):
    """Merge two dictionaries, with dict2 overwriting dict1 in case of duplicate keys."""
    merged = dict1.copy() 
    merged.update(dict2)  
    return merged

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

merged_dict = merge_dicts(dict1, dict2)

print("Merged Dictionary:", merged_dict)

#(13) a function that removes duplicates from a list of integers while preserving the original order.
def remove_duplicates(lst):
    """Remove duplicates while preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

nums = list(map(int, input("Enter integers separated by spaces: ").split()))

unique_nums = remove_duplicates(nums)

print("List without duplicates:", unique_nums)

#(14) a function to check whether a given string is a palindrome, ignoring case and spaces.
def is_palindrome(s):
    """Check if the string is a palindrome, ignoring case and spaces."""
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

#(15)a function that generates the first n numbers in the Fibonacci sequence based on user input.
def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_numbers = fibonacci(n)

print(f"The first {n} Fibonacci numbers are: {fib_numbers}")


#(16)a program that takes a series of numbers from the user, validates the input, and calculates the average. 
def calculate_average():
    """Take numbers from the user and calculate the average."""
    numbers = []
    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            if len(numbers) == 0:
                print("No numbers entered. Cannot calculate average.")
                return
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")

calculate_average()

#(17) Generate and print a multiplication table from 1 to 10 using nested loops.
def multiplication_table():
    """Generate and print a multiplication table from 1 to 10."""
    for i in range(1, 11):  
        for j in range(1, 11):  
            print(f"{i * j:4}", end=" ")
        print() 

multiplication_table()

#(18)Implement a simple registration and login system using a dictionary to store user 
credentials. 

users = {}

def register():
    """Register a new user."""
    print("Registration")
    username = input("Enter a username: ")
    if username in users:
        print("Username already taken. Please choose a different one.")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print("Registration successful!")

def login():
    """Login with an existing user."""
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    """Main function to handle registration and login."""
    while True:
        choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\nYour choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

#(19) Take a list of words from the user and count the frequency of each word using a dictionary.
def count_word_frequency():
    """Count the frequency of each word in the list."""
    words = input("Enter a list of words separated by spaces: ").split()  
    
    word_count = {}  
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print("\nWord frequencies:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

count_word_frequency()


#(20)Create a function to convert temperatures between Celsius and Fahrenheit based on user choice. 
def convert_temperature():
    """Convert temperatures between Celsius and Fahrenheit."""
    print("Temperature Conversion")
    choice = input("Choose the conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nYour choice: ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32 
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9  
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    
    else:
        print("Invalid choice! Please choose 1 or 2.")

convert_temperature()
















