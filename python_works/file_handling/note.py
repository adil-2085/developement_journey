'''
files are used to store data
eg: .txt,.json


--operations--

read---> read the data inthe file
write--> overwrites the data in the file (w) if the given file is not exists python creates the file
append--> append data with the existing data in the file (a)


---syntax---

variable_name=open("filepath","mode")


eg:

vr=open("note.txt","r")   ----   reads the file


'''


# fr=open("C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\demo.txt","r")
file_path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\demo.txt'
# read

fr=open(file_path,'r')

for l in fr:

    print(l)

fr.close()



# write
fw=open(file_path,'w')

word_list=['good','morning']

for w in word_list:

    fw.write(w+'\n')

fr.close()


# append

fa=open(file_path,'a')

word_list=['good','morning']

for w in word_list:

    fa.write(w+'\n')

fr.close()




