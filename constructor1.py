class department:
    id=0
    name_of_students=""
    dept=""
    age=0

    def __init__(self,id_of_the_student,student_dept,student_name,student_age):
        self.id=id_of_the_student
        self.name_of_students=student_name
        self.dept=student_dept
        self.age=student_age

    def __del__(self):
        print("This is the deconstructor:",self) #str nu kudukalana hexa value la self print agum 
    
    def __str__(self):
        return(self.name_of_students) #Ethu la return nu than kudukanum 

stu1=department(11,"CSE","Jeberson","20")
print(stu1)
print(stu1.id,stu1.name_of_students,stu1.dept,stu1.age)

        