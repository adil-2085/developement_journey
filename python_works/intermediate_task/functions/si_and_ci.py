# - SI & CI Calculator: Write separate functions for calculating Simple Interest and Compound
#  Interest


# Simple Interest (SI):
# SI=(𝑃×𝑅×𝑇)/100
# P = Principal
# R = Annual interest rate in percent
# T = Time period in years

# Compound Interest (CI):
# a=p * ((1+(r/100))**t)
# CI=A−P
# where:
# A = Final amount after compounding


def si_and_ci(principal,rate,time):

    
    simple_interest=(principal*rate*time)/100

    final_amount=principal * ((1+(rate/100))**time)

    compound_interest=final_amount-principal

    print(f"compount interest = {compound_interest}\ncompount final amount = {final_amount}\nsimple interest = {simple_interest}")


principal=int(input("Enter the principal amount:"))
rate=int(input("Enter the interest rate in percentage:"))
time=int(input("Enter the time period in years"))


si_and_ci(principal,rate,time)