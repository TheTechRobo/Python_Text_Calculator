"""
https://byjus.com/volume-formulas/
"""

from math import pi, sqrt

def _floats(*args):
    a = list()
    for num in args:
        a.append(float(num))
    return a

def volume_cuboid(length: float, width: float, height: float):
    """
    Cuboids include rectangular solids
    """
    l, w, h = _floats(length, width, height)
    return l * w * h

def volume_cube(length: float):
    """
    length: Length of edge of side
    """
    l = float(length)
    return l ** 3

def volume_cylinder(radius: float, height: float):
    """
    radius: Radius of the circular base
    height: Height of the cylinder
    """
    r, h = _floats(radius, height)
    return pi * (r ** 2)

def volume_hollow_cylinder(radius, height, thickness):
    """
    https://www.vcalc.com/wiki/KurtHeckman/Hollow+Cylinder+-+Volume
    Report bugs if it's incorrect
    radius: Outer radius
    height: Height (or length) of the cylinder
    thickness: Thickness
    """
    r, h, t = _floats(radius, height, thickness)
    return pi * h * (r ** 2 - (r - t) ** 2)

def volume_prism(area, height):
    """
    area: Area of base
    height: Height of the prism.
    """
    B, h = _floats(area, height)
    return B * h

def volume_sphere(radius):
    r = _floats(radius)[0]
    return (4 / 3) * pi * (r ** 3)

def volume_hollow_sphere(total, hollow):
    """
    Not quite as accurate as the old method (1 decimal point less) but close enough :P
    Idea from https://www.vedantu.com/question-answer/what-is-the-volume-of-hollow-sphere-5b7fada8e4b084fdbbfc1df1
    hollow: Radius of the hollow space
    total: Radius of the entire sphere
    """
    return sphere(total) - sphere(hollow)

def volume_pyramid(area, height):
    """
    area: Area of the base
    height: Height (base to tip)
    """
    B, h = _floats(area, height)
    return (1/3) * B * h

# "Square or Rectangular Pyramid" isn't impl'ed because it just is
# "Pyramid" but it calculates the area of the base

def volume_right_circular_cone(radius, height):
    """
    radius: Radius of the base
    height: Height
    """
    r, h = _floats(radius, height)
    return (1 / 3) * pi * (r ** 2) * h
volume_cone = volume_right_circular_cone

def volume_ellipsoid(a, b, c):
    """
    a: Semi axe of the ellipsoid
    b: Semi axe
    c: Semi axe
    """
    a, b, c = _floats(a, b, c)
    return (4/3) * pi * a * b * c

def volume_tetrahedron(length):
    """
    length: length of the edge
    """
    a = float(a)
    return a ** 3 / (6 * sqrt(2))
