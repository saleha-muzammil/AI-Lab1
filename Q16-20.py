#average calculator with validator 

def average(lst):
    return sum(lst)/len(lst)

def validator(lst):
    return all(isinstance(x, (int, float)) for x in lst)

lst = [1,2,3,4,5,6,7,8,9,10]
while True:
    if validator(lst):
        print(average(lst))
        break
    else:
        print("Please enter a valid list of numbers")
        lst = [int(x) for x in input("Enter the list of numbers :").split()]

#nested loop multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("\n")


#user registration system 

users = {}

# Function to register a new user
def register(username, password):
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print("User registered successfully!")

# Function to login a user
def login(username, password):
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Main program
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")



# Counting word frequency with a dictionary
def count_word_frequency(words):
    return {word: words.count(word) for word in words}

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_frequency = count_word_frequency(words)
print(word_frequency)


#temperature converter
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def farhenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp= float(input("Enter the temperature :"))
unit = input("Enter the unit (C/F) :")
if unit.upper() == "C":
    print(celsius_to_fahrenheit(temp))
elif unit.upper() == "F":
    print(farhenheit_to_celsius(temp))
else:
    print("Please enter a valid unit (C/F)")
