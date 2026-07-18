class users:
    id=0
    name=""
    city=""
    Mobileno=""

    def __init__(self,id,name,city,mobileno):
        self.id=id
        self.name=name
        self.city=city
        self.Mobileno=mobileno

    def printobject(self):
        print(self.id)
        print(self.city)

# same order la than kudukanum      
user1=users(1,"jeberson","chennai","12345678")
user2=users(2,"yabez","Thoothukudi","123456789")

user1.printobject()
print(user1.name)
print(user2.name)
