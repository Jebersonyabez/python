class department:
    id=0
    name_of_students=""
    dept=""
    age=0

    def __init__(self,id_of_the_student,student_dept,student_name,student_age):
        self.id=id_of_the_student
        self.name_of_students=student_name
        self.dept=student_dept
        self.__age=student_age #__ kuduthu kudutha private la varum 

    def __del__(self):
        print("This is the deconstructor:",self) #str nu kudukalana hexa value la self print agum 
    
    def __str__(self):
        return(self.name_of_students) #Ethu la return nu than kudukanum 
    
    #getter 
    def get_agee(self):
        return self.__age #ethukuduthu value va print pannalam seperate ta value function use panni 
    
    #setter
    def set_agee(self,age):
        self.__age=age #ethu use panni private la vachha value ku value change pannalam 
    

stu1=department(11,"CSE","Jeberson",20)
print(stu1)
print(stu1.id,stu1.name_of_students,stu1.dept,stu1.get_agee())


stu1.set_agee(30)
print(stu1.get_agee())

        