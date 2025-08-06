
number=int(input("Enter a no: "))

is_primary=True

for i in range(2,number):

    if number%i==0:

        is_primary=False

        break

result="prime number" if is_primary == True else "not a prime no"

print(result)