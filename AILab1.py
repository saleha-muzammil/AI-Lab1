def hello_python():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")

def data_type_identification():
    value = input("Enter something: ")
    try:
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
    except ValueError:
        pass
    print(f"The data type of input is: {type(value)}")

def list_operations():
    my_list = ["apple", "banana", "cherry"]
    my_list.append("date")
    my_list.remove("banana")
    print([item.upper() for item in my_list])

def tuple_unpacking():
    my_tuple = (10, 20, 30, 40)
    first, second, *_ = my_tuple
    print(first, second)

def dictionary_management():
    students = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92, "Eve": 88}
    print(students)

def set_operations():
    list1 = set(map(int, input("Enter numbers for list1: ").split()))
    list2 = set(map(int, input("Enter numbers for list2: ").split()))
    print("Union:", list1 | list2)
    print("Intersection:", list1 & list2)
    print("Difference:", list1 - list2)

def number_checker():
    num = int(input("Enter an integer: "))
    print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
    print("Even" if num % 2 == 0 else "Odd")

def fizzbuzz():
    for i in range(1, 51):
        print("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def prime_checker(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_comprehension_squares(nums):
    return [x ** 2 for x in nums]

def merge_dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def palindrome_checker(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def fibonacci(n):
    fib_seq = [0, 1]
    for _ in range(n - 2):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def average_calculator():
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    print("Average:", sum(numbers) / len(numbers) if numbers else 0)

def multiplication_table():
    for i in range(1, 11):
        print(" ".join(f"{i * j:2}" for j in range(1, 11)))

def user_registration():
    users = {}
    while True:
        action = input("Register/Login/Exit: ").lower()
        if action == "register":
            username = input("Username: ")
            password = input("Password: ")
            users[username] = password
        elif action == "login":
            username = input("Username: ")
            if users.get(username) == input("Password: "):
                print("Login successful!")
            else:
                print("Invalid credentials!")
        elif action == "exit":
            break

def word_frequency():
    words = input("Enter words: ").split()
    print({word: words.count(word) for word in set(words)})

def temperature_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Convert to (C/F): ").upper()
    print((temp - 32) * 5/9 if unit == "C" else temp * 9/5 + 32, "degrees", unit)

# Example usage:
if __name__ == "__main__":
    hello_python()
    data_type_identification()
    list_operations()
    tuple_unpacking()
    dictionary_management()
    set_operations()
    number_checker()
    fizzbuzz()
    print(factorial(5))
    print(prime_checker(7))
    print(list_comprehension_squares([1, 2, 3]))
    print(merge_dictionaries({"a": 1}, {"b": 2}))
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(palindrome_checker("A man a plan a canal Panama"))
    print(fibonacci(10))
    average_calculator()
    multiplication_table()
    user_registration()
    word_frequency()
    temperature_converter()
