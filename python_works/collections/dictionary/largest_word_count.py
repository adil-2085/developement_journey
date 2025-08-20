text = "this is a python program to find most recursive word this python is python"

words = text.split()

count = {}

for i in words:

    if i in count:

        count[i] += 1

    else:

        count[i] = 1

# print(count)

max_value = max(count.values())

for k,v in count.items():

    if v == max_value:

        print(k,':',v) 





# print(count)#{'this': 2, 'is': 2, 'a': 1, 'python': 3, 'program': 1, 'to': 1, 'find': 1, 'most': 1, 'recursive': 1, 'word': 1}
# sorted_count=sorted(count,reverse=True,key=count.get)#['python', 'this', 'is', 'a', 'program', 'to', 'find', 'most', 'recursive', 'word']

# for k in sorted_count:

#     print(k,count.get(k),end='')