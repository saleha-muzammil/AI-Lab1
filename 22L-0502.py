#  Task No 1
# Write a program that asks the user for their name and age, then prints a greeting 
# message. 
def task1():
    Name = input(" Enter Your Name ")
    Age = input(" Enter You Age ")
    Age = int(Age)
    print("Hello ", Name, " Ypu are ", Age, "years old")

task1()
# Task No 2
# Create a program that takes user input and determines its data type, handling 
# conversions to int or float when possible.
def task2():
    data = input(" Enter Data")
    if data.isdigit():
        print(" Data is Integer ")
        data = int(data)
        print(" Data is: ", data)
    elif data.replace(".","",1).isdigit():
        print(" Data is Float ")
        data = float(data)
        print(" Data is: ", data)
    else:
        print(" Data is Dtring")
        # data = str(data)
        # print(" Data is: ", data)
task2()
# Task No 3
# Initialize a list with specific elements, modify it by adding and removing items, and print 
# each element in uppercase. 

def Task3():
    myList = [" Moli "," Gajar "," Pyaz ", " Aloo ", " Palak "]
    print(" Original List is: ", myList)
    choice = input(" Enter 1 to add Elem, 2 for Remove Elem and 3 for Print Elem in Upper Case")
    if choice == "1":
        elem = input(" Enter Elem to Add ")
        myList.append(elem)
        print(" List after adding Elem: ", myList)
    elif choice == "2":
        elem = input(" Enter Elem to Remove ")
        myList.remove(elem)
        print(" List after removing Elem: ", myList)
    elif choice == "3":
        for elem in myList:
            print("Elem in Upper Carse: ", elem.upper())
Task3()
# Task No 4
# Unpack the first two elements of a given tuple into separate variables and print them. 

def Task4():
    myTupple = (" Moli "," Gajar "," Pyaz ", " Aloo ", " Palak ")
    print(" Original Tupple is: ", myTupple)
    elem1 = myTupple[0]
    elem2 = myTupple[1]
    print(" First Elem is: ", elem1)
    print(" Second Elem is: ", elem2)
Task4()

# Task No 5
# Create a program to store five student names and their grades in a dictionary and then 
# print the dictionary.

def Task5():
    myDict = {}
    for i in range(5):
        name = input(" Enter Student name:")
        grade = input(" Enter STudent Grade:")
        myDict[name] = grade
    print(" Dictionary is: ", myDict)
Task5()

# Task No 6
# Take two lists of integers from the user, convert them to sets, and display their union, 
# intersection, and difference. 
def Task6():
    list1 = []
    list2 = []
    for i in range (5):
        elem = input(" Enter Elem for List 1: ")
        list1.append(int(elem))
    for i in range (5):
        elem = input(" Enter Elem for List 2: ")
        list2.append(int(elem))
    set1 = set(list1)
    set2 = set(list2)
    print(" Union is: ", set1.union(set2))
    print(" Intersection is: ", set1.intersection(set2))
    print(" Difference is: ", set1.difference(set2))
Task6()

# Task No 7
# Ask the user to enter an integer and determine if it is positive, negative, or zero, and 
# whether it is even or odd. 

def Task7():
    num = input(" Enter the Number: ")
    num = int(num)
    if num > 0 
        print(" Number is Positive ")
    elif num < 0:
        print(" Number is Negative ")
    else:
        print(" Number is Zero ")   
    if num % 2 == 0:
        print(" Number is Even ")   
    else:
        print(" Number is Odd ")
Task7()


# Task No 8
# Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with 
# "Buzz", and multiples of both with "FizzBuzz".

def Task8():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print(" FitBuzz ")
        elif i % 3 == 0:
            print(" Fizz ")
        elif i % 5 == 0:
            print(" Buzz ")     
        else:
            print(i)
Task8()

# Task No 9
# Define a function to calculate the factorial of a non-negative integer using a loop. 

def fict():
    num = input(" Enter the Number: ")
    num = int(num)
    if num < 0:
        print(" It is a Negative Number ")
        return
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(" Factorial is: ", fact) 
fict()

# Task No 10
# Create a function to check if a number is prime and use it to verify a user-entered 
# number. 

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

n = input(" Enter the Number: ")
isPrime(n)
    
# Task No 11
# Write a function that takes a list of integers and returns a new list with the squares of 
# each number using list comprehension.
def task11():
    list1 = []
    for i in range(5):
        elem = input(" Enter ELem: ")
        list1.append(int(elem))
    sqrList = [x*x for x in list1]
    print(" Squared List is: ", sqrList)
task11()

# Task No 12
# Merge two dictionaries into one, with the second dictionary's values overwriting the first's 
# in case of duplicate keys. 

def Task12():
    myDict = {"Name":"Ali", "Age":25, "City":"Karachi"}
    myDict2 = {"Name":"Ahmed", "Age":30, "City":"Lahore"}
    myDict.update(myDict2)
    print(" Merged Dictionary is: ", myDict)
Task12()


# Task No 13
# Write a function that removes duplicates from a list of integers while preserving the 
# original order.

def Task13():
    myList = [1,2,3,4,5,2,3,4,5,6,7,8,9,1]
    print(" Oroginal List is: ", myList)
    newList = []
    for elem in myList:
        if elem not in newList:
            newList.append(elem)
    print(" List after removing duplicates: ", newList)
Task13()

# Task No 14
# Create a function to check whether a given string is a palindrome, ignoring case and 
# spaces.
    
def Task14():
    str = input(" Enter the String: ")
    str = str.replace(" ","")
    str = str.lower()
    if str == str[::-1]:
        print(" String is Palindrome ")
    else:
        print(" String is not Palindrome ")
Task14()

# Task No 15
# Write a function that generates the first n numbers in the Fibonacci sequence based on 
# user input. 

def Task15():
    num = input(" Enter the Number: ")
    num = int(num)
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,num):
        c = a+b
        print(c)
        a = b
        b = c
Task15()


# Task No 16
# Develop a program that takes a series of numbers from the user, validates the input, and 
# calculates the average.

def Task16():
    sum = 0
    count = 0
    while True:
        num = input(" Enter the Number and press 'e for exit': ")
        if num == "e":
            break
        num = int(num)
        sum = sum + num
        count = count + 1
    avg = sum / count
    print(" Average is: ", avg)
Task16()

# # Task No 17
# Generate and print a multiplication table from 1 to 10 using nested loops.

def TAsk17():
    for i in range(1,11):
        for j in range(1,11):
            print(i, " x ", j, " = ", i*j)
TAsk17()

# Task No 18
# Implement a simple registration and login system using a dictionary to store user 
# credentials. 
def Task18():
    myDict = {}
    while True:
        choice = input(" Enter 1 for Registration, 2 for Login and 3 for Exit")
        if choice == "1":
            userName = input(" Enter youtr User Name: ")
            password = input(" Enter your Password: ")
            myDict[userName] = password
        elif choice == "2":
            uuserName = input(" Enter youtr User Name: ")
            password = input(" Enter your Password: ")
            if myDict[userName] == password:
                print(" Login Successfull")
            else:
                print(" Login Failed! May be You are Not Registered")
        elif choice == "3":
            break
Task18()

# Task No 19
# Take a list of words from the user and count the frequency of each word using a 
# dictionary. 

def Task19():
    myDict = {}
    words = []
    for i in range(5):
        word = input(" Enter the Word: ")
        words.append(word)
    for word in words:
        if word in myDict:
            myDict[word] = myDict[word] + 1
        else:
            myDict[word] = 1
    print(" Dictionary is: ", myDict)
Task19()

# Task No 20
# Create a function to convert temperatures between Celsius and Fahrenheit based on 
# user choice. 
    
def TAsk20():
    while True:
        choice = input(" Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius and 3 for Exit")
        if choice == "1":
            temp = input(" Enter the Temperature in Celsius: ")
            temp = float(temp)
            temp = (temp * 9/5) + 32
            print(" Temperature in Fahrenheit is: ", temp)
        elif choice == "2":
            temp = input(" Enter the Temperature in Fahrenheit: ")
            temp = float(temp)
            temp = (temp - 32) * 5/9
            print(" Temperature in Celsius is: ", temp)
        elif choice == "3":
            break
TAsk20()





