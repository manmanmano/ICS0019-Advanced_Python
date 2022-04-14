def calculate_area(b, h):
    """Calculates area of a triangle. Takes as input base and height"""
    if b < 0 or h < 0:
        exit("Negative input is not allowed!")
    return h * b / 2
