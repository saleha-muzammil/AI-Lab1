
users = {}

def register():
    global users

    print("Enter a username:")
    username = str(input())
    print("Enter a password:")
    password = str(input())
    users[username] = password
    print("User registered successfully.")

def login():
    global users

    print("Enter your username:")
    username = str(input())
    print("Enter your password:")
    password = str(input())

    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Login failed.")


done = False

while not done:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit\n")

    try:
        choice = int(input())
    except ValueError:
        print("Invalid choice. Please try again.")
        continue

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        done = True
    else:
        print("Invalid choice. Please try again.")