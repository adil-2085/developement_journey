text="brijin is brijin  brijin is bad"

words=text.split()

count={}

for i in words:

    if i in count:

        count[i]+=1

    else:

        count[i]=1

print(count)


