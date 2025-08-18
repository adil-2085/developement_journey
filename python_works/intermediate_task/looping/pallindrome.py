# - Reverse Number and Check Palindrome: Reverse a number using a while loop and check if it's a
#  palindrome

number = int(input("Enter a number:"))

temp = number

rev = 0

while number > 0:

    rem = number % 10

    rev = (rev * 10) + rem

    number = number // 10

if rev == temp:

    print("it is a pallindrome")

else:

    print("it is not a pallindrome")
