input=[1,2,3,4,5,5]
target=6
result=[]
for i in range(len(input)):
    # result=[[input[0],j] for j in input if input[0]+j==target and input[0]!=j]
    for j in input:
        if input[0]+j==target and input[0]!=j and [input[0],j] not in result:
            result.append([input[0],j])
    input.pop(0)   
print(result)
