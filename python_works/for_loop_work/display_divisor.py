
#read a number number=12
# display all divisor of 12 

number = int(input("enter number "))

for i in range(1,number+1):
    
    if number%i==0:
        
        print(i)
        