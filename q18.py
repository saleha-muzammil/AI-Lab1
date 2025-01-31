users = {}


def register():
    user = input("Enter username: ")
    pass_ = input("Enter password: ")
    users[user] = pass_


def login():
    user = input("Enter username: ")
    pass_ = input("Enter password: ")
    print("Login done"
          if users.get(user) == pass_
          else "Login not done")


print("Register:")
register()

print("Login:")
login()
