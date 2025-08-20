
words='goodmorning'

char_dict={}


# meyhord 1
# for i in words:

#     if i in char_dict:

#         char_dict[i]+=1

#     else:

#         char_dict[i]=1

# for i,j in char_dict.items():

#     if char_dict[i]==1:

#         print(i,'=',j)

# print("methord1",char_dict)



# methord2

char_dict2={}

for i in set(words):

    char_dict2[i]=words.count(i)

# print(char_dict2)


mx=max(char_dict2.values())

for i,j in char_dict2.items():

    if j==mx:

        print(i,j) 


long_char={}

long_value=0

for k,v in char_dict2.items():
    if v>long_value:
        
        long_value=v
        long_char.clear()
        long_char[k]=v
print(long_char)



    


