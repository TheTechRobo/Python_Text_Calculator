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

def areaTriangle(base, height):
    base, height = _floats(base, height)
    return base * height * 0.5

def areaSquare(length):
    a = _floats(a)[0]
    return a * a

def areaRectangle(width, height):
    width, height = _floats(width, height)
    return width * height

def areaParallelogram(base, height):
    base, height = _floats(base, height)
    return base * height

def areaTrapezium(height, base1, base2):
    """
    Also known as a "trapezoid" in the US.
    """
    height, base1, base2 = _floats(height, base1, base2)
    return 0.5 * h * (base1 + base2)
areaTrapezoid = areaTrapezium

def areaCircle(radius):
    """
    Uses `math.pi' as pi.
    """
    radius = _floats(radius)[0]
    return pi * (radius ** 2)

def areaEllipse(major, minor):
    """
    param major: Length of Semi-major axis
    param minor: Length of Semi-minor axis
    """
    major, minor = _floats(major, minor)
    return pi * major * minor
