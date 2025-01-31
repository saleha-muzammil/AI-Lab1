
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

n = int(input("Enter a number: "))
print("The first",n,"numbers in the Fibonacci sequence are:")
fibonacci(n)
