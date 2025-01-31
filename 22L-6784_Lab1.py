# ------------------------------------------------------
# Question 1 - done
# name = input("Please enter your name: ")
# print(f"Hello {name}, nice to have you here!")
# ------------------------------------------------------





# ------------------------------------------------------
# Question 2 - done
data = input ("Please enter an input: ")
try: 
    data = int(data)
    print(type(data))
    
except: 
    try: 
        data = float(data)
        print(type(data))
    
    except:
        print(type(data))
# ------------------------------------------------------




# ------------------------------------------------------
# Question 3 - done
# names_list = ["abc", "def", "ghi"]
#     #modifying elements
# names_list[1] = "hello"
#     #removing elements
# names_list.remove("hello")
#     #printing in uppercase
# for name in names_list: 
#     print(name.capitalize())

# print(names_list)
# ------------------------------------------------------



# ------------------------------------------------------
# Question 4: Tuple Unpacking - done
name_tuple = ("Hello", "I", "Am", "A", "Tuple")
var1 = name_tuple[0]
var2 = name_tuple[1]

print(f"First element: {var1}")
print(f"Second element: {var2}")
# ------------------------------------------------------



# ------------------------------------------------------
# Question 5: Dictionary management -done
# student_grades_dictionary = {"Kainat": "A", "Nasir": "B"}
# print(student_grades_dictionary)
# print(type(student_grades_dictionary))
# ------------------------------------------------------



# ------------------------------------------------------
# Question 6: Set Operations - done
list1 = input("Please enter a list of numbers seperate by space: ").split()
set1 = set(list1)

list2 = input("Please enter a 2nd list of numbers seperate by space: ").split()
set2 = set(list2)



print(set1 - set2)    # diff  
print(set1 | set2)    # union 
print(set1 & set2)    # intersction
# ------------------------------------------------------




# ------------------------------------------------------
# Question 7: Conditional Statements: Number Checker - done
num = int(input("Please enter a number: "))
if (num % 2 == 0):
    print("Number is even")
    
else:
    print("Number is odd.")
    
if(num > 0):
    print("Number is positive")
elif (num < 0):
    print("Number is negative")
else: 
    print("Number is 0.")
# ------------------------------------------------------



# ------------------------------------------------------
# Question 8: FizzBuzz - done
# n = 1
# while (n<=50):
#     if (n%3 == 0 and n%5 ==0):
#         print("FizzBuzz")
#     elif (n%3 == 0):
#         print("Fizz")
#     elif (n%5 == 0):
#         print("Buzz")
#     else:
#         print(n)
#     n = n+1
# ------------------------------------------------------





# ------------------------------------------------------
# Question 9: Function: Factorial Calculator -done 
# def factorial(num):
#     if num < 0:
#         print("Factorial cannot be computed for a negative number")
#     if num == 0:
#         return 1
        
#     ans = 1
#     n = num 
#     while n>1:
#         ans = ans*n
#         n = n-1
#     return ans
    
# print(factorial (5))
# ------------------------------------------------------


# ------------------------------------------------------
# Question 10: Prime Number Checker - done
# def check_prime(num):
#     if(num ==1):
#         print("This number is neither prime nor consonant")
#     n = 2
#     while (n <= num/2):
#         if(num % n == 0):
#             print("The given number is not prime")
#             return
#         n = n+1
#     print("The given number is prime")
#     return

# number = int(input("Please enter a number: "))
# check_prime(number)
# ------------------------------------------------------



# ------------------------------------------------------
# Question 11: List Comprehension: Squares
def square(num): 
    new_num = []
    for i in num: 
        new_num.append(i*i)
        
    return new_num

num = [1, 2, 3]
print(square(num))
# ------------------------------------------------------



# ------------------------------------------------------
# Question 12: Merge Dictionaries
dict1 = {'a': 1, 'b': 2, 'c':3}
dict2 = {'b': 6, 'c':100, 'd': 8}

dict1.update(dict2)

print(dict1)
# ------------------------------------------------------



# ------------------------------------------------------
# Question 13:Remove Duplicates from a List
def remove_dup(num): 
    exists = []
    new_num = []
    for i in num: 
        if i in exists:
            continue
        else:
            new_num.append(i)
            exists.append(i)
        
    return new_num

num = [1, 2, 2, 3, 3, 3, 2]
print(remove_dup(num))
# ------------------------------------------------------




# ------------------------------------------------------
# Question 14: Palindrome Checker
palindrome = lambda s: s==s[::-1]
 
string = input("Please enter a string: ")
new_s = string.split()  #removing spaces
new_s_2 = ''.join(new_s)    #turning it back to a string
new_s_2 = new_s_2.lower()   


if palindrome(new_s_2) == True:
    print(f"{string} is a palindrome")

else:
    print(f"{string} is a not palindrome")
# ------------------------------------------------------




# ------------------------------------------------------
# Question 15: Fibonacci Sequence Generator
def fibonacci(n):
    sequence = []
    a = 0
    b = 1
    i = 0 #itertor
    
    while(i<n):
        sequence.append(a)
        c = a
        a = b
        b = b+c
        
        i +=1
    
    return sequence
    
    
n = int(input("Please enter the number of values you want in the fibonacci sequence: "))
seq = fibonacci(n)
print(seq)
# ------------------------------------------------------


# ------------------------------------------------------
# Question 16: Average Calculator with Validation
def is_valid(n):
    for i in n:
        try:
            i = int(i)
            
        except:
            return False
    
    return True
        


def avg(num):
    sum = 0
    total = 0
    
    for i in num: 
        sum += i
        total +=1
        i+=1
    
    if (total == 0):
        print("Division by zero error")
        return 0
    return sum/total
    
    
while True:    
    n = input("Please enter a series of numbers seperated by space: ").split()
    if is_valid(n):
        for i in range(len(n)): 
            n[i] = int(n[i])
        print(avg(n))
        break
    
    else: 
        print("invalid values entered")
        continue
# ------------------------------------------------------




# ------------------------------------------------------
# Question 17: Nested Loops: Multiplication Table
num = 1

while(num <= 10):
    i = 1
    while(i <=10):
        print(f"{num} * {i} = {num*i}")
        i+=1
        
    print("------------------------")
    num +=1
# ------------------------------------------------------






# ------------------------------------------------------
# Question 18: User Registration System
user_info = {}
num = 1

while(num!= 'e'):
    username = input("Username: ")
    password = input("Password: ")
    
    if(username == '' or password == ''):
        print("Invalid credentials. Pls try again")
        continue
    
    if username in user_info:
        if user_info[username] == password:
            print("You are logged in.\n")
    
    else:
        print(f"Thank you for signing up {username}")
        user_info[username] = password
        
    
    num = input("Press e to terminate: ")

# ------------------------------------------------------





# ------------------------------------------------------
# Question 19: Counting Elements with a Dictionary
words_list = ["Hello", "Hello", "K", "K", "Hello", "a"]
freq = {}
for w in words_list: 
    if w in freq:
        freq[w] +=1
        
    else:
        freq[w] = 1
        
print(freq)
# ------------------------------------------------------
   
    

# ------------------------------------------------------
# Question 20:
def temp():
    option = int(input("press 1 for C to F and 2 for F to C: "))
    
    if option == 1:
        t = float(input("Enter temperature in C: "))
        f = (t * 9/5) + 32
        print(f)
        
    elif option ==2:
        t = float(input("Enter temperature in F: "))
        c = (t - 32) * 5/9
        print(c)
        
    return 

temp()
# ------------------------------------------------------