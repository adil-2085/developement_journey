def pallindrome(number):

    temp = number
    rev = 0

    for i in range(len(str(number))):

        rem = number%10

        rev = rev *10 + rem

        number = number//10

    if temp == rev:

        return True
    
    else:

        return False

print(pallindrome(1231))