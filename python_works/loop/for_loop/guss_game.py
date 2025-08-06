from random import randint

attemtt=0

target=randint(1,10)

while True:

    number=int(input("Enter a number"))

    attemtt+=1

    if number==target:

        print("Congratulations")

        print(f"your attempt is :{attemtt}")

        break