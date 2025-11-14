num = int(input("enter a no:"))

if num>0:

    ans=0

    temp = num

    while temp != 0:

        rem= temp%10

        ans += rem

        temp=temp//10


    if num%ans==0:

        print("It is harshad")

    else:

        print("It is not harshad")


else:

    print("it is not a harshad")


