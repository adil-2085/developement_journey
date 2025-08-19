numbers = [2,3,4,5,6]

square_list = {}

for i in numbers:

    # square_list[i] = i**2

    square_list.update({i:i**2})

print(square_list)

