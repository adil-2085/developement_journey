for row in range(6,1,-1):
    for col2 in range(row,6):
        print(" ",end="")
    for col1 in range(row-1):
        print("*",end=" ")
    
    print()