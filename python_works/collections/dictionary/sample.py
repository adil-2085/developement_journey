jdm_car={"brand":"Toyota","model":"land cruiser","type":"suv","milage":5}

print(jdm_car["brand"])

print(jdm_car["model"])

print(jdm_car["type"])

jdm_car["type"]="sedan"

print(jdm_car["type"])


if "milage" in jdm_car:
     
     jdm_car["milage"]+=10
     
else:
     
     jdm_car["milage"]=6

print(jdm_car["milage"])
