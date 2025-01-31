
users = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users:
        print("Username already exists. Please try again.")
        register()
    else:
        users[username] = password
        print("Registration successful. Please login.")
        login()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Login failed. Please try again.")
        login()



register()