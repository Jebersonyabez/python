userdata=[
    {
        "username":"jeberson",
        "password":"jeb"
    },
    {
        "username":"yabez",
        "password":"yab"
    },
    {
        "username":"steffi",
        "password":"stef"
    }
]

def login():
    username=input("Enter the username:")
    password=input("Enter the password:")

    islogin=False

    for user in userdata:
        if(user["username"]==username and user["password"]==password):
            islogin=True
       
    if(islogin):
        print("Login successfull")
    else:
        action=input("password wrong try again or resetpassword 1.yes or 2.no")
        if(action=="yes"):
             resetpassword()
        else:
            print("login fail.Try again later")

def resetpassword():
        username=input("Enter the user name:")
        password=input("Enter the password:")
        re_enterpassword=input("Enter the password reenter:")
        print("login Succesfully")

option=input("Enter the option to perform 1.login 2.resetpassword")

if(option=="1"):
    login()
elif(option=="2"):
    resetpassword() 
else:
     print("Invalid input")
