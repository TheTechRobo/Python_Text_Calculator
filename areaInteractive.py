from mathmod.area import *
from modules.cprint import cprint
import logging
logging.info("Launched areaInteractive.")
def main(Comandeer):
    globals()['_'] = Commandeer

def equ_triangle():
    a = float(input(_("What length is the side of the triangle? ")))
    area = equtri(a)
    cprint.info(_("The area is: %s" % area))
    logging.info("User used equalateral triangle area with origin %s answer %s" % (a, area))
def right_triangle():
    b = float(input(_("What length is the base of the triangle? ")))
    h = float(input(_("What length is the height of the triangle? ")))
    area = righttri(b=b, h=h)
    logging.info("User used Righttri area with variable b=%s, h=%s, answer=%s" % (b, h, area))
    cprint.info(_("The area is: %s" % area))
def acute_triangle():
    a = float(input(_("What is the length of the first side? ")))
    b = float(input(_("what is the length of the second side? ")))
    c = float(input(_("What is the length of the third side? ")))
    area = actri(a, b, c)
    logging.info("User used Acutetri area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area))
    cprint.info(_("The area is: %s" % area))
def obtuse_triangle():
    a = float(input(_("What is the length of the first side? ")))
    b = float(input(_("What is the length of the second side? ")))
    c = float(input(_("What is the length of the third side? ")))
    area = obtri(a, b, c)
    logging.info("User used Obtuse Triangle area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area))
    cprint.info(_("The area is: %s" % area))
def square():
    a = float(input(_("What is the length of the side of the square? ")))
    area = sq(a)
    logging.info("User used Square area with variable a=%s, answer=%s" % (a, area))
    cprint.info(_("The area is: %s" % area))
def rectangle():
    from area import rectangle as rec
    l = float(input(_("What is the length of the rectangle? ")))
    b = float(input(_("What is the height of the rectangle? ")))
    area = rec(l, b)
    logging.info("User used Rectangle area with variable l=%s, b=%s, answer=%s" % (l, b, area))
    cprint.info(_("The area is: %s" % area))
def parallelogram():
    from area import parallelogram as para
    b = float(input(_("What is the length of the base? ")))
    h = float(input(_("What is the height of the shape? ")))
    area = para(b, h)
    logging.info("User used Parallelogram area with variable b=%s, h=%s, answer=%s" % (b, h, area))
    cprint.info(_("The area is: %s" % area))
def rhombus():
    from area import rhombus as rhombu
    do = float(input(_("What is the length of the first diagonal? ")))
    ds = float(input(_("What is the length of the 2nd diagonal? ")))
    area = rhombu(do, ds)
    logging.info("User used Rhombus area with variable do=%s, ds=%s, answer=%s" % (do, ds, area))
    cprint.info(_("The area is: %s" % area))
def trapezium():
    from area import trapezium as trapezi
    a = float(input(_("What is the length of the 1st set of parallel sides? ")))
    b = float(input(_("What is the length of the 2nd set of parallel sides? ")))
    h = float(input(_("What is the height of the trapezium? ")))
    area = trapezi(a, b, h)
    logging.info("User used Trapezium area with variable a=%s, b=%s, h=%s, answer=%s" % (a, b, h, area))
    cprint.info(_("The area is: %s" % area))
def circle():
    from area import circle as circl
    r = float(input(_("What is the radius of the circle? ")))
    area = circl(r)
    logging.info("User used Circle area with variable r=%s, answer=%s" % (r, area))
    cprint.info(_("The area is: %s" % area))
def semicircle():
    from area import semicircle as semi
    r = float(input(_("What is the radius of the semicircle? ")))
    area = semi(r)
    logging.info("User used Semicircle area with variable r=%s, answer=%s" % (r, area))
    cprint.info(_("The area is: %s" % area))
def sector():
    r = float(input(_("What is the radius of the circular sector? ")))
    a = float(input(_("What is the angle of the circular sector *in degrees*? ")))
    area = cirsector(r, a)
    logging.info("User used Cirsector area with variable r=%s, a=%s answer=%s" % (r, a, area))
    cprint.info(_("The area is: %s" % area))
def ring():
    from area import ring as myprecious
    ro = float(input(_("What is the radius of the outer circle? ")))
    rs = float(input(_("What is the radius of the inner circle? ")))
    area = myprecious(ro, rs)
    logging.info("User used Ring area with variable ro=%s, rs=%s answer=%s" % (ro, rs, area))
    cprint.info(_("The area is: %s" % area))
def ellipse():
    from area import ellipse as el
    a = float(input(_("What is the length of the major axis? ")))
    b = float(input(_("What is the length of the minor axis? ")))
    area = el(a, b)
    logging.info("User used Ellipse area with variable a=%s, b=%s answer=%s" % (a, b, area))
    cprint.info(_("The area is: %s" % area))

def AreaMain():
    cprint.info(_('''Options:
1 - Equilateral triangle
2 - Right angle triangle
3 - Acute triangle
4 - Obtuse triangle
5 - Square
6 - Rectangle
8 - Parallelogram
9 - Rhombus
10 - Trapezium
11 - Circle
12 - Semicircle
13 - Circular sector
14 - Ring
15 - Ellipse'''))
    while True:
        try:
            choice = int(input(_("Please type one: ")))
        except (ValueError, TypeError):
            cprint.err(_("Please type an integer"))
            logging.error("User did ValueError // TypeError while inputting areaInteractive choice")
        if choice == 7:
            cprint.err(_("I was too lazy to change 7."))
            logging.info("Lazy 7")
        elif choice == 1:
            equ_triangle()
            break
        elif choice == 2:
            right_triangle()
            break
        elif choice == 3:
            acute_triangle()
            break
        elif choice == 4:
            obtuse_triangle()
            break
        elif choice == 5:
            square()
            break
        elif choice == 6:
            rectangle()
            break
        elif choice == 8:
            parallelogram()
            break
        elif choice == 9:
            rhombus()
            break
        elif choice == 10:
            trapezium()
            break
        elif choice == 11:
            circle()
            break
        elif choice == 12:
            semicircle()
            break
        elif choice == 13:
            sector()
            break
        elif choice == 14:
            ring() #my precious!
            break
        elif choice == 15:
            ellipse()
            break
if __name__ == "__main__":
    def _(thestring):
        return thestring
    AreaMain()
