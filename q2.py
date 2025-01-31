user_input = input("Enter input: ")

if user_input.isnumeric():
    user_input = int(user_input)
    print(f"Integer: {user_input}")
elif "." in user_input and len(user_input.split('.')) == 2:
    spl = user_input.split(".")
    if spl[0].isnumeric() and (not spl[1] or spl[1].isnumeric()):
        user_input = float(user_input)
        print(f"Float: {user_input}")
    else:
        print(f"String: {user_input}")
else:
    print(f"String: {user_input}")


