weight_in_kg=int(input("Enter your weight in kg:"))

height_in_meter=int(input("Enter your height in CM:"))/100

bmi=weight_in_kg/height_in_meter**2

print(bmi)