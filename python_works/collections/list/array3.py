# q1
# arr=[153,151,1634,1771,2332]

# generate three new list palindrome_list and armstrong_list,prime_number


arr=[153,151,1634,1771,2332]

pallindrome_list=[]

armstrong_list=[]

prime_number_list=[]


for i in arr:

    rev=0
    number=i
    for j in range(len(str(number))):

        rem=number%10

        rev=rev*10+rem

        number=number//10

    if rev == i:

        pallindrome_list.append(i)




    div_count = 0

    for j in range(2,i):

        if i%j == 0:

            div_count += 1
    
    if div_count==0:

        prime_number_list.append(i)



    digit_count = len(str(i))

    armstrong = 0

    number=i

    while(number != 0):

        last_digit = number%10

        armstrong += (last_digit ** digit_count)

        number=number//10

    if armstrong==i:

        armstrong_list.append(i)

print(f"pallindrome:{pallindrome_list}\narmstrong:{armstrong_list}\nprime:{prime_number_list}")





# number = 153

# digit_count = len(str(number))

# armstrong = 0

# while(number != 0):

#     last_digit = number%10

#     armstrong += (last_digit ** digit_count)

#     number=number//10

# print('armstrong')