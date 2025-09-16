num1 = int(input('enter the first no'))

num2 = int(input('enter the second no'))

try:
    print(num1/num2)

except Exception as e:

    print(e)

    num2=int(input('enter a valid no'))

    print(num1/num2)

finally:

    print('program finished')
