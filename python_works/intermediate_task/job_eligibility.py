# - Job Eligibility Checker: Determine job eligibility based on gender, age, and qualification using
#  conditional checks.

# Gender: must be male

# Age: Must be between 21 and 35

# Qualification: Must have a minimum of Bachelor's Degree

age= int(input("Enter the age :"))

gender=input("Enter the gender (Male/Female):").casefold()

qualification=input("Enter your qualification (Diploma/Bachelor/Master):").casefold()

if (gender == "male" or gender == "female") and (qualification == "diploma" or qualification == "bachelor" or qualification == "master") and (age > 0):

    if (age > 21 and age < 35) and( qualification != "diploma") and gender == "male" :

        print("you are eligible for this job")

    else:

        print("You are not eligible for this job") 

else:

    print("Enter a valid gender / qualification / age") 









