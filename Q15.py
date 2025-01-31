n = 10

def fibo_generator(n):
    if(n == 1):
        print(0)
        return
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    next_number = num2  
    count = 2

    while count < n:
        print(next_number)
        count = count + 1
        num1 = num2
        num2 = next_number
        next_number = num1 + num2

fibo_generator(n)