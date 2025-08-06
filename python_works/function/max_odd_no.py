def max_odd_no(num):

    largest_odd = 0

    for i in range(len(str(num))):

        digit = num%10

        if digit %2!=0 and digit > largest_odd:

            largest_odd = digit

        num = num//10

    return largest_odd

num=int(input("enter a no:"))

print(max_odd_no(num))

