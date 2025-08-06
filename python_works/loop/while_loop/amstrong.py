number = 153

digit_count = len(str(number))

armstrong = 0

while(number != 0):

    last_digit = number%10

    armstrong += (last_digit ** digit_count)

    number//10

print('armstrong')