
"""
read number
set digit_count = len(str(number)) //  convert the number into string for getting the digi_count
set sum as 0

    
loop:
    extract digit
    
    find exponent of digit with digit_count
    
    add exponent with sum
    
    floor number
    
display sum

"""

number = int(input("enter a number"))

digit_count = len(str(number))

sum = 0

original = number

while( number != 0):
    
    digit = number% 10
    
    exponent = digit ** digit_count
    
    sum = sum + exponent
    
    number = number//10
    
if original == sum:
    
    print(original,"is a armstrong number")
    
else:
    
    print(original,"not a armstrong number")
    
    