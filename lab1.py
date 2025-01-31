# name=input("Enter name: ")
# age=input("Enter age: ")
# print("Your name is "+ name+" your age "+age)






# #q2

# def data_type():
#     U_input=input("Enter input: ")
#     try:
#         if (int(U_input)):
#             print("int type")
#     except ValueError as err:
#         try:    
#             if (float(U_input)):
#                 print("float type")
#         except ValueError as e:        
#             pass

#             if(U_input.lower()=='true' or U_input.lower()=='false'):    
#                 print("Boolean")
#             else:
#                 print("String")    
# data_type()






#q3

# def ListOP():
#     def_list=['Hello','feeling','well','.']
#     u_input=input("Enter user input: ")
#     print("Initial list:\n")

#     for i in def_list:
#         print(i.upper())

#     def_list.append(u_input) 
#     print("Modified list:\n")
#     for i in def_list:
#         print(i.upper())

#     def_list.remove(u_input)    
#     print("Removed list:\n")
#     for i in def_list:
#         print(i.upper())

# ListOP()





# #q4

# def Q4():
#     tp=(1,2,3)
#     (v1,v2,v3)=tp
#     #Unpacking them as v1 and v2
#     print(v1)
#     print(v2)

# Q4()








#q no.5

# def Dictionary():
#     student={
#         "Mujtaba":"A",
#         "Aun":"A+",
#         "Ahmed":"F",
#         "Adil":"A-",
#         "Ghulam":"B+"
#     }
#     print(student)

# Dictionary()









#Q6

# def setOP():
#     l1=[]
#     l2=[]
#     print("Enter the integer values for list_1 and enter exit to finish\n")
#     u_input=input("Enter value: ")
#     while(u_input!='exit'):
#         if(u_input!='exit' and int(u_input)):
#             l1.append(u_input)
#         u_input=input("Enter value: ") 

#     print("\nEnter the integer values for list_2 and enter exit to finish\n")

#     u_input1=input("Enter value: ") 
#     while(u_input1!='exit'):
#         if(u_input1!='exit' and int(u_input1)):
#             l2.append(u_input1)
#         u_input1=input("Enter value: ")     

#     myset1=set(l1)
#     myset2=set(l2)

#     print(myset1)
#     print(myset2)

   
#     print("UNION:",myset1|myset2)
#     print("INTERSECTION:",myset1&myset2)
#     print("Difference:",myset1-myset2)

# setOP()            









# def condition_check():
#     u_input=input("Enter value: ")
#     if(int(u_input)):
#         num=int(u_input)
#         if(num>0):
#             if(num%2==0):
#                 print("Positive and even")
#             elif(num%2!=0):
#                 print("Positive and odd")
#         elif(num<0):
#             if(num%2==0):
#                 print("Negative and even")
#             elif(num%2!=0):
#                 print("Negative and odd")
#         else:
#             print("Zero")        
#     else:
#         print("Not an integer")

# condition_check()









# def fizzbuzz():
#     for i in range(1,51):
#         if(int(i)%3==0 and int(i)%5==0):
#             print("FIZZBUZZ")
#         elif(int(i)%3==0):
#             print("Fizz")
#         elif(int(i)%5==0):
#             print("BUZZ")        
#         else:
#             print(i)
# fizzbuzz()








# def fact():
#     num=input("Enter value: ")
    
#     num=int(num)
#     if(num<0):
#         print("neg number")
#         return
#     ans=1
#     if (num==0):
#         print("1")
#     else:
#         for i in range(1,num+1):
#             ans*=i
#         print(ans)        
# fact()








# def prime():
#     num=input("Enter number ")
#     num=int(num)
#     half=int(num/2)
#     for i in range(1,half+1):
#         if (num%i)==0:
#             print("Composite")

#     print("Prime")

# prime()








# def square():
#     l1=[]
#     print("Enter list and type exit to finish:")
#     u_input=input("Enter value: ")
#     while(u_input!='exit'):
#         if(u_input!='exit' and int(u_input)):
#             l1.append(u_input)
#         u_input=input("Enter value: ") 
    
    
#     for i in l1:
#         print(int(i)*int(i))
# square()







# def MergeDictionary():
#     student1={
#         "Mujtaba":"A",
#         "Aun":"A+",
#         "Ahmed":"F",
#         "Adil":"A-",
#         "Ghulam":"B+"
#     }
#     student2={
#         "Ali":"A",
#         "Asim":"A+",
#         "Ahmed":"F",
#         "Adil":"A-",
#         "Hassaan":"B+"
#     }

#     student1.update(student2)
#     print(student1)
    
# MergeDictionary()











# def removedup():
#     mylist = [1,2,2,3,4]
#     mylist = list(dict.fromkeys(mylist))
#     print(mylist)

# removedup()






# def palindrome():
#     val1="1221221"    
#     val2="2215672"

#     is_pal=lambda x:(x)==(x)[::-1]
#     if(is_pal(val1)):
#         print("Is palindrome")
#     else:
#         print("Not a palindrome")

# palindrome()    








# def fibonacci():
#     num=input("Enter number to generate fibonacci series\n")
#     f=0
#     s=1
#     if(int(num)):
#         num=int(num)
#         print("0")
#         print("1")
#         for i in range(1,num-1):
#             ans=f+s
#             f=s
#             s=ans
#             print(ans)
#     else:
#         print("Not a valid positive int")

# fibonacci()









# def avg():
#     l1=[]
#     num=0
#     print("Enter list of numbers and type exit to finish:")
#     u_input=input("Enter value: ")
#     while(u_input!='exit'):
#         if(u_input!='exit' and int(u_input)):
#             l1.append(u_input)
#         u_input=input("Enter value: ") 

#     for i in range(0,len(l1)+1):
#         num=int(i)
#         num+=num

#     print("AVG=",num/len(l1))        
# avg()








# def multable():
#     for i in range(1,11):
#         for j in range(1,11):
#             print(i," x ",j," = ",i*j )

# multable()












# REGISTERATION USING DICTIONARY
# users = {}  
# def register():
#     username = input("Enter a username: ")
#     if username in users:
#         print("Username already exists. Choose a different one.")
#         return
#     password = input("Enter a password: ")
#     users[username] = password
#     print("Registration successful!")

# def login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if users.get(username) == password:
#         print("Login successful! Welcome,", username)
#     else:
#         print("Invalid username or password.")

# def display_users():
#     if users:
#         print("Registered Users:")
#         for user in users:
#             print(user)
#     else:
#         print("No registered users yet.")

# def main():
#     while True:
#         print("\n1. Register\n2. Login\n3. Display Users\n4. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             register()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             display_users()
#         elif choice == '4':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()











# def word_frequency():
#     words = input("Enter words separated by spaces: ").split()  
#     word_count = {
#         "Ali": "A",
#         "Asim": "A+",
#         "Ahmed": "F",
#         "Adil": "A-",
#         "Hassaan": "B+",
#         "Hamza": "A",
#         "Zain": "B+",
#         "Bilal": "C",
#         "Saad": "B",
#         "Usman": "A-"
#     }

#     selected_count = {}
#     for word in words:
#         word = word.capitalize() 
#         if word in word_count:
#             selected_count[word] = selected_count.get(word, 0) + 1 
#     return selected_count
# word_freq = word_frequency()
# print("\nWord Occurrence in Dictionary:")
# for word, count in word_freq.items():
#     print(f"{word}: {count}")













# def temperature_converter():
#     choice = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

#     if choice == "C":
#         celsius = float(input("Enter temperature in Celsius: "))
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

#     elif choice == "F":
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         celsius = (fahrenheit - 32) * 5/9
#         print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

#     else:
#         print("Invalid choice! Please enter 'C' or 'F'.")


# temperature_converter()












