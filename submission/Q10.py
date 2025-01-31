

def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

num=input("Enter a number: ")
num=int(num)
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")