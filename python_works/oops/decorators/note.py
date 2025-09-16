''' 
decorators are functions that changes the behaviour of another function without changing definition


deorator doen't affects the definition of a function
it adds new feature to a function without modifying the function

it is reusable ,





it is three types 

* bult-in
    
eg:
@classmethord

* custom decorator - defined by user
* property - we can call methords in property calling way

    eg:

    student.get_name



'''


# eg

def swap_decorator(fn):

    def inner_func(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return inner_func

@swap_decorator
def sub(n1,n2):
    return n1-n2
@swap_decorator
def div(n1,n2):
    return n1/n2
print(sub(5,10)) 
print(div(5,10))


