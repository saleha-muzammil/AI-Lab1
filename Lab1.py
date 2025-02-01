#Q1
# name=input("Enter your name: ")
# age = int(input("Enter your age: "))


# print("Hello World!",name,"!")

# def determine_data_type(user_input):
   
#     try:
#         return int(user_input), 'int'
#     except ValueError:
#         pass

  
#     try:
#         return float(user_input), 'float'
#     except ValueError:
#         pass


#     return user_input, 'string'


#Q2
# Main function to take user input
# def main():
#     user_input = input("Enter something: ")
#     value, data_type = determine_data_type(user_input)
#     print(f"Value: {value}, Data Type: {data_type}")
    
# def list_operations():
  
#     my_list = ['apple', 'banana', 'cherry','mango']
#     print("Original List:", my_list)
    

#     my_list.append('date')
#     my_list.append('peach')
#     print("List after adding items:", my_list)
    

#     my_list.remove('banana')
#     print("List after removing 'banana':", my_list)
 
#     print("List elements in uppercase:")
#     for item in my_list:
#         print(item.upper())

# Run the function
list_operations()
# Run the main function
# if __name__ == "__main__":
#     main()

#Q3
my_tuple = (1, 2, 3, 4, 5)
first, second = my_tuple[0], my_tuple[1]
print("First:", first)
print("Second:", second)

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}
print(students)


list1 = list(map(int, input("Enter integers for the first list (comma-separated): ").split(',')))
list2 = list(map(int, input("Enter integers for the second list (comma-separated): ").split(',')))

set1 = set(list1)
set2 = set(list2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

number = int(input("Enter an integer: "))
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
    
    for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
        
        def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Example usage

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it's prime: "))
print(is_prime(number))

def square_numbers(numbers):
    return [x**2 for x in numbers]

print(square_numbers([1, 2, 3, 4, 5]))  # Example usage

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Example usage

def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # Example usage

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))

numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == 'done':
        break
    try:
        numbers.append(float(num))
    except ValueError:
        print("Please enter a valid number.")

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No numbers were entered.")
    
    for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=' ')
    print()
    
    users = {}

def register(username, password):
    if username in users:
        return "Username already exists."
    users[username] = password
    return "Registration successful."

def login(username, password):
    if users.get(username) == password:
        return "Login successful."
    return "Invalid credentials."

# Example usage
print(register("user1", "pass1"))
print(login("user1", "pass1"))


words = input("Enter words (space-separated): ").split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

def convert_temperature(value, to_scale):
    if to_scale == 'C':
        return (value - 32) * 5/9
    elif to_scale == 'F':
        return (value * 9/5) + 32
    else:
        return "Invalid scale."

temp = float(input("Enter temperature: "))
scale = input("Convert to (C/F): ").upper()
print("Converted temperature:", convert_temperature(temp, scale))