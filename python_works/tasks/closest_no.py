# given an array of numbers find the closest to zero 

# positive

arr=[-2,-3,-5,-4,-1,2,3,4,5,1]


# assign any positive value from arr to closest_positive
for i in arr:

    if i>0:

        closest_positive=i

        break

# assign any negative value from arr to closest_negative
for i in arr:

    if i<0:

        closest_negative=i

        break


# find the closest positive and closest negative to zero
for i in arr:

    if i >0 and i<closest_positive:

        closest_positive=i

    if i <0 and i>closest_negative:

        closest_negative=i


# print closest no to zero if the distance is same then print positive distance
if 0-closest_positive>=closest_negative:

    print(closest_positive)

else:

    print(closest_negative)
    