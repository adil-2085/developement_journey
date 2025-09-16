def digit_count(num):

    if num == 0:

        return 0
    
    return num%10 + digit_count(num//10)

print (digit_count(456))

