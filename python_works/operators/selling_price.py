
product_price = int(input("enter the product origional price:"))

percentage = int(input("Enter the margin percentege:"))

gst_persentage = 8

gst_price = (product_price/100)*gst_persentage

margin = (product_price/100)*percentage

selling_price = product_price+margin+gst_price

print("selling price = ",selling_price)