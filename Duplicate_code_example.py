def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def calculate_surface_area(length, width, height):
    return 2 * calculate_area(length, width) + 2 * calculate_area(length, height) + 2 * calculate_area(width, height)

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
