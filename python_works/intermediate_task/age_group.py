age=int(input("Enter the age:"))

if age<=0:
    print("enter a valid age")
else:
    if age<12:
        print("Child")
    elif age<19:
        print("Teen")
    elif age<59:
        print("Adult")
    elif age>60:
        print("Senior")