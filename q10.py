def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


try:
    user_number = int(input("Enter a number to check if it's prime: "))
    
    # Check if the number is prime
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
