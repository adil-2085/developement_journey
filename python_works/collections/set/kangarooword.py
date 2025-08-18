# A kangaroo word is a word that contains letters of another word, in order, with the same or similar meaning. 
# The phrase kangaroo word is derived from the fact that kangaroos carry their young, known as joeys, in a body pouch. 
# Likewise, kangaroo words carry their joey words within themselves.



word1='chicken'
word2='n'
starting_index=0
ending_index=len(word2)
kangaroo=False
for i in word1:

    if word2 == word1[starting_index:ending_index]:

       kangaroo=True


    starting_index+=1
    ending_index+=1


if kangaroo:
    print("kangaroo")
else:
    print("not")