# q4 
# numbers=[151,152,153,1634,8891,345,678]
# display armstrong numbers from list


numbers=[151,152,153,1634,8891,345,678]

for number in numbers:

    digit_count = len(str(number))

    armstrong = 0

    temp=number

    while(number != 0):

        last_digit = number%10

        armstrong += (last_digit ** digit_count)

        number//10

    print(armstrong)

    if armstrong==temp:

        print(temp)