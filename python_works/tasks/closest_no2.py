# given an array of numbers find the closest to zero 

# positive

arr=[-2,-3,-5,-4,-1,2,3,4,5,1]

closest_no=arr[0]

# find the closest positive and closest negative to zero
for i in arr:

    if abs(i)<abs(closest_no):

        closest_no=i

if closest_no<0 and abs(closest_no) in arr:

    closest_no=abs(closest_no)

print(closest_no)
    