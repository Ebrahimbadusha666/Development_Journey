

numbers = [1,2,3,4,6,7]

numbers.sort()  # asc
#          0  1  2
#          c  n

for current in range(0,len(numbers)-1):
    
    next = current + 1
    
    current_element = numbers[current]
    
    next_element = numbers[next]
    
    difference = next_element - current_element
    
    if difference != 1: 
            
        print("missing positive numbers:",current_element + 1)
        
        break