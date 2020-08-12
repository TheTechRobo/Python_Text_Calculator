from math import pi, sqrt
import logging
if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")
# Contains Volume Calculating Functions

#CUBE
def vol_cube(a: int) -> 'volume':
    '''
    Takes 'a' as the side of the cube. Returns the volume
    :param a: int
    :return: volume
    '''
    volume = pow(a, 3)
    logging.info("User ran Cuvolu(m) a=%s answer=%s" % (a, volume))
    
    return volume

#CUBOID
def vol_cuboid(l: int, b: int, h: int) -> 'volume':
    '''
    Takes 'l','b', and 'h' as length, breadth, and height, respectively.
    Returns the volume.
    :param l: int
    :param b: int
    :param h: int
    :return: volume
    '''
    volume = l * b * h
    logging.info("User ran Triangle Pyramid Volume l=%s b=%s h=%s answer=%s" % (l, b, h, volume))
    
    return volume

#CYLINDER
def vol_cylinder(r: int, h: int) -> 'volume':
    '''
    Takes 'r' and 'h' as radius and height, respectively. Returns the volume.
    :param r: int
    :param h: int
    :return: volume
    '''
    volume = pi * pow(r, 2) * h
    logging.info("User ran Triangle Pyramid Volume r=%s h=%s answer=%s" % (r, h, volume))
    
    return volume

#HOLLOW CYLINDER
def vol_hollow_cylinder(ro: int, rs: int, h: int) -> 'volume':
    '''
    Takes 'ro', 'rs', and 'h' as radius of the hollow space, radius of the cylinder, and height of the cylinder, respectively. Returns the volume.
    :param ro: int
    :param rs: int
    :param h: int
    :return: volume
    '''
    volume = 2 * pi * (ro + rs) * h
    logging.info("User ran Hollowcylinder Volume ro=%s rs=%s h=%s answer=%s" % (ro, rs, h, volume))
    
    return volume

#CONE
def vol_cone(r: int, h: int) -> 'volume':
    '''
    Takes 'r' and 'h' as the radius and height of the cone, respectively. Returns the volume.
    :param r: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * pi / pow(r, 2) * h
    logging.info("User ran Conevol r=%s h=%s answer=%s" % (r, h, volume))
    
    return volume

#SPHERE
def vol_sphere(r: int) -> 'volume':
    '''
    Takes 'r' as the radius of the sphere. Returns the volume.
    :param r: int
    :return: volume
    '''
    volume = 4 / 3 * pi * pow(r, 3)
    logging.info("User ran sphere Volume r=%s answer=%s" % (r, volume))
    
    return volume

#HOLLOW SPHERE
def vol_hollow_sphere(ro: int, rs: int) -> 'volume':
    '''
    Takes 'ro' and 'rs' as the full radius of the sphere, and radius of the hollow space of the sphere, respectively. Returns the volume.
    :param ro: int
    :param rs: int
    :return: volume
    '''
    volume = 4 / 3 * pi * (pow(ro, 3) - pow(rs, 3))
    logging.info("User ran Hollowsphere Volume ro=%s rs=%s answer=%s" % (ro, rs, volume))
    
    return volume

#BASE TRIANGLE PRISM
def vol_tri_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the legnth of the side of the triangular base, and height of the prism, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (sqrt(3) / 4 * pow(a, 2)) * h
    logging.info("User ran Triangle Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
    
    return volume

#PRISM BASE PENTAGON
def vol_penta_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the pentagon base, and height of the prism, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (sqrt(3) * pow(a, 2)) * h
    logging.info("User ran PentaPrism Volume a=%s h=%s answer=%s" % (a, h, volume))
    
    return volume

#PRISM WITH A HEXAGON BASE
def vol_hexa_prism(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the hexagon, and height of the prism, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (2.5981 * pow(a, 2)) * h
    logging.info("User ran Hexagon Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
    return volume

#PYRAMID WITH A SQUARE BASE
def vol_sqr_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the square base, and height of the pyramid, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (1 / 3 * h) * pow(a, 2)
    logging.info("User ran Square Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    
    return volume

#PYRAMID WITH A TRIANGULAR BASE
def vol_tri_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the triangle base, and height of the pyramid, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * h * (sqrt(3) / 4 * pow(a, 2))
    logging.info("User ran Triangle Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    
    return volume

#PYRAMID WITH A PENTAGON BASE
def vol_penta_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the pentagon base, and height of the pyramid, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = 1 / 3 * h * (sqrt(3) * pow(a, 2))
    logging.info("User ran Pentapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    
    return volume

#PYRAMID WITH A HEXAGON BASE
def vol_hexa_pyramid(a: int, h: int) -> 'volume':
    '''
    Takes 'a' and 'h' as the length of the side of the hexagon base, and height of the pyramid, respectively. Returns the volume.
    :param a: int
    :param h: int
    :return: volume
    '''
    volume = (1 / 3 * h) * (2.5981 * pow(a, 2))
    logging.info("User ran Hexapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    return volume
