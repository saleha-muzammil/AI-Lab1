# -*- coding: utf-8 -*-
"""AI-lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t3S1lqH9ZmqP5xIVAfi6e9JCbsETR9BK
"""



from re import I

# # part 1
# name =input("Enter your name: ")
# age =input("Enter your agee: ")

# print("Hello %s, aged %s"  % (name, age))



# # part 2
# data =input("Enter some data: ")

# try:
#     i=int(data)
#     print("The data is an integer number= ", i)

# except ValueError:
#         try:
#             f=float(data)
#             print("The data is a float number= ", f)

#         except ValueError:
#              print("The data is a string = ", data)



# #part 3
# pookielist=['kafka', 'jane austen', 'charles bukowski']
# pookielist.append('max verstappen')
# pookielist.remove('kafka')

# for i in pookielist:
#     print(i.upper())


# #part 4
# pookieTuple=('kafka', 'jane austen', 'charles bukowski')

# ele1=pookieTuple[0]
# ele2=pookieTuple[1]

# print(ele1)
# print(ele2)


# #part 5

# amalNama ={
#     'laiba' :'A',
#     'arham':'A',
#     'umer':'F'
# }
# print(amalNama)


##part 6
# l1 = list(map(int, input("Enter integer list 1: ").split()))
# l2 = list(map(int, input("Enter integer list 2: ").split()))

# set1 = set(l1)
# set2 = set(l2)

# print("Union:", set1 | set2)
# print("Intersection:", set1 & set2)
# print("Difference (set1 - set2):", set1 - set2)


## part 7
# num =int(input("enter number:"))
# if(num>0):
#   print ("Number is positive")
# elif(num<0):
#   print  ("number is negative")
# else:
#   print  ("number is zerooo")
# if num % 2 == 0:
#     print("number is even.")
# else:
#     print("number is odd.")


## part 8
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzzzBuzzzz")
#     elif i % 3 == 0:
#         print("Fizzzzz")
#     elif i % 5 == 0:
#         print("Buzzzz")
#     else:
#         print(i)

##part 9
# def factorial(n):
#     if(n<0):
#       print("num shoukd be positive!")
#       return
#     else:
#       res=1
#       for i in range (1, n+1):
#         res=res*i
#     return res

# n=int(input("enter a number"))
# print("factorial of this num is:", factorial(n))


##part 10
# def isPrime(n):
#   if n <= 1:
#         return False
#   for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#   return True

# n=int(input("enter a number"))
# if (isPrime(n)):
#   print("num is prime!")
# else:
#    print("num is not prime!")


##part 11
# def listsquared(numbersList):
#   squaredList=[]
#   for n in numbersList:
#     squaredList.append(n*n)

#   return squaredList


# numbers=[1,2,3,4,5]
# print("This is the int list:", numbers)
# print("These is the squared list: ", listsquared(numbers))


##part 12
# dict1={
#     'laiba',
#     'arham',
#     'umer'
# }
# dict2={
#     'kainat',
#     'laiba'
# }

# def mergeDictionaries(d1, d2):
#   mergedDict=d1.copy()
#   mergedDict.update(d2)
#   return mergedDict

# print(mergeDictionaries(dict1, dict2))


##part 13
# pookielist=['kafka', 'jane austen', 'charles bukowski', 'kafka']
# def removeDuplicates(listt):
#   print("This is the list after removing duplicates: ",  list(set(listt)))

# print("This is the oroginal list: ",pookielist)
# removeDuplicates(pookielist)


#part 14
palindrome = lambda s: (s.replace(" ", "").upper() == s.replace(" ", "").upper()[::-1])

s=input("enter a string: ")
if(palindrome(s)):
  print("String is a plaindrome!")
else:
    print("String is not a plaindrome!")



##part 15
# def fibonnaci():
#   terms=int(input("enter the no of terms: "))
#   n1=0
#   n2=1
#   count=0

#   if terms <= 0:
#    print("Please enter a positive num")

#   elif terms == 1:
#     print("Fibonacci sequence upto",terms,":")
#     print(n1)

#   else:
#     print("Fibonacci sequence:")
#     while count < terms:
#         print(n1)
#         nth = n1 + n2

#         n1 = n2
#         n2 = nth
#         count += 1

# fibonnaci()



##part 16
# def calcAverage():

#     numbers = []
#     while True:
#         try:
#             num = input("Enter a number (or type 'done' to finish): ")
#             if num.lower() == 'done':
#                 break
#             numbers.append(float(num))
#         except ValueError:
#             print("Invalid input! Please enter a positive number")

#     if numbers:
#         average = sum(numbers) / len(numbers)
#         print(f"The average is: {average}")

# calcAverage()


##part 17
# def multiplicationTable():
#   if n<0:
#     return "invalid number"
#   else:
#     for i in range(1, 11):
#       print("table of ",i)
#       for j in range (1 ,13):
#         print(i ,"*" ,j, "=", i*j)



# #n=int(input("enter a number: "))
# multiplicationTable()



##part 18
# user_credentials = {}

# def register_user():
#     username = input("Enter a username: ")
#     if username in user_credentials:
#         print("Username already exists!")
#         return

#     password = input("Enter a password: ")
#     user_credentials[username] = password
#     print(f"Registration successful! Welcome, {username}.")


# def login_user():
#     username = input("Enter your username: ")
#     if username not in user_credentials:
#         print("Username not found! Please register first")
#         return
#     password = input("Enter your password: ")

#     if user_credentials[username] == password:
#         print(f"Login successful! Welcome back, {username}.")
#     else:
#         print("Incorrect password! Try again.")

# #main
# def user_registration_system():
#     while True:
#         print("\n--- User Registration System ---")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option: ")
#         if choice == '1':
#             register_user()
#         elif choice == '2':
#             login_user()
#         elif choice == '3':
#             print("Exiting the system :)) Goodbye!")
#             break
#         else:
#             print("Invalid choice, please try again.")

# user_registration_system()


##part 19
# def countWordFrequency():
#     words = input("Enter a list of words (separated by spaces): ").split()
#     word_count = {}

#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     print("\nWord frequencies:")
#     for word, count in word_count.items():
#         print(f"{word}: {count}")

# countWordFrequency()


##part 20
# def tempconverter():
#     print("Temperature Converter!!")
#     print("1. Celsius to Fahrenheit")
#     print("2. Fahrenheit to Celsius")

#     choice = input("Choose (1 or 2): ")

#     if choice == '1':
#         c = float(input("Enter temperature in Celsius: "))
#         f = (c * 9/5) + 32
#         print(f"{c}°C is equal to {f}°F.")

#     elif choice == '2':
#         f = float(input("Enter temperature in Fahrenheit: "))
#         c= (f - 32) * 5/9
#         print(f"{f}°F is equal to {c}°C.")

#     else:
#         print("Invalid choice!")

# tempconverter()