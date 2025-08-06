count=0

number=int(input("Enter the no:"))

for i in str(number):
    digit=number%10

    count+=1

    number//10
    

print(count)

