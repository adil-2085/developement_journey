
def abs_no(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    
    return wrapper

@abs_no
def add_number(num1,num2):

    print(num1+num2)

add_number(-5,9)