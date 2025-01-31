def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


user_input = input("Enter input: ")

if user_input.isnumeric():
    print(f"Factorial is {factorial(int(user_input))}")
