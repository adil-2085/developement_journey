'''

shallow copy(copies top level(outer) objects,share reference of nested(inner) object)
deepcopy (copies both toplevel object and nested object)

'''


from copy import copy,deepcopy


ali_fav_food= [['porotta','beef'],
               ['biriyani','salad'],
               ['tea','coffee']               
               ]


akash_fav_food1 = copy(ali_fav_food)    #shallow copy

akash_fav_food2 = deepcopy(ali_fav_food)   #deep copy

akash_fav_food2[0][0] = 'idly'

print(ali_fav_food)

print(akash_fav_food2)

akash_fav_food1[0][0] = 'dosa'

print(ali_fav_food)

print(akash_fav_food1)
