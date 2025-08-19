text = 'malayalam'

text_list = list(text)

long_pallindrome = list()

for i in range(len(text)+1):

    for j in range(i):

        sample = text_list[j:i]

        sample_reverse = text_list[j:i]

        sample_reverse.reverse()

        if (sample == sample_reverse) and (len(long_pallindrome)<len(sample)):
            
            long_pallindrome = sample

            str=text[j:i]

# str="".join(long_pallindrome)

print(str)
    
