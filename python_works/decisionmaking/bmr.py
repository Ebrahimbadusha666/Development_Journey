

gender = input("Enter gender")

age = int(input("Enter age"))

weight_in_kg = int(input("Enter weight in kg"))

height_in_cm = int(input("Enter height in cm"))

activity_level = 1.2

"""
the basal metabolic rate (BMR)=
10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5 for (men)
10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161 for(women)
"""
if gender == "male":
    
    BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5
    
else:
    
    BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161
    
calories = BMR * activity_level

print(calories)