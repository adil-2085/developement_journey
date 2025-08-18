# find least +ve number from this sorted array start from 1


# without using built in functions

array = [8,10,11,12,13,14,16,17,19]

for k in range (len(array)-1):

    i = array[k]

    j = array[k+1]

    if j-i != 1:

        print(i+1)



# using built in functions

# arr = [8,10,11,12,13,14,16,17,19]

# i = arr[0]

# j = arr[1]

# for k in range(len(arr)-1):

#     if j-i != 1:

#         print(i+1)

#     if k==len(arr)-2:

#         break

#     i=arr[arr.index(i)+1]

#     j=arr[arr.index(j)+1]


