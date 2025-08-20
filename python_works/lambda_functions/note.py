

# lambda funtion  --  short one line function without name : lambda funtion(anonimous=>without name)


# syntax :       

# lambda parameter1,parameter2:expression



sum = lambda num1,num2:num1+num2

print(sum(100,200))


last_digit_max = lambda num1,num2:num1 if num1 % 10 > num2 % 10 else  num2

print(last_digit_max(235,146))


positive = lambda num1:'positive' if num1 > 0 else  'negative'

print(positive(1))