list1=[1,2,3,4]

target=7

a=[i,j for i in list1 for j in list1 if i+j==target ]




for i in list1:
    for j in list1:
        ans=0
        if i+j == target:
            
            ans=[i,j]
            print(ans)
            break
    if ans != 0:
        break