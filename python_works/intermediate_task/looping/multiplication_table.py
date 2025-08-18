# - Multiplication Table (Nested Loop): Generate a multiplication table (1 to 10) using nested loops.

for i in range (1,11):

    for j in range (1,11):

        print(f"{j} * {i} = {j*i}" )
    
    print("\n")