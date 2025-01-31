name = input("Enter name: ")
age = input("Enter age: ")

if not age.isnumeric():
    print("Enter age correctly")
else:
    print(f"Welcome {name}, your age is {age}")