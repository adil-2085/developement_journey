# A kangaroo word is a word that contains letters of another word, in order, with the same or similar meaning. 
# The phrase kangaroo word is derived from the fact that kangaroos carry their young, known as joeys, in a body pouch. 
# Likewise, kangaroo words carry their joey words within themselves.

# using remove/pop
word1 = 'malayalam'

word2 = 'lam'

list1 = list(word1)

list2 = list(word2)

index = 0

count = 0

for i in range (len(list2)):

    if list2[index] in list1:

        count += 1
        
        for j in range (list1.index(list2[index])-2):

            # list1.remove(list1[j])
            list1.pop(j)      

    index+=1

print("using remove :")

if count == len(list2):

    print('kangaroo')

else:

    print("not")



# using del 
print("using del :")

list1 = list(word1)

list2 = list(word2)

index = 0

count = 0

for i in range (len(list2)):

    if list2[index] in list1:

        count += 1         

        del list1[0:list1.index(list2[index])+1] 

    index += 1

if count == len(list2):

    print('kangaroo')

else:

    print("not")




