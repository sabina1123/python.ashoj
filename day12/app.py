#register
#login agadi tapai register
#register username unique
#show all the user(user must be login)

users = []


def register():

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user:
        print("Username already exists")
    else:
        user[username] = password
        print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user and user[username] == password:
        print("Login successful. Welcome, " + username + "!")
    else:
        print("Invalid username or password. Please try again.")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
#katana
#rank hacker