def register_user(users):
    username = input("Enter a username: ")
   
    if username in users:
        print("Username already exists. Please choose a different one.")
        return
    
    password = input("Enter a password: ")
    
    
    users[username] = password
    print(f"User '{username}' registered successfully!")

def login_user(users):
    username = input("Enter your username: ")
    
  
    if username not in users:
        print("Username not found. Please register first.")
        return
    
    password = input("Enter your password: ")
    
    
    if users[username] == password:
        print(f"Welcome back, {username}!")
    else:
        print("Incorrect password. Please try again.")


users = {}  
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == '1':
        register_user(users)
    elif choice == '2':
        login_user(users)
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


