num=int(input("enter a no:"))
sum = 0
for i in range(1,num):

    if num%i ==0:

        sum+=num

if sum == num:

    print(f"{num} is perfect")

else:

    print("it is not perfect")