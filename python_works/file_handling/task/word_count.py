'''
Task 3: Count Each Word in a File
 Question:
Write a program to read the content and display the count of each word in the file.
 Expected Output:
python: 2
 is: 2
 a: 1
 powerful: 1
 programming: 1
 language: 1
 fun: 1
 to: 1
 learn: 1
'''

path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\task\\words2.txt'

fr=open(path,'r')

split=[word for line in [all.split() for all in fr] for word in line]

[print(k,':',v) for k,v in {item:split.count(item) for item in split}.items()]