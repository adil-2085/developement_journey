file_path = 'C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\words.txt'

words = ['hello','hai','madam','racecar','pangram']

fw = open(file_path,'w')

for w in words:

    if w == w[::-1]:

        fw.write(w+'\n')

fw.close()

fr=open(file_path,'r')

for l in fr:

    print(l)

fr.close()