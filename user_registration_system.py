USERS = [
    {"username": "jose", "password": "123"},
    {"username": "malik", "password": "123"},
    {"username": "usman", "password": "123"},
    {"username": "john", "password": "123"},
]

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in USERS:
        if user["username"] == username and user["password"] == password:
            print("You are logged in!")
            break
    else:
        print("Invalid credentials!")


def main():
    global USERS
    print("Welcome to the user registration system.")
    login_user()
        
if __name__ == "__main__":
    main()