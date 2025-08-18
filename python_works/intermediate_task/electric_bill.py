#  Electricity Bill Calculator: Based on the number of units consumed, calculate the bill with slab rates
#  and a fixed meter charge.

# Meter Charge (Fixed): ₹100

# Slab Rates (for Units Consumed):

# 0 – 100 units → ₹1.50/unit

# 101 – 200 units → ₹2.50/unit

# 201 – 300 units → ₹4.00/unit

# 301 – 500 units → ₹6.00/unit

# Above 500 units → ₹7.00/unit

consumed=int(input("Enter the number of units consumed:"))

fixed_charge = 100


if consumed <= 100:

    bill_amount = consumed*2.5

elif consumed <= 300:

    bill_amount = consumed*4

elif consumed < 500:

    bill_amount = consumed*6

elif consumed > 500:

    bill_amount = consumed*7

if consumed <= 0:

    print("Enter a valid unit")

elif bill_amount < fixed_charge:

    print (f"bill amount is:{fixed_charge}")

else:

    print(f"bill maount is:{bill_amount}")




