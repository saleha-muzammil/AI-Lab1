def convert_temp():
    user_input = float(input("Enter int: "))
    unit = input("C or F: ").upper()
    print(user_input * 9 / 5 + 32 if unit == 'F' else (user_input - 32) * 5 / 9)


convert_temp()
