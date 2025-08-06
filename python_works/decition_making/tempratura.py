temprature = int(input("Enter the temprature in degree celcious: "))

if temprature <= 9:
    print("cold")

elif temprature <= 20:
    print("cool")

elif temprature <= 25:
    print("pleasent")

elif temprature <= 30:
    print("warm")

elif temprature <= 35:
    print("hot")

elif temprature <= 40:
    print("very hot")

else:
    print("invalid temprature")