import string


# Task 1
def greeting_task():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hi" + name + ", you are " + age + " years old.\n")


# Task 2
def datatype_identification():
    userInput = input("Enter your input: ")
    try:
        if int(userInput):
            print("int type")
    except ValueError as e:
        try:
            if float(userInput):
                print("float type")
        except ValueError as e:
            if userInput.lower()=='true' or userInput.upper()=='false':
                print("boolean type")
            else:
                print("string type")


# Task 3
def modify_list():
    tmpList = ['i', 'am', 'hassaan', 'raza', '.']
    userInput = input("Enter the string to append: ")
    tmpList.append(userInput)
    newList = []
    for i in tmpList:
        newList.append(i.upper())
    for i in newList:
        print(i)


# Task 4
def tuple_unpack():
    first, second = ("Hello", "World")
    print(first + " " + second)


# Task 5
def dict_manage():
    studentsDict ={
        "Hassaan": "F",
        "GA": "A+",
        "Mujtaba": "A",
        "Ahmed": "B",
        "Aun": "C"
    }
    # print(studentsDict)
    for key, val in studentsDict.items():
        print(key + " has grade " + val + ".")


# Task 6
def set_merge():
    list1 = []
    list2 = []

    print("Add int elements to list 1: (-1 to end)")
    userInput = 0
    while userInput != '-1':
        userInput = input("append: ")
        if userInput != '-1':
            try:
                if int(userInput):
                    list1.append(int(userInput))
            except ValueError as e:
                userInput = '-1'

    print("Add int elements to list 2: (-1 to end)")
    userInput = 0
    while userInput != '-1':
        userInput = input("append: ")
        if userInput != '-1':
            try:
                if int(userInput):
                    list2.append(int(userInput))
            except ValueError as e:
                userInput = '-1'

    # print(list1)
    # print(list2)
    set1 = set(list1)
    set2 = set(list2)
    union = set1 | set2
    inter = set1 & set2
    diff = set1 - set2

    print("Union: ", union)
    print("Intersection: ", inter)
    print("Difference: ", diff)


# Task 6
def number_checker():
    num = input("Enter an integer: ")

    while 1:
        if num == '0':
            print("Zero\nEven")
            break
        else:
            try:
                if int(num):
                    num = int(num)
                    if num > 0:
                        print("Positive")
                    elif num < 0:
                        print("Negative")

                    try:
                        if num % 2 == 0:
                            print("Even")
                        else:
                            print("Odd")
                    except ZeroDivisionError as e:
                        print("Even")  # 0 is even
                    break

            except ValueError as e:
                num = input("Re-enter an INTEGER: ")


# Task 7
def fizz_buzz():
    for num in range(1, 51):
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


# Task 8
def fact():
    while 1:
        num = input("Enter a non-negative integer: ")
        if num == '0':
            print("1")
        else:
            try:
                if int(num):
                    num = int(num)
                    if num > 0:
                        prod = 1
                        for i in range(1, num + 1):
                            prod *= i
                        print(prod)
                        break
            except ValueError as e:
                pass


# Task 9
def prime_checker():
    def prime(val):
        for j in range(2, (val/2) + 1):
            if val % j == 0:
                return 0
        return 1

    while 1:
        num = input("Enter a positive integer greater than 1: ")
        try:
            if int(num):
                num = int(num)
                if num > 1:
                    if prime(num):
                        print(num, " is a prime.")
                    else:
                        print(num, " is a composite.")
                    break
        except ValueError as e:
            pass


# Task 10
def list_comp():
    list1 = []

    print("Add int elements to list: (x to end)")
    userInput = 0
    while userInput != 'x':
        userInput = input("append: ")
        if userInput != 'x':
            try:
                if int(userInput) or userInput == '0':
                    list1.append(int(userInput))
            except ValueError as e:
                userInput = 'x'

    print(list1)
    newList = [x**2 for x in list1]
    print(newList)


# Task 11
def merge_dictionaries():
    dict1 = {
        "a": 'old a',
        "b": 'old b',
        "c": 'old c'
    }
    dict2 = {
        "b": 'new b',
        "c": 'new c'
    }
    merged = dict1.update(dict2)
    print(dict1)


# Task 12
def rem_dup():
    list1 = []

    print("Add int elements to list: (x to end)")
    userInput = 0
    while userInput != 'x':
        userInput = input("append: ")
        if userInput != 'x':
            try:
                if int(userInput) or userInput == '0':
                    list1.append(int(userInput))
            except ValueError as e:
                userInput = 'x'
    print(list1)

    newList = []
    for i in list1:
        if i not in newList:
            newList.append(i)
    print(newList)


# Task 13
def palindrome_checker():
    userInput = input("Enter a string to check palindrome: ")
    isPal = lambda val: val == val[::-1]
    if isPal(userInput):
        print(userInput + " is a palindrome.")
    else:
        print(userInput + " is NOT a palindrome.")


# Task 14
def fib_generator():
    while 1:
        num = input("Enter a positive integer n (n >= 1) for Fibonacci Sequence: ")
        try:
            if int(num):
                num = int(num)
                if num >= 1:
                    first = 0
                    second = 1
                    if num == 1:
                        print(first)
                    elif num >= 2:
                        print(str(first) + "\n" + str(second))
                        for i in range(2, num):
                            tmp = first + second
                            first = second
                            second = tmp
                            print(str(second))

                    break
        except ValueError as e:
            pass


# Task 15
def avg_calc():
    list1 = []

    print("Add int elements to list: (x to end)")
    userInput = 0
    while userInput != 'x':
        userInput = input("append: ")
        if userInput != 'x':
            try:
                if int(userInput) or userInput == '0':
                    list1.append(int(userInput))
            except ValueError as e:
                userInput = 'x'

    print(list1)

    total = sum(list1)
    print("Average: " + str(float(total) / len(list1)))


# Task 16
def multiplication_table():
    for i in range(1, 11):
        print("MULTIPLICATION TABLE OF " + str(i))
        for j in range(1, 11):
            print(str(i) + " x " + str(j) + " = " + str(i * j))
        print("\n")


# Task 17
def user_reg():
    userDetails = {
        'hassaan202': '123',
        'mujtaba123': '456',
        'gaharoon': '789'
    }
    userName = input("Enter username: ")
    if userName in userDetails:
        password = input("Enter password: ")
        if userDetails[userName] == password:
            print("Logged in!")
        else:
            print("Incorrect password entered.")
    else:
        print("username not present.")


# Task 18
def count_elements():
    list1 = []

    print("Add words to the list: (x to end)")
    userInput = 0
    while userInput != 'x':
        userInput = input("append: ")
        if userInput != 'x':
            list1.append(userInput)

    print(list1)

    newDict = {}
    for word in list1:
        if word in newDict:
            newDict[word] += 1
        else:
            newDict.update({word: 1})

    print(newDict)


# Task 19
def convert_temperature():
    def convert(x, ch):
        if ch == 1:
            res = (x * 1.8) + 32
            print(str(x) + " celsius to " + str(res) + " fahrenheit.")
        elif ch == 2:
            res = (x - 32) * 0.555555555
            print(str(x) + " fahrenheit to " + str(res) + " celsius.")

    while 1:
        num = input("Press 1 from C to F, 2 for F to C: ")
        try:
            if int(num):
                num = int(num)
                if num == 1 or num == 2:
                    while 1:
                        val = input("Enter the value to be converted: ")
                        try:
                            if int(val) or val == '0':
                                val = int(val)
                                convert(val, num)
                                break
                        except ValueError as e:
                            try:
                                if float(val) or val == '0.0':
                                    val = float(val)
                                    convert(val, num)
                                    break
                            except ValueError as e:
                                print("Value must be float or int")
                    break
        except ValueError as e:
            print("Incorrect value entered!")
            pass


def main():
    # greeting_task()
    # datatype_identification()
    # modify_list()
    # tuple_unpack()
    # dict_manage()
    # set_merge()
    # number_checker()
    # fizz_buzz()
    # fact()
    # prime_checker()
    # list_comp()
    # merge_dictionaries()
    # rem_dup()
    # palindrome_checker()
    # fib_generator()
    # avg_calc()
    # multiplication_table()
    # user_reg()
    # count_elements()
    convert_temperature()


if __name__ == "__main__":
    main()
