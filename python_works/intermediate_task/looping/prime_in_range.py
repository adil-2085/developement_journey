# - Prime Numbers in Range (For + Else): Display all prime numbers between 50 and 100 using
#  for-else loop.

# The for-else loop in Python is a special control flow structure where the else block runs only
# if the loop completes without encountering a break.

for i in range (50,101) :

    for j in range (2,i) :

        if i % j == 0:
            
            break

    else:

        print(i)
