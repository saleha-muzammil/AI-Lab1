users = {}

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Invalid username or password.")

register()
login()