# # # # #
# # # # # #Greetings
# # # # # #name = input("enter name: ")
# # # # # #age = input("enter age: ")
# # # # # #print("greetings " + name + "and your age is " + age)
# # # # #
# # # # # #Data type identification
# # # # # getvalue = input("enter data ")
# # # # #
# # # # # try:
# # # # #     if int(getvalue):
# # # # #         getvalue = int(getvalue)
# # # # #         print(type(getvalue))
# # # # # except ValueError:
# # # # #     try:
# # # # #         if float(getvalue):
# # # # #             getvalue = float(getvalue)
# # # # #             print(type(getvalue))
# # # # #     except ValueError:
# # # # #         if str(getvalue):
# # # # #             print(type(getvalue))
# # # # #
# # # # #
# # # # #List Operations
# # # # array = ['a','b','c','a','b','c','a','b','c']
# # # # array.append("c")
# # # # array.remove('c')
# # # # for item in array:
# # # #     print(item.upper())
# # #
# # # #Tuple Unpacking
# # # mytuple = ("good","bad","best")
# # # var1 = mytuple[0]
# # # var2 = mytuple[1]
# # # print(var1)
# # # print(var2)
# #
# #
# # #Dictionary Management
# # mydict = { "john":"A" , "cena":"D","mic":"B","johl":"C","jane":"B" }
# # for item in mydict:
# #     print(item)
# #     print(mydict[item])
#
# #Set Operations
# list1 = [4,7,8,2]
# list2 = [5,4,3,2,9,7]
#
# set1 = set()
# set2 = set()
# for item in list1:
#     set1.add(item)
# for item in list2:
#     set2.add(item)
# print("Union:" , set1|set2)
# print("Intersection: " , set1 &set2)
# print("Dofference: ", set1 - set2)

#Number Checker
# value = input("enter int value : ")
# value = int(value)
# if value > 0:
#     if value % 2 == 0:
#         print("positive")
#         print("even")
#     else:
#         print("positive")
#         print("odd")
# elif value < 0:
#     if value % 2 == 0:
#         print("negitive")
#         print("even")
#     else:
#         print("negitive")
#         print("odd")
# else:
#     print("0")
#     print("even")

#FizzBuzz
# for x in range(1,50):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x & 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")

#Factorial Calculator
# def cal_factorial(val):
#     ans = val
#     while val>1:
#         val = val - 1
#         print(val)
#         ans = ans * val
#     print(f"Factorial {ans}")
#
# cal_factorial(5)

#Prime Number Checker

# value = input("enter int value : ")
# value = int(value)
#
# check  = True
# for x in range(2,int(value/2)):
#     if value % x == 0:
#         check = False
# if check:
#     print("prime number")
# else:
#     print("not prime")

#List Comprehension

# def squares(list):
#     ans = [x * x for x in list]
#     print(ans)
#
# l = [5,4,3,2,9,7]
# squares(l)

#Merge Dictionaries
# dict1 = { "john":"A" , "cena":"D","mic":"B","johl":"C","jane":"B" }
# dict2 = { "john":"E" , "kera":"D","joly":"C","bane":"B" }
#
# dict1.update(dict2)
# print(dict1)

#Remove Duplicates
# mylist = [5,4,3,2,9,2,7,5,3]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

#Palindrome Checker
# string = "abbbba"
# x =  lambda s : string == s[::-1]
#
# if x(string):
#     print("palindrome")
# else:
#     print("not a palindrome")

#Fibonacci
# num = input("enter number for fibonacci: ")
# firstnum= 0
# secondnum = 1
# ans = 0
# print(firstnum)
# print(secondnum)
# for x in range(0,int(num) ):
#     ans = firstnum + secondnum
#     print(ans)
#     firstnum = secondnum
#     secondnum = ans
#

#Average Calculator

# print("enter total no of values")
# user_input = int(input())
# number_list = []
# print("enter values")
# for i in range(user_input):
#     number_list.append(int(input()))
# sum = 0
# count = 0
# for x in number_list:
#     sum = sum + x
#     count = count + 1
# average = sum/count
# print("Average: ")
# print(average)


#Multiplication Table
# for x in range(1,11):
#     for y in range(1,11):
#         mul = x * y
#         print(f"{x} x {y} = {mul}")
#     print("\n")

#User Registration System
# credentials = { "john":"123" , "sigma":"42"}
# name = input("enter name: ")
# password = input("enter password: ")
# if credentials.get(name):
#     if password == credentials[name]:
#         print("Logged In")
#     else:
#         print("wrong username/password")
# else:
#     print("wrong username/password")

#Counting words from Dictionary
# string = input("enter: ")
# list = string.split()
# dict = {}
# for item in list:
#     dict[item] = 0
# for item in list:
#     dict[item] = dict[item] + 1
#
# print(dict)

#Temperature Converter
# check = int(input("enter 0 for celsius to fahrenheit - enter 1 for fahrenheit to celsius "))
# value = int(input("enter temperature value "))
#
# if check == 0:
#     ans = (value*9/5) + 32
#     print(f"{ans} fahrenheit")
# elif check == 1:
#     ans = (value-32) * (5/9)
#     print(f"{ans} celsius")
