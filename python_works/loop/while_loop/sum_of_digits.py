sum=0

number=int(input("Enter the no:"))

while(number!=0):
    digit=number%10

    sum+=digit

    number//10

print(sum)
print("sum")
