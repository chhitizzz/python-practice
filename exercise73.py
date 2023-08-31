# Function that calculates the area of a rectangle given its width and height. Then, write a function that calculates the area of a triangle given its base and height

def rectangleArea(width, height):
    area = width * height
    return area 

def triangleArea(base, height):
    area = 0.5 * base * height
    return area

rect_width = float(input("Enter the width of the rectangle: "))
rect_height = float(input("Enter the height of the rectangle: "))

rect_area = rectangleArea(rect_width, rect_height)
print(f"The area of the rectangle is {rect_area:.2f} square units.")