for row in range(1,5):
    for col2 in range(row):
        print(" ",end="")
    for col1 in range(row,5):
        print("*",end=" ")
    print()
for row in range(1,5):
    for col2 in range(row,5):
        print(" ",end="")
    for col1 in range(row):
        print("*",end=" ")
    print()