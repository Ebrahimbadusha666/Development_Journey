
#last_week_attendence store organize "P","O","A","H"

attendence=["H","P","P","A","P","H","O"]

attendence[3]="O"
print(attendence)

#holiday_count
#offline_count
#absent__count

holiday_count=0
offline_count=0
online_count=0
absent_count=0

for at in attendence:
    
    if at =="H":
        
        holiday_count+=1
        
    elif at =="P":
        
        offline_count+=1
        
    elif at =="O":
        
        online_count+=1
        
    elif at =="A":
        
        absent_count+=1
        
print("Holiday count",holiday_count)
print("Absent count",absent_count)
print("Offline count",offline_count)
print("Online count",online_count)
  

# # for at in attendence:
    
#     if at =="H":
        
#         print("holiday")
        
#     elif at =="A":
        
#         print("absent")
        
#     elif at =="O":
        
#         print("online")
        
#     elif at =="P":
        
#         print("offline")
        
        
