users=[
    {
        "username":"user",
        "password":"123"
    }
]
isLogin=False

def login(username,password):
    for user in users:
        if username ==user["username"] and password ==user["password"]:
            global isLogin
            isLogin=True
            return
        print("No credential match")

def checkLogin():
    if isLogin:
        print("User is logged in")
    else:
        print("user havenot  logged in yet")
while True:
    choice=int(input("""
             Enter any choices
             1.Press 1 to login
             2.press 2 to check if user logged in or not
                    """))
    if choice==1:
        username=input("Enter username:")
        password=input("Enter password:")
        login(username,password)
    else:
        checkLogin()