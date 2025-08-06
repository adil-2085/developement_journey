count=0

number=int(input("Enter the no:"))

while(number!=0):
    digit=number%10

    count+=1

    number//10

print(count)

