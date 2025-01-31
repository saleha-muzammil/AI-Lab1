num1 = input("Enter a Number : ")
num=int(num1)
if(num < 0):
    print("Number is Negative.")
elif(num > 0):
    print("Number is Positive.")
elif(num % 2 == 0):
    print("Number is Even.")
elif(num % 2 != 0):
    print("Number is Odd.")