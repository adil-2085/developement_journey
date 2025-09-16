"""Write a program to read the years from the
 file and display only the leap years.
 Expected Output:
 2000
 2004
 2012
 2024"""

path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\task\\years.txt'

fr = open(path,'r')

result=[print(y.rstrip('\n')) for y in fr if (int(y) % 100==0 and int(y) % 400==0) or (int(y) % 100!=0 and int(y) % 4==0)]


