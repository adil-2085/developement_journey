# Print the list of integers from  through  as a string, without spaces.

# a=4

# print('1234')

a=int(input())
c=0

for i in range(1,a+1):

    c=(c*10)+i


# for i in c:
#     print()
# # d=list(c)

d=chr(c)


e={}

for i in range(1,a+1):
    e[i]=i

print(type(e.keys()))

