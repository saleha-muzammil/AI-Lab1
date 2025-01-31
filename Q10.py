number = int(input("Enter a number: "))

def check_prime(number): # not considering negative nos
    if number == 0 or number == 1: 
        return False
    i = 2
    while(i <= number/2):
        if number % i == 0:
            return False
        i = i + 1
        
    return True

if check_prime(number) == True:
    print("Number is prime.")
else:
    print("Number is not prime.")