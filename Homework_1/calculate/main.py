from triangle_madang import triangle

print("This program will calculate the area of a triagle with the given input.")
base = float(input("Type in the base: "))
height = float(input("Type in the height: "))
area = triangle.calculate_area(base, height)
print(f"The area is: {area}")
