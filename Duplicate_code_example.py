def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_area_and_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter

# Example usage
length = 5
width = 3
height = 2

area_result, perimeter_result = calculate_area_and_perimeter(length, width)
surface_area_result = calculate_surface_area(length, width, height)

print("Area:", area_result)
print("Perimeter:", perimeter_result)
print("Surface Area:", surface_area_result)

