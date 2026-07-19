class user:
    id=0
    name=""
    dept=""

    def __init__(self,id,name,dept):
        self.id=id
        self.name=name
        self.dept=dept

    def dept_coll(self):
        print("Steffi is very good",self.name)

user1=user(1,"jeberson","Cse")
print(user1.id,"\n",user1.name,"\n",user1.dept)
user1.dept_coll()


