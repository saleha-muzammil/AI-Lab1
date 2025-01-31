

def temp_convert():
    temp = input("Enter the temperature: ")
    unit = input("Enter the unit (C/F): ")
    if unit == 'C':
        f = (int(temp) * 9/5) + 32
        print(f"{temp}C is {f}F")
    elif unit == 'F':
        c = (int(temp) - 32) * 5/9
        print(f"{temp}F is {c}C")
    else:
        print("Invalid unit")

temp_convert()

