# easy way to create list,set,dictionary from an iterable 

# syntax

# [expression iteration condition]   --  list comprehension
# {expression iteration condition}   --  set comprehension
# (expression iteration condition)   --  tuple comprehension
# {key:value iteration condition}   --  ditionary comprehension


# eg

arr = [2,3,4,5]
# mapping  --  it returns values for every 
# filtering
# reduce
square_list = ([i**2 for i in arr])

odd = [i for i in arr if i%2!=0]

even = [i for i in arr if i%2==0]

print(odd)


print(even)