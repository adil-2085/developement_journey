for row in range(1,5):
    for col2 in range(row,5):
        print(" ",end="")
    for col1 in range(row):
        print("*",end=" ")
    print()
for row in range(1,4):
    for col2 in range(row+1):
        print(" ",end="")
    for col1 in range(row,4):
        print("*",end=" ")
    print()