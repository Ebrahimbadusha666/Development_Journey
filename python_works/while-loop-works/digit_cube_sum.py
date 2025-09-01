
#read number
# set sum 0

#loop:
    #extract digit 
    #find digit cube
    #add digit cube with sum
    #floor  number
    

number = int(input("enter number"))

sum = 0

while(number!=0):
    
    digit = number %10
    
    cube = digit **3
    
    sum = sum + cube
    
    number = number //10

print(sum)