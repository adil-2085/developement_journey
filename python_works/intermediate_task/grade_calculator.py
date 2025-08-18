# Grade Calculator with Validation: Accept marks of 5 subjects, calculate average and assign grade
#  A/B/C/D/Fail. Include input validation.

# A+ 91-100%	
# A	 81-90%	
# B	 61-70%	
# C	 41-50%
# D  21-40%
# F	 0-20%	

print("Total mark of a subject is: 100")

# Accept marks of 5 subjects

sub_1=int(input("Enter the mark of first subject:"))

sub_2=int(input("Enter the mark of second subject:"))

sub_3=int(input("Enter the mark of third subject:"))

sub_4=int(input("Enter the mark of fourth subject:"))

sub_5=int(input("Enter the mark of fifth subject:"))

# input validation.

if sub_1<=0 or sub_2 <=0 or sub_3 <=0 or sub_4 <=0 or sub_5 <=0 or sub_1 > 100 or sub_2 > 100 or sub_3 > 100 or sub_4 > 100 or sub_5 > 100 :

    print("Enter valid marks")

else:

    # calculate average

    average_mark=(sub_1+sub_2+sub_3+sub_4+sub_5)/5

    mark_percentage=((sub_1+sub_2+sub_3+sub_4+sub_5)*100)/500
    
    print(f"Total mark percentage is: {mark_percentage} %")

    # assign grade A/B/C/D/Fail
    
    if mark_percentage <= 20:

        print("Fail")

    elif mark_percentage <= 40:

        print("D grade")

    elif mark_percentage <= 50:

        print("C grade")

    elif mark_percentage <= 700:

        print("B grade")

    elif mark_percentage <= 90:

        print("A grade")

    else:
        
        print("A plus grade")

