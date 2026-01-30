# Write a program to create area calculator
print("*****AREA CALCULATOR*****")

print("""press 1 to calculate area of square
press 2 to calculate area of circle
press 3 to calculate area of rectangle
press 4 to claculate area of triangle""")

choice=int(input("Enter a number betwwen 1-4:"))

if choice == 1:
    side=float(input("Enter the length of one side of square:"))
    area_of_square= side**2
    print("Area of Square = ",area_of_square)

elif choice == 2:
    radius=float(input("Enter the radius of circle : "))
    area_of_circle= ((22/7)*radius**2)
    print("Area of Circle = ",area_of_circle)

elif choice == 3:
    length=float(input("Enter the length of the rectangle:"))
    width=float(input("Enter the width of the rectangle:"))
    area_of_rectangle= length*width
    print("Area of Rectangle = ",area_of_rectangle)

elif choice == 4:
    base=float(input("Enter the base of the triangle:"))
    height=float(input("Enter the height of the triangle:"))
    area_of_triangle= 0.5*base*height
    print("Area of triangle = ",area_of_triangle)

else:
    print("Enter a valid choice ")