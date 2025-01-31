# Dictionary to store user credentials
user_database = {}

def register():
    username = input("Enter a new username: ")
    if username in user_database:
        print("Username already exists.")
        return
    password = input("Enter a new password: ")
    user_database[username] = password
    print("Registration successful!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_database.get(username) == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")


def userRegistrationSystem():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    userRegistrationSystem()