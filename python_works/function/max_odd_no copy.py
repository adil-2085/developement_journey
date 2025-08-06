def max_odd_no(num):

    for i in range(len(str(num))):

        digit = num%10

        if digit %2!=0:

            print(num)
            
            break

        num = num//10

num=int(input("enter a no:"))

max_odd_no(num)