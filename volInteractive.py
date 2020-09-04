from mathmod.volume import *
from modules.cprint import cprint
import logging
logging.info("Launched volInteractive.")
def main(Comandeer):
    global _
    _ = Comandeer

def cuvol():
    a = float(input(_("What length is the side of the cube? ")))
    volume = vol_cube(a)
    logging.info("User ran Cuvolu(m) a=%s answer=%s" % (a, volume))
    cprint.info(_("The volume is: %s" % volume))
def cuboid():
    b = float(input(_("What length is the breadth of the cuboid? ")))
    h = float(input(_("What length is the height of the cuboid? ")))
    l = float(input(_("What length is the cuboid? ")))
    volume = vol_cuboid(b=b, h=h, l=l)
    logging.info("User ran Cuboid Volume l=%s b=%s h=%s answer=%s" % (l, b, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def cylindervol():
    r = float(input(_("What is the radius of the cylinder? ")))
    h = float(input(_("What is the height of the cylinder? ")))
    volume = vol_cylinder(r=r, h=h)
    logging.info("User ran Cylinder Volume r=%s h=%s answer=%s" % (r, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def hollow_cylinder():
    ro = float(input(_("What is the radius of the hollow space? ")))
    rs = float(input(_("What is the radius of the cylinder? ")))
    h = float(input(_("What is the height of the cylinder? ")))
    volume = vol_hollow_cylinder(ro=ro, rs=rs, h=h)
    logging.info("User ran Hollowcylinder Volume ro=%s rs=%s h=%s answer=%s" % (ro, rs, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def cone():
    r = float(input(_("What is the radius of the cone? ")))
    h = float(input(_("What is the height of the cone? ")))
    volume = vol_cone(r=r, h=h)
    logging.info("User ran Conevol r=%s h=%s answer=%s" % (r, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def sphere():
    r = float(input(_("What is the radius of the sphere? ")))
    volume = vol_sphere(r)
    logging.info("User ran sphere Volume r=%s answer=%s" % (r, volume))
    cprint.info(_("The volume is: %s" % volume))
def hollow_sphere():
    ro = float(input(_("What is the radius of the sphere? ")))
    rs = float(input(_("What is the radius of the hollow space? ")))
    volume = vol_hollow_sphere(ro=ro, rs=rs)
    logging.info("User ran Hollowsphere Volume ro=%s rs=%s answer=%s" % (ro, rs, volume))
    cprint.info(_("The volume is: %s" % volume))
def triprism():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the prism? ")))
    volume = vol_tri_prism(a=a, h=h)
    logging.info("User ran Triangle Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def pentprism():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the prism? ")))
    volume = vol_penta_prism(a=a, h=h)
    logging.info("User ran PentaPrism Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def hexaprism():
    a = float(input(_("What is the length of the side of the hexagon? ")))
    h = float(input(_("What is the height of the prism? ")))
    volume = vol_hexa_prism(a=a, h=h)
    logging.info("User ran Hexagon Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def squiramid():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the pyramid? ")))
    volume = vol_sqr_pyramid(a=a, h=h)
    logging.info("User ran Square Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def triramid():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the pyramid? ")))
    volume = vol_tri_pyramid(a=a, h=h)
    logging.info("User ran Triangle Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def pentapyr():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the pyramid? ")))
    volume = vol_penta_pyramid(a=a, h=h)
    logging.info("User ran Pentapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))
def hexramid():
    a = float(input(_("What is the length of the side of the base? ")))
    h = float(input(_("What is the height of the pyramid? ")))
    volume = vol_hexa_pyramid(a=a, h=h)
    logging.info("User ran Hexapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
    cprint.info(_("The volume is: %s" % volume))

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
