def odd_even_count(num):
    odd_count=0
    even_count=0
    while num>0:
        digit=num%10

        if digit%2==0:

            even_count+=1
        elif digit%2!=0:

            odd_count+=1

        num=num//10

    print(f"even count = {even_count} odd count={odd_count}")

print(odd_even_count(12345))
