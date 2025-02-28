"""Module to classify triangles based on side lengths."""
def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on its side lengths.
    Args:
        side_a (float): Length of side A.
        side_b (float): Length of side B.
        side_c (float): Length of side C.
    Returns:
        str: A string describing the type of triangle.
    """
    # Check if inputs are actually numbers
    if not all(isinstance(side, (int, float)) and not isinstance(side, bool)
               for side in (side_a, side_b, side_c)):
        return "Not given a number for at least one input"
    # Check if the sides can even form a triangle
    sides = [side_a, side_b, side_c]
    sides_sorted = sorted(sides)
    if (sides_sorted[0] <= 0 or
            sides_sorted[0] + sides_sorted[1] <= sides_sorted[2]):
        return "Invalid triangle, not possible given side lengths"
    triangle_type = ""
    if (round(side_a**2, 5) + round(side_b**2, 5) == round(side_c**2, 5)) or \
       (round(side_a**2, 5) + round(side_c**2, 5) == round(side_b**2, 5)) or \
       (round(side_b**2, 5) + round(side_c**2, 5) == round(side_a**2, 5)):
        triangle_type += "Right "
    #Determines if a right triangle
    if side_a == side_b == side_c:
        triangle_type += "Equilateral"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_type += "Isosceles"
    else:
        triangle_type += "Scalene"

    return f"{triangle_type} Triangle"
