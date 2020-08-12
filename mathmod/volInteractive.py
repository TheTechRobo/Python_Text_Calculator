from volume import *
from cprint import cprint
import logging
logging.info("Running volinteractive")
def main(Comandeer):
    global _
    _ = Comandeer

def cuvol():
    a = int(input(_("What length is the side of the cube? ")))
    cprint.info(_("The volume is: %s" % vol_cube(a)))
def cuboid():
    b = int(input(_("What length is the breadth of the cuboid? ")))
    h = int(input(_("What length is the height of the cuboid? ")))
    l = int(input(_("What length is the cuboid? ")))
    cprint.info(_("The volume is: %s" % vol_cuboid(b=b, h=h, l=l)))
def cylindervol():
    r = int(input(_("What is the radius of the cylinder? ")))
    h = int(input(_("what is the height of the cylinder? ")))
    cprint.info(_("The volume is: %s" % vol_cylinder(r=r, h=h)))
def hollow_cylinder():
    ro = int(input(_("What is the radius of the hollow space? ")))
    rs = int(input(_("What is the radius of the cylinder? ")))
    h = int(input(_("What is the height of the cylinder? ")))
    cprint.info(_("The volume is: %s" % vol_hollow_cylinder(ro=ro, rs=rs, h=h)))
def cone():
    r = int(input(_("What is the radius of the cone? ")))
    h = int(input(_("What is the height of the cone? ")))
    cprint.info(_("The volume is: %s" % vol_cone(r=r, h=h)))
def sphere():
    r = int(input(_("What is the radius of the sphere? ")))
    cprint.info(_("The volume is: %s" % vol_sphere(r)))
    vol_sphere(r)
def hollow_sphere():
    ro = int(input(_("What is the radius of the sphere? ")))
    rs = int(input(_("What is the radius of the hollow space? ")))
    cprint.info(_("The volume is: %s" % vol_hollow_sphere(ro=ro, rs=rs)))
def triprism():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the prism? ")))
    cprint.info(_("The volume is: %s" % vol_tri_prism(a=a, h=h)))
def pentprism():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the prism? ")))
    cprint.info(_("The volume is: %s" % vol_penta_prism(a=a, h=h)))
def hexaprism():
    a = int(input(_("What is the length of the side of the hexagon? ")))
    h = int(input(_("What is the height of the prism? ")))
    cprint.info(_("The volume is: %s" % vol_hexa_prism(a=a, h=h)))
def squiramid():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the pyramid? ")))
    cprint.info(_("The volume is: %s" % vol_sqr_pyramid(a=a, h=h)))
def triramid():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the pyramid? ")))
    cprint.info(_("The volume is: %s" % vol_tri_pyramid(a=a, h=h)))
def pentapyr():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the pyramid? ")))
    cprint.info(_("The volume is: %s" % vol_penta_pyramid(a=a, h=h)))
def hexramid():
    a = int(input(_("What is the length of the side of the base? ")))
    h = int(input(_("What is the height of the pyramid? ")))
    cprint.info(_("The volume is: %s" % vol_hexa_pyramid(a=a, h=h)))

def VolMain():
    cprint.info(_('''Options:
1 - Cube
2 - Cuboid
3 - Cylinder
4 - Hollow cylinder
5 - Cone
6 - Sphere
8 - Hollow sphere
9 - Triangular prism
10 - Pentagonal prism
11 - Hexagonal prism
12 - Square-based pyramid
13 - Triangular pyramid
14 - Pentagon-based pyramid
15 - Hexagon-based pyramid'''))
    while True:
        try:
            choice = int(input(_("Please type one: ")))
        except (ValueError, TypeError) as ename:
            cprint.err("Please type an integer")
            logging.error("User did a ValueError or TypeError while inputting choice in volinteractive (%s)" % ename)
        if choice == 7:
            cprint.ok("Sorry, that was not an option. >:)")
            logging.info(">:) choice 7")
        elif choice == 1:
            cuvol()
            break
        elif choice == 2:
            cuboid()
            break
        elif choice == 3:
            cylindervol()
            break
        elif choice == 4:
            hollow_cylinder()
            break
        elif choice == 5:
            cone()
            break
        elif choice == 6:
            sphere()
            break
        elif choice == 8:
            hollow_sphere()
            break
        elif choice == 9:
            triprism()
            break
        elif choice == 10:
            pentprism()
            break
        elif choice == 11:
            hexaprism()
            break
        elif choice == 12:
            squiramid()
            break
        elif choice == 13:
            triramid()
            break
        elif choice == 14:
            pentapyr()
            break
        elif choice == 15:
            hexramid()
            break
if __name__ == "__main__":
    def _(thestring):
        return thestring
    VolMain()
