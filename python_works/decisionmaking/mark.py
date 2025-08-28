
mark1= int(input("enter mark1: "))

mark2= int(input("enter mark2: "))

mark3= int(input("enter mark3: "))

total_mark = mark1 + mark2 + mark3

if total_mark >= 140:
    
    print("Excellent pool")
    
elif total_mark >= 130:
    
    print("progress pool")
    
elif total_mark >= 120:
    
    print("foundation pool")
    
elif total_mark <= 100:
    
    print("dead pool")