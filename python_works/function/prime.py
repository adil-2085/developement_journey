def is_prime(num):

    divisible = 2

    for i in range(1,num+1):

        if num%i == 0:

            divisible += 1

    if divisible == 2:

        return True
    else:
        return False
    
print(is_prime(4))