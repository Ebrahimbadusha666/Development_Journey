"""""
display century year if last two digits of year is 00 else display 
not a century year

"""""

year = int(input("Enter a year: ")) #2000

if (year % 100) == 0: #2000 % 100 == 0
    
    print("Century year") #true
    
else:
    
    print("Not a century year")