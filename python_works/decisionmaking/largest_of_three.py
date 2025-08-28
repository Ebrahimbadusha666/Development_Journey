
"""
read three numbers num1,num2,num3
display largest number

"""

num1 = int(input("enter first number: ")) #6 

num2 = int(input("enter second number: ")) #4

num3 = int(input("enter third number: ")) #8

if num1 >num2 and num1 > num3: #6 > 4 and 6 > 8
    
    print("Largest number is",num1) #false
    
elif num2 > num1 and num2 > num3: #4 > 6 and 4 > 8
    
    print("Largest number is",num2) #false
    
elif num3 > num1 and num3 > num2:
    
    print("Largest number is", num3)

elif num1==num2 and num1==num3:
    print("three numbers are equal")
    
