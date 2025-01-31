def generate_fibonacci(n):
   
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

 
    fib_sequence = [0, 1]

    
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence


try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
     
        fibonacci_sequence = generate_fibonacci(n)
        print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")