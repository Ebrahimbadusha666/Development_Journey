# read temp in degree celsious convert into Fh

celsius = int(input("Enter temperature in Celsius: "))
fh = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fh)

# read temp in fh convert ito degree celsious

fh = int(input("Enter temperature in Fahrenheit: "))
celsius = (fh - 32) * 5/9
print("Temperature in Celsius:", celsius)

# read kilometer and convert into meter

km = int(input("Enter distance in kilometers: "))
meter = km * 1000
print("Distance in meters:", meter)
