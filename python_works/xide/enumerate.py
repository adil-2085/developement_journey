'''
definition: slicing means extracting a part (subsequence) from a sequence like a list,string,or tuple using a speasial syntax

syntax: sequence[start:stop:step]


enumarate()  -  it is a built-in function that returns index,and value of a list,tuple,string

'''

# eg of enumerate()
for index,element in enumerate(arr):

    print(index,element)

list=[2,3,4,5]

for index,element in enumerate(list,start=1):

    print(element**index)