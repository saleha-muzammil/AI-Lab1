integer_no = 5
def calc_factorial(integer_no):
    if(integer_no == 0):
        return 1
    else:
        i = 1
        factorial = 1
        
        for i in range(1, integer_no+1):
            factorial = factorial * i

        return factorial

factorial = calc_factorial(integer_no)
print("Factorial: ", factorial)