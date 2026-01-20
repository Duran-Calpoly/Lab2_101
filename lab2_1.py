# lab2_1.py

def get_first_alphabetically(char1, char2):
    """Returns the character that comes first in the alphabet."""
    if char1 < char2:
        return char1
    return char2

def calculate_triangle_area(base, height):
    """Calculates the area of a triangle given base and height."""
    return 0.5 * base * height