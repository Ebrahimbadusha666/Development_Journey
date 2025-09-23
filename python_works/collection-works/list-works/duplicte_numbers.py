

numbers=[10,20,30,20,40,10,11,12,20,20,11]
# sort()  => [10,10,11,11,12,20,20,20,20,30,40]
#          0   1  2  3  4  5 6  7  8  9  10  11
#          c    n

numbers.sort()  # asc

duplicate_numbers=[]


for current in range(0,len(numbers)-1):
    
    next = current + 1
    
    current_element = numbers[current]
    
    next_element = numbers[next]
    
    difference = next_element - current_element
    
    if difference == 0 and current_element not in duplicate_numbers:
        
        duplicate_numbers.append(current_element)
        
print("duplicate numbers:",duplicate_numbers)




# duplicate_numbers=[]

# for num in numbers:
    
#     frequency = numbers.count(num)
    
#     if frequency > 1 and num not in duplicate_numbers:
        
#         duplicate_numbers.append(num)
        
# print("duplicate numbers:",duplicate_numbers)

