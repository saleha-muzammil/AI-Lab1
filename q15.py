user_input = input("Enter integer: ")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if not user_input.isnumeric():
    print("Enter int")
else:
    user_input = int(user_input)
    print(f"Fibonacci: {fibonacci(user_input)}")
