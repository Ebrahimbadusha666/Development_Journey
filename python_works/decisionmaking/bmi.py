
"""
based on bmi display health conditon

under weight
normal weight
over weight
obese

BMI= weight_in_kg / height_in_meter**2
"""

height_in_cm = int(input("enter height in cm "))

weight_in_kg = int(input("enter weight in kg "))

height_in_meter = height_in_cm/100

bmi = weight_in_kg/(height_in_meter**2)

bmi = round(bmi)

print(bmi)

if bmi >= 30:
    
    print("obese")   
    
elif bmi >= 25:
    
    print("over weight")
    
elif bmi >= 20:
    
    print("normal weight")
    
else:
    
    print("under weight")
    
