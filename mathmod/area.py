from __future__ import division
from __future__ import print_function
from math import sqrt, pi

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")
_f = float
# Contains Area Calculating Functions
# Triangles

#Equilateral Triangle
def area_equilateral_triangle(a):
    '''
    This Function Is For Equilateral Triangle's Area Calculation.
    Takes 'a' As Side Of The Triangle.
    :param a: int
    :return: area
    '''
    a = _f(a)
    area = (sqrt(3) / 4) * pow(a, 2)
    return area

#Right Angle Triangle
def area_right_triangle(b, h):
    '''
    This Function Is For Right Angled Triangle's Area Calculation.
    Takes 'h' As Height & 'b' As The Base Of The Right Angled Triangle.
    And Returns The (approx)Area.
    :param h: int
    :param b: int
    :return: area
    '''
    b = _f(b)
    h = _f(h)
    area = 1 / 2 * b * h
    return area

#Acute Triangle
def area_acute_triangle(a, b, c):
    '''
    This Function Is For Acute Angled Triangle's Area Calculation.
    Takes 'a','b','c' As Length Of Side.
    And Divides The Sum Of The Three Integers By 2.
    And returns the (approx) Area.
    :param a: int
    :param b: int
    :param c: int
    :return: area
    '''
    a = _f(a)
    b = _f(b)
    c = _f(c)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

#Obtuse Triangle
def area_obtuse_triangle(a, b, c):
    '''
        This Function Is For Obtuse Angled Triangle's Area Calculation.
        Takes 'a','b','c' As Length Of Side.
        And Divides The Sum Of The Three Integers By 2.
        And Returns The (approx) Area.
        :param a: int
        :param b: int
        :param c: int
        :return: area
        '''
    a = _f(a)
    b = _f(b)
    c = _f(c)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Quadrilaterals

#Square
def area_square(a):
    '''
    This Function Is For Square's Area Calculation.
    Takes 'a' As Length Of The Side.
    And Returns The Area.
    :param a: int
    :return: area
    '''
    a = _f(a)
    area = pow(a, 2)
    return area

#Rectangle
def area_rectangle(l, b):
    '''
       This Function Is For Rectangle's Area Calculation.
       Takes 'a' As Length Of The Side.
       And Returns The Area.
       :param l: int
       :param b: int
       :return: area
       '''
    l = _f(l)
    b = _f(b)
    area = l * b
    return area

#Parallelogram
def area_parallelogram(b, h):
    '''
    This Function Is For Parallelogram's Area Calculation.
    Takes 'b' As The Base And 'h' As The Height.
    And Returns The Area.
    :param b: int
    :param h: int
    :return: area
    '''
    b = _f(b)
    h = _f(h)
    area = b * h
    return area

#Rhombus
def area_rhombus(do, ds):
    '''
    This Function Is For Rhombus's Area Calculation.
    Takes 'do' As The First Diagonal And 'ds' As The Second Diagonal.
    And Returns The Area.
    :param do: int
    :param ds: int
    :return: area
    '''
    do = _f(do)
    ds = _f(ds)
    area = 1 / 2 * do * ds
    return area

#Trapezium
def area_trapezium(a, b, h):
    '''
    This Function Is For Trapezium's Area Calculation.
    Takes 'a' and 'b' as the length of the parallel sides and 'h' as rhe height.
    And Returns The Area.
    :param a: float
    :param b: float
    :param h: float
    :return: area
    '''
    a = _f(a)
    b = _f(b)
    h = _f(h)
    area = 1 / 2 * (a + b) * h
    return area


# Circles

#Full Circle
def area_circle(r):
    '''
    This Function Is For Circle's Area Calculation.
    Takes 'r' As The Radius Of The Circle.
    And Returns The Area.
    :param r:float
    :return: area
    '''
    r = _f(r)
    area = pi * (pow(r, 2))
    return area

#Semicircle
def area_semicircle(r):
    """
    This Function Is For Semicircle's Area Calculation.
    Takes 'r' As The Radius Of The semicircle.
    And Returns The Area.
    :param r: float
    :return: area
    """
    r = _f(r)
    area = 1 / 2 * (area_circle(r))
    return area

#Circular sector
def area_circular_sector(r,a):
    """
    This Function Is For Circular Sector's Area Calculation.
    Takes 'r' As The Radius Of The Circular Sector.
    Takes 'a' as the angle of the sector in degrees.
    Returns the area.
    :param r: int
    :param a: int
    :return: area
    """
    r = _f(r)
    a = _f(a)
    length = (a / 360) * 2 * pi * r
    area = 1 / 2 * length * r
    return area

#Ring
def area_ring(ro, rs):
    """
    This Function Is For Circular Ring's Area Calculation.
    Takes 'ro'(Radius Of The Outer Circle),
    'rs'(Radius Of The Inner Circle) As The Radii Of The Circular Ring.
    And Returns The Area.
    :param ro: int
    :param rs: int != 1
    :return: area
    """
    ro = _f(ro)
    rs = _f(rs)
    area = pi * (pow(ro, 2) - pow(rs, 2))
    return area

#Ellipse
def area_ellipse(a, b):
    """
    This Function Is For Ellipse's Area Calculation.
    Takes 'a' and 'b' As The Length Of Major And Minor Axis, Respectively.
    And Returns The Area.
    :param a: float
    :param b: float
    :return: area
    """
    a = _f(a)
    b = _f(b)
    area = pi * a * b
    return area

#backwards compatibility
def righttri(b, h):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_right_triangle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_right_triangle(b=b, h=h)
    return result
def equtri(a):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_equilateral_triangle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_equilateral_triangle(a)
    return result
def actri(a, b, c):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_acute_triangle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_acute_triangle(a=a, b=b, c=c)
    return result
def obtri(a, b, c):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_obtuse_triangle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_obtuse_triangle(a=a, b=b, c=c)
    return result
def sq(a):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_square' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_square(a)
    return result
def rectangle(l, b):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_rectangle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_rectangle(l=l, b=b)
    return result
def parallelogram(b, h):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_parallelogram' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_parallelogram(b=b, h=h)
    return result
def rhombus(do, ds):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_rhombus' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_rhombus(do=do, ds=ds)
    return result
def trapezium(a, b, h):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_trapezium' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_trapezium(a=a, b=b, h=h)
    return result
def circle(r):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_circle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_circle(r)
    return result
def semicircle(r):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_semicircle' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_semicircle(r)
    return result
def cirsector(r, a):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_circular_sector' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_circular_sector(r=r, a=a)
    return result
def ring(ro, rs):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_ring' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_ring(ro=ro, rs=rs)
    return result
def ellipse(a, b):
    '''
    This function will be removed in Palc v.0.11-stable.
    See `area_ring' for documentation.
    '''
    print("MATHMOD: WARNING: This naming scheme is deprecated and will be removed in Palc v.0.11-stable.")
    result = area_ellipse(a=a, b=b)
    return result
