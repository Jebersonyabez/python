userdata =[
    {"username":"jeberson",
     "password":"jeb"},
     {
         "username":"yabez",
         "password":"yab"
     },
     {
         "username":"steffi",
         "password":"stef"
     }
]

username=input("Enter the username:")
password=input("Enter the password:")

islogin=False

for i in range(len(userdata)):
    user=userdata[i]
    if(user["username"]==username and user["password"] == password):
        islogin=True

if(islogin):
    print("Login successfully")
else:
    print("Login failed.Try again later")