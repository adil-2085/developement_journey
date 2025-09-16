# metords are 


'''
methords are three tupes

* instance methord -bounded with object,first parameter self,no decorator,called 
* class methord - bounded with class ,first parameter cls,decorator @classmethord
* static methord - bounded with none,first parameter none, decorator @staticmethord


'''

class Employee:

    # constructor
    def __init__(self,id,name):
        
        self.id=id

        self.name=name

    # instance methord

    def display_employee(self):

        print(self.id,self.name)


    # class methord

    @classmethod
    def class_demo(cls):
       
       print('inside class methord')


    # static methord

    @staticmethod
    def static_demo():

        print('inside static methord')
       
Employee_instance = Employee(100,'hai')

Employee_instance.display_employee() #instance methord calling

Employee.class_demo()   #class methord calling

Employee.static_demo()  #static methord calling



