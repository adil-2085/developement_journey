number=int(input("Enter a no:"))

rev=0

for i in range(len(str(number))):
    rem=number%10

    rev=rev*10+rem

    number=number//10

print(rev)