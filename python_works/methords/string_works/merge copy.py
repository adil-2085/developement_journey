
# take inputs 

text1 =input("Enter the first text:")

text2 = input("Enter the second text:")

# find the largest amd smallest text

if len(text1) > len(text2):

    large_text = text1

    small_text= text2

else:

    large_text = text2

    small_text = text1

# merge texts if one text is larger than other adds the largest text's rest to the result

result = ""

for i in range(len(large_text)):

    if i < len(small_text):

        result += text1[i] + text2[i]

    else:

        result += large_text[i]

# print result

print(result)

    