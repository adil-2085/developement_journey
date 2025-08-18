# q3

# arr=[10,11,12,13,11,10,14]
# display duplicate number without any methods and 'in' operator

arr = [10,11,12,13,11,10,14]

array_index=0

for number in arr:

    j_index=0

    count=0

    for j in arr:

        if arr[array_index] == arr[j_index]:

            count += 1

        j_index += 1

    if count != 1:

        print(number)

    array_index += 1
