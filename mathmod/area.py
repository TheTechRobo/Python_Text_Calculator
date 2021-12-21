from math import pi
"""
Mathmod area function file
--------------------------
Run `import mathmod.area'
followed by `help(mathmod.area)'
for documentation. It should
be complete.
Most formulae come from https://www.mathsisfun.com/area.html.
"""

def _floats(*args):
    '''
    internal usage only
    '''
    hi = []
    for item in args:
        hi.append(float(item))
    return hi

def area_triangle(base, height):
    base, height = _floats(base, height)
    return base * height * 0.5

def area_square(length):
    a = _floats(length)[0]
    return a * a

def area_rectangle(width, height):
    width, height = _floats(width, height)
    return width * height

def area_parallelogram(base, height):
    base, height = _floats(base, height)
    return base * height

def area_trapezium(height, base1, base2):
    """
    Also known as a "trapezoid" in the US.
    """
    height, base1, base2 = _floats(height, base1, base2)
    return 0.5 * height * (base1 + base2)
area_trapezoid = area_trapezium

def area_circle(radius):
    """
    Uses `math.pi' as pi.
    """
    radius = _floats(radius)[0]
    return pi * (radius ** 2)

def area_semicircle(radius):
    """
    See areaCircle
    """
    r = _floats(radius)[0]
    return 0.5 * (area_circle(r))

def area_ellipse(major, minor):
    """
    param major: Length of Semi-major axis
    param minor: Length of Semi-minor axis
    """
    major, minor = _floats(major, minor)
    return pi * major * minor

def area_sector(angle, radius):
    """
    :param angle: Angle in radians
    :param radius: Radius of the sector
    """
    angle, radius = _floats(angle, radius)
    return 0.5 * (radius ** 2) * angle

def area_rhombus(base, height):
    """
    :param base: Length of any side.
    :param height: Height of the rhombus.
    Source: https://byjus.com/maths/area-of-rhombus/
    """
    base, height = _floats(base, height)
    return base * height

def area_ring(inner, outer):
    """
    :param inner: Radius of the inner circle
    :param outer: Inner but outer
    """
    inner, outer = _floats(inner, outer)
    return pi * ((outer ** 2) - (inner ** 2))
