"""
numbers=[10,11,14,3,8,19,20,21,22,23,56]

q1)display all even numbers
q2)display all odd numbers
q3)display_sum of all even numbers
q4)display largest number
q5)display smallest number

"""

numbers=[10,11,14,3,8,19,20,21,22,23,56]
#          0  1  2 3 4  5  6  7  8  9 10
#q1)display all even numbers
print("Even numbers")

for num in numbers:
    
    if num%2==0:
        
        print(num)
        
#q2)display all odd numbers
print("Odd numbers")

for num in numbers:
    
    if num%2!=0:
        
        print(num)
        
#q3)display_sum of all even numbers

even_sum=0

for num in numbers:
    
    if num%2==0:
        
        even_sum+=num
        
print("Sum of even numbers:",even_sum)

#q4)display largest number  

largest=numbers[0]

for i in range(1,len(numbers)):
    
    if numbers[i]>largest:
        
        largest=numbers[i]
        
print("Largest number:",largest)

#q5)display smallest number

smallest=numbers[0]

for i in range(1,len(numbers)):
    
    if numbers[i]<smallest:
        
        smallest=numbers[i]
        
print("Smallest number:",smallest)
