user_input = input("Enter integer: ")


def is_num(s):
    if s.startswith('-'):
        s = s[1:]
    return s.isdigit()


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True


if not is_num(user_input):
    print("Enter integer")
    exit(1)
else:
    user_input = int(user_input)
    print("Is prime?", is_prime(user_input))
