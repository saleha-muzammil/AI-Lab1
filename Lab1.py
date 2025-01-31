def helloPython():
    name, age = input("Please enter your name and age (name/age): ").strip().split('/')
    print(f"Welcome, {name}! You are {age} years old.")


def dataTypeIdentification():
    num = input("Enter some numbers to check their data type: ")
    if "." in num:
        print("Data type is: float")
        print(f"Converted to int: {round(float(num))}")
    else:
        print("Data type is: int")
        print(f"Converted to float: {float(num)}")


def listOperations():
    this_list = ['a', 'B', 'c', 'd', 'E', 'f', 'G', 'h']
    print(f"List: {this_list[::]}")
    rem_letter = input("Enter a letter to remove from the list: ")
    this_list.remove(rem_letter)
    print(f"Modified List: {list[::]}")
    add_letter, index = input("Enter a letter to add to the list (letter/index): ").strip().split('/')
    this_list.insert(int(index), add_letter)
    print(f"Modified List: {this_list[::]}")
    lower_list = [element.lower() for element in this_list]
    print(f"Lower Case List: {lower_list[::]}")
    upper_list = [element.upper() for element in this_list]
    print(f"Upper Case List: {upper_list[::]}")


def tupleUnpacking():
    this_tuple = (10, "hundred", "@#", 500, -23)
    print(f"Tuple: {this_tuple}")
    variable1, variable2, *extra = this_tuple
    print(f"Variable 1 of Tuple: {variable1}")
    print(f"Variable 2 of Tuple: {variable2}")


def dictionaryManagement():
    d1 = {'Charlie': 54, 'Kate': 23, 'Alice': 98, 'Bob': 79, 'Ben': 82}
    print(d1)
    d2 = {}
    i = 5
    while i > 0:
        name, grade = input("Enter Student Name and Grade (name/grade): ").strip().split('/')
        d2[name] = grade
        i = i - 1
    print(d2)


def setOperations():
    list1 = list(map(int, input("Enter the first list of numbers (num1,num2,...): ").split(',')))
    list2 = list(map(int, input("Enter the second list of numbers (num1,num2,...): ").split(',')))

    set1 = set(list1)
    set2 = set(list2)

    print("Set 1: ", set1)
    print("Set 2: ", set2)

    print("Union: ", set1 | set2)
    print("Intersection: ", set1 & set2)
    print("Difference (Set1 - Set2): ", set1 - set2)
    print("Difference (Set2 - Set1): ", set2 - set1)


def numberChecker():
    num = int(input("Enter an integer: "))

    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")


def fizzBuzz():
    num_list = {}
    i = 1
    while i != 50:
        num_list[i-1] = i
        i = i + 1
    print("Numbers: ", num_list)

    for j in num_list:
        if (j % 3 == 0) & (j % 5 != 0):
            num_list[j] = "Fizz"
        elif (j % 5 == 0) & (j % 3 != 0):
            num_list[j] = "Buzz"
        elif (j % 3 == 0) & (j % 5 == 0):
            num_list[j] = "FizzBuzz"
        j = j + 1
    print("Numbers: ", num_list)


def factorialCalculator():
    n = int(input("Please enter a number to calculate factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"Factorial of {n} is {result}")


def primeNumChecker():
    num = int(input("Enter a number to check if it's prime: "))
    check = False
    if num < 2:
        print(f"Invalid number. {num} is smaller than 2.")
    else:
        i = 2
        while (i >= 2) & (i <= int(num ** 0.5) + 1):
            if num % i == 0:
                check = False
                print(f"{num} is not a prime number.")
                break
            else:
                check = True
                i = i + 1
        if check == True:
            print(f"{num} is a prime number.")


def mergeDictionaries():
    dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
    print("Dictionary 1: ", dict1)
    dict2 = {"b": 20, "d": 1, "e": 5}
    print("Dictionary 2: ", dict2)
    dict1.update(dict2)
    print("Merged Dictionary: ", dict1)


def removeDuplicatesFromList():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    seen = set()
    new_nums = list(x for x in nums if not (x in seen or seen.add(x)))
    print("List after removing duplicates:", new_nums)


def palindromeChecker():
    text = input("Enter a string to check if it's a palindrome: ")
    pal_string = ''.join(text.lower().split())
    if pal_string == pal_string[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")


def fibonacciGenerator():
    num = int(input("Enter how many Fibonacci numbers to generate: "))
    if num <= 0:
        print("Please enter a positive integer.")
        return
    fib_seq = [0, 1]
    for _ in range(2, num):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    print("Fibonacci Sequence:", fib_seq[:num])


def averageCalculator():
    numbers = []
    while True:
        num = input("Enter a number (or type 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"Average of entered numbers: {avg:.2f}")
    else:
        print("No valid numbers were entered.")


def multiplicationTable():
    print("Multiplication Table (1 to 10):\n")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end=" ")
        print()


def countElementsInDictionary():
    text = input("Enter a sentence: ")
    words = text.split()
    frequency = {}

    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1

    print("Word Frequencies:")
    for word, count in frequency.items():
        print(f"{word}: {count}")


def temperatureConverter():
    print("\n1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")


def lab1():
    helloPython()
    dataTypeIdentification()
    listOperations()
    tupleUnpacking()
    dictionaryManagement()
    setOperations()
    numberChecker()
    fizzBuzz()
    factorialCalculator()
    primeNumChecker()
    mergeDictionaries()
    removeDuplicatesFromList()
    palindromeChecker()
    fibonacciGenerator()
    averageCalculator()
    multiplicationTable()
    countElementsInDictionary()
    temperatureConverter()


if __name__ == '__main__':
    lab1()