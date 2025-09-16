class Student():

    school_name='ABC'

    def __init__(self,roll,name,total):

        self.roll=roll

        self.name = name

        self.total = total

    @classmethod

    def update_school_name(cls,new_name):

        cls.school_name=new_name

        print(cls.school_name)

    @staticmethod

    def is_pass(total):

        print(True if total>140 else False)

student_instance1 = Student(123,'aromal',138)

student_instance2 = Student(124,'brijin',141)


Student.update_school_name('KVVS')

Student.is_pass(student_instance1.total)

Student.is_pass(student_instance2.total)
