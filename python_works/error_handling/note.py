'''
try  -  doubtful code
except  -  handling code
finally  -  clean up procrssing
raise  -  custom error throw
assert  -  debugging


'''


num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))

try:
    div = num1 / num2
    
    print(div)
    
except:
    print("error occured")
    

print("send text msg to user phone")
print("send mail to user phone")