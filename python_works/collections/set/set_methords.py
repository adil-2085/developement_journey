# set i  mutable duplicates are not alllowed and unordered

# define

# methords

# union()   -  merging
# intersection()  - common elements
# difference()   - 
# add()  - it is used to add an element to a set
# issubset(object)  - it is used to check if the set is subset of another set
# symmetric_difference(object) = (a - b) U (b - a)





# eg
st1={'green','yellow'}

st2={'blue','red'}

st3=set('green')



union=st1.union(st2)

intersection=st1.intersection(st2)

difference=st1.difference(st2)

symmetric_diff=st1.symmetric_difference(st2)

st2.add("black")

print(st1.issubset(st2))
print(st1.issuperset(st2))

print(f"set 1:{st1} \nset :{st2}\n union:{union}\n intersection: {intersection}\ndifference:{difference} \nsymmetric difference={symmetric_diff}")