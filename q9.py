
def factorial(num):
    fact=1
    while num!=0:
        fact=fact*num
        num=num-1
    print("factorial is as ",fact)
#factorial
num=int(input("enter the number for which you want to calculate factorial"))

factorial(num)