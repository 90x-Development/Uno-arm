import math

def calculate_angle(m, n, y, r, x, z):
    # Calculate the direction vectors of the lines
    d1 = (y - m, r - n)
    d2 = (x - m, z - n)

    # Calculate the dot product of the direction vectors
    dot_product = d1[0] * d2[0] + d1[1] * d2[1]

    # Calculate the magnitudes of the direction vectors
    magnitude_d1 = math.sqrt(d1[0] ** 2 + d1[1] ** 2)
    magnitude_d2 = math.sqrt(d2[0] ** 2 + d2[1] ** 2)

    # Calculate the angle between the lines at the point (m, n)
    angle = math.acos(dot_product / (magnitude_d1 * magnitude_d2))
    
    # Convert angle to degrees
    angle_degrees = math.degrees(angle)
    
    return angle_degrees
