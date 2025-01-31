#write this code in function
def factorial(num):
    if(num>0):
        factorial=1
        for i in range(1,num+1):
            factorial=factorial*i
        return factorial
    else:
        return False
    
num=input("Enter a number: ")
num=int(num)
print("The factorial of",num,"is",factorial(num))