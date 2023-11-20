import math

print (" Step 2: ")
for i in range(11):
    print(i)

print ("Step 3: ")
for i in range (1,11):
    print (i)

print ("Step 4: ")
for i in range (1,11,2):
    print (i)

radius = int(input("Enter the radius of the circle "))

if radius > 0:
    area = math.pi * radius**2
    print(f"Step 7: The area of the circle is: {area}")
else:
    print("Step 7: Input parameter is not greater than 0. Cannot compute the area of the circle.")

length = int(input("Enter the length of the rectangle "))
width = int(input("Enter the width of the rectangle "))
if length > 0 and width > 0:
    rectangle_area = length * width
    print(f"Step 10: The area of the rectangle is: {rectangle_area}")
else:
    print("Step 10: Input parameters are not greater than 0. Cannot compute the area of the rectangle.")

