"""
Write a program to read the words from the
 file and display only the words that start with a vowel (a, e, i, o, u).
 Expected Output:
 apple
 orange
 umbrella
 ice
 elephant"""

path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\task\\words.txt'

fr=open(path,'r')

result=[print(w.rstrip('\n')) for w in fr if w[0] in 'aeiou']  
