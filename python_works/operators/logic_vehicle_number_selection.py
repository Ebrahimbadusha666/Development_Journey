
#read vehicle_number last 4 digit

#last_digit even
#last_digit >5

vehicle_number = int(input("Enter last 4 digit: "))
last_digit = vehicle_number % 10
print(last_digit>5 and last_digit %2==0 )

