
"""
expenses=[14000,13000,14000,15000,16000]

expenses={"jan":14000,"feb":13000,"mar":14000]  #dictionary

"""
mobile={"brand":"samsung","model":"s24","ram":8,"storage":128,"color":"white"}

mobile_model=mobile["model"]
mobile_brand=mobile["brand"]

print(mobile_model)
print(mobile_brand)

#chk key exist or not

if "price" in mobile:
    
    print("exist")
    
else:
    
    print("not exist")
    
#add | update new key:value

mobile["price"] = 58000

print(mobile)