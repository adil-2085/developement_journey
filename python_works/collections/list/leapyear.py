# q3
# years =[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011] 
# display all leap years from list


years =[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011]

for i in years:

    if (i % 100==0 and i % 400 == 0) or (i % 100!=0 and i % 4 == 0):

        print(i)