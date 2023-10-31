def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

def calculate_area_and_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter

