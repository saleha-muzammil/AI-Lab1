##q1

# name=input("enter your name ")
# age = input("enter your age ")
# print("welcome"+name+"your age is "+ age)




#q2

# def detect_data_type(input):
#     try:
#         inttt = int(input)
#         print("value is integer", inttt)
#     except ValueError:
#         try:
#             floatt= float(input)
#             print("value is a float", floatt)
#         except ValueError:
#             print("value is a string ", input)

# if __name__ == "__main__":
#     input = input("Enter a value: ")
#     detect_data_type(input)
    

#q3


# listt = ["arham", "arham2", "arham3"]
# listt.append("laiba")  # Adding at end
# listt.insert(1, "kainat") 

# # Remove items from the list
# listt.remove("arham2") 
# last_fruit = listt.pop() 

# print("uppercase list: ")
# for item in listt:
#     print(item.upper())

#q4


#q5
# # dictionary 
# students = {
#     "arham": 85,
#     "laiba": 92,
#     "kainat": 78
# }

# # Print the dictionary
# print("Student Grades:")
# for name, grade in students.items():
#     print(f"{name}: {grade}")



#q6


# list1 = list(map(int, input("Enter first list : ").split()))
# list2 = list(map(int, input("Enter second list : ").split()))
# set1 = set(list1)
# set2 = set(list2)
# union_set = set1 | set2         
# intersection_set = set1 & set2   
# difference_set = set1 - set2     
# print(f"Union {union_set}")
# print(f"Intersection {intersection_set}")
# print(f"Difference Set1 - Set2 {difference_set}")



#q7

# number = int(input("Enter integer: "))
# if number > 0:
#     sign = "positive"
# elif number < 0:
#     sign = "negative"
# else:
#     sign = "zero"

# if number % 2 == 0:
#     evennn = "even"
# else:
#     evenn = "odd"

# # Print the results
# print(f"The number {number} is {sign} and {evenn}.")


#q8


# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



#q9

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# number = int(input("Enter a  integer: "))
# if number >= 0:
#     num= factorial(number)
#     print("The factorial is",num)
# else:
#     print("Please enter a positive nteger.")

#q10

# def is_prime(n):
#     if n < 2:
#         return False
       
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
    
#     return True

# number = int(input("Enter a number to check if it's prime: "))
# if is_prime(number):
#     print("is a prime number.")
# else:
#     print("is not a prime number.")



#q11

# def squares(numbers):
#     squared_numbers = []
#     for num in numbers:
#         squared_numbers.append(num ** 2)
#     return squared_numbers

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = squares(numbers)

# print(f"Original numbers: {numbers}")
# print(f"Squared numbers: {squared_numbers}")


# #q12

# def merge_dictionaries(dict1, dict2):
#     dict1.update(dict2)
#     return dict1

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'd': 5}

# merged_dict = merge_dictionaries(dict1, dict2)
# print("Merged Dictionary:", merged_dict)


#q13
# def removedup(numbers):
   
#     seen = []
#     newlist = []
#     for num in numbers:
#         if num not in seen:
#             newlist.append(num)
#             seen.append(num)
    
#     return newlist


# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
# newlist2 = removedup(numbers)

# print(f"Original list {numbers}")
# print(f"List without duplicates {newlist2}")




#q14

# def palindromee(inp):
#     inp = inp.replace(" ", "").lower()
#     for i in range(len(inp) // 2):
#         if inp[i] != inp[-(i + 1)]:
#             return False
    
#     return True


# inputt = input("Enter a string to check palindrome ")
# if palindromee(inputt):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# #q14 using lambda
# def is_palindrome(s):
 
#     clean_string = lambda s: ''.join(s.split()).lower()  
#     return clean_string(s) == clean_string(s)[::-1]

# # Test the function with an example
# input_string = input("Enter a string to check if it's a palindrome: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


#q15

# def fibonnacci(n):

#     fib= []
    
   
#     a, b = 0, 1
#     for i in range(n):
#         fib.append(a)
#         a, b = b, a + b 
    
#     return fib

# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fib_numbers = fibonnacci(n)
# print(f"The first {n} numbers in the Fibonacci sequence: {fib_numbers}")


#q16

# def calculate_average(numbers):
#     if numbers:  
#         return sum(numbers) / len(numbers)
#     else:
#         return 0 
# # Main program
# numbers=[1,2,3,4,5]
# average = calculate_average(numbers)
# print(f"The average of the entered numbers is: {average}")




#q17

# for i in range (1,11):
#     print("multiplication table of " , i )
#     for j in range(1,13):
#         print(i, "*" , j ,"=", i*j)






#q18


# users = {}

# def register():
#     print("---- Registration ----")
#     username = input("Enter a username: ")
#     if username in users:
#         print("Username already exists choose a different username.")
#     else:
#         password = input("Enter a password: ")
#         users[username] = password
#         print(username, "User successfully registered!")

# def login():
#     print("---- Login ----")
#     username = input("Enter your username: ")
    
#     if username in users:
#         password = input("Enter your password: ")

#         if users[username] == password:
#             print("Logged in" , username )
#         else:
#             print("Incorrect password. Please try again.")
#     else:
#         print("Username not found. Please register first.")

# def main():
#     while True:
#         print("\n---- Main Menu ----")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option 1/2/3: ")

#         if choice == '1':
#             register()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             print("exitted")
#             break
#         else:
#             print("Invalid option. Please choose 1, 2, or 3.")


# main()



#q19

# def count_word_frequency():
   
#     words = input("Enter a list of words separated by spaces: ").split()

#     wordcount = {}  ## dictionaryyyy 

#     # Loop through the list of words
#     for word in words:
#         word = word.lower()
        
#         if word in wordcount:
#             wordcount[word] += 1
#         else:
#             wordcount[word] = 1

#     # Print the word frequency
#     print("Word frequency:")
#     for word, count in wordcount.items():
#         print(f"{word}: {count}")

# # Run the function
# count_word_frequency()





#q20
def convert():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2  ")

    if choice == '1':
       
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}celciius is equal to {fahrenheit}°Farenheight")
    
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}farenheight is equal to {celsius}Celcius")
    
    else:
        print("Invalid choice")

# Run the function
convert()


