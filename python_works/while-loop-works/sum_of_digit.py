
#read number 
#set sum as 0

#loop num!=0
    #extract digit frm the number
    #add digit with number
    #flooring the number
    
number = int(input("enter number"))

sum = 0

while(number!=0):
    
    digit = number%10
    sum = sum + digit
    number = number//10

print(sum)
    
    
    
    