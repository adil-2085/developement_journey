# q5


# display palindromic numbers from list


numbers =[11,12,13,33,131,343,12321,1234]


for i in numbers:

    rev=0
    number=i
    for j in range(len(str(number))):

        rem=number%10

        rev=rev*10+rem

        number=number//10

    if rev == i:

        print(i)

    





