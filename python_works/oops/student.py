class Student:

    id:int

    student_name:str

    course:str

    blood_type:str

    def set_student(self,id,student_name,course,blood_type):

        self.id = id

        self.student_name = student_name

        self.course = course

        self.blood_type = blood_type

    def display_student(self):

        print(self.id,self.student_name,self.course,self.blood_type)



student_instance1 = Student()

student_instance1.set_student(100,'brigin','bca','b+')

student_instance1.display_student()
    