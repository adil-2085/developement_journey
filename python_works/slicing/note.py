'''
definition: slicing means extracting a part (subsequence) from a sequence like a list,string,or tuple using a speasial syntax

syntax: sequence[start:stop:step]


enumarate()  -  it is a built-in function that returns index,and value of a list,tuple,string

'''



word='pradiyod world'
#     01234567

sliced_word1=word[0:7:3]

# print(sliced_word1)

sliced_word2=word[7:0]

# print(sliced_word2)


arr=['word','madam','racecar','car']

# for i in arr:

#     print(i,'is pallindrome') if i==i[::-1] else print()

# eg of enumerate()
for index,element in enumerate(arr):

    print(index,element)

list=[2,3,4,5]

for index,element in enumerate(list,start=1):

    print(element**index)



