# - Pass or Fail Evaluator: Function that checks if all subject marks are 35+ and average is 50+.

def pass_or_fail(sub_1,sub_2,sub_3,sub_4,sub_5):

    if sub_1<=0 or sub_2 <=0 or sub_3 <=0 or sub_4 <=0 or sub_5 <=0 or sub_1 > 100 or sub_2 > 100 or sub_3 > 100 or sub_4 > 100 or sub_5 > 100 :

        print("Enter valid marks")
    else:

    # calculate average and pass/fail

        mark_percentage=((sub_1+sub_2+sub_3+sub_4+sub_5)*100)/500
  
        if (mark_percentage >= 50) and (sub_1>=35 and sub_2 >=35 and sub_3 >=35 and sub_4 >=35 and sub_5 >=35):

            print("Pass")

        else:
            print("Fail")


    
sub_1=int(input("Enter the mark of first subject:"))

sub_2=int(input("Enter the mark of second subject:"))

sub_3=int(input("Enter the mark of third subject:"))

sub_4=int(input("Enter the mark of fourth subject:"))

sub_5=int(input("Enter the mark of fifth subject:"))

pass_or_fail(sub_1,sub_2,sub_3,sub_4,sub_5)
