user_input = input("Enter integer: ")


def is_num(s):
    if s.startswith('-'):
        s = s[1:]
    return s.isdigit()


if not is_num(user_input):
    print("Enter integer")
    exit(1)
else:
    user_input = int(user_input)

if user_input == 0:
    print("Num is 0")
else:
    if user_input > 0:
        print("Num is positive")
    else:
        print("Num is negative")

    print(f"Num is {'Even' if user_input % 2 == 0 else 'Odd'}")
