total_bottles = 10

while total_bottles > 0:

    print(f"there are {total_bottles} bottles are in total")

    ans = int(input("if one bottle accedently falls then how mwny remains : "))

    if ans == total_bottles -1 :

        print(f"there is {total_bottles-1} bottles")

        total_bottles -= 1

    else:

        print("wrong answer try again")

