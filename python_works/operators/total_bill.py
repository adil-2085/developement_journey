bill_amount = int(input("Enter the bill amount:"))

tip_percentege = 12

gst_percentege = 8

tip_amount = bill_amount/100 * tip_percentege

gst_amount = bill_amount/100 * gst_percentege

bill_total = bill_amount + tip_amount + gst_amount

print("total amount of the bill is: ",bill_total)

ind_split=bill_total/4

print("individual split is : ",ind_split)
