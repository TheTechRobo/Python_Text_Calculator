from area import *
from cprint import cprint
import logging
logging.info("User used areaInteractive...")
def main(Comandeer):
    global _
    _ = Comandeer

def equ_triangle():
    a = int(input(_("What length is the side of the triangle? ")))
    cprint.info(_("The area is: %s" % equtri(a)))
def right_triangle():
    b = int(input(_("What length is the base of the triangle? ")))
    h = int(input(_("What length is the height of the triangle? ")))
    cprint.info(_("The area is: %s" % righttri(b=b, h=h)))
def acute_triangle():
    a = int(input(_("What is the length of the first side? ")))
    b = int(input(_("what is the length of the second side? ")))
    c = int(input(_("What is the length of the third side? ")))
    cprint.info(_("The area is: "))
    cprint.info(actri(a, b, c))
def obtuse_triangle():
    a = int(input(_("What is the length of the first side? ")))
    b = int(input(_("what is the length of the second side? ")))
    c = int(input(_("What is the length of the third side? ")))
    cprint.info(_("The area is: "))
    cprint.info(obtri(a, b, c))
def square():
    a = int(input(_("What is the length of the side of the square? ")))
    cprint.info(_("The area is: "))
    cprint.info(sq(a))
def rectangle():
    from area import rectangle as rec
    l = int(input(_("What is the length of the rectangle? ")))
    b = int(input(_("What is the height of the rectangle? ")))
    cprint.info(_("The area is: "))
    cprint.info(rec(l, b))
def parallelogram():
    from area import parallelogram as para
    b = int(input(_("What is the length of the base? ")))
    h = int(input(_("What is the height of the shape? ")))
    cprint.info(_("The area is: "))
    cprint.info(para(b, h))
def rhombus():
    from area import rhombus as rhombu
    do = int(input(_("What is the length of the first diagonal? ")))
    ds = int(input(_("What is the length of the 2nd diagonal? ")))
    cprint.info(_("The area is: "))
    cprint.info(rhombu(do, ds))
def trapezium():
    from area import trapezium as trapezi
    a = int(input(_("What is the length of the 1st set of parallel sides? ")))
    b = int(input(_("What is the length of the 2nd set of parallel sides? ")))
    h = int(input(_("What is the height of the trapezium? ")))
    cprint.info(_("The area is: "))
    cprint.info(trapezi(a, b, h))
def circle():
    from area import circle as circl
    r = int(input(_("What is the radius of the circle? ")))
    cprint.info(_("The area is: "))
    cprint.info(circl(r))
def semicircle():
    from area import semicircle as semi
    r = int(input(_("What is the radius of the semicircle? ")))
    cprint.info(_("The area is: "))
    cprint.info(semi(r))
def sector():
    r = int(input(_("What is the radius of the circular sector? ")))
    a = int(input(_("What is the angle of the circular sector *in degrees*? ")))
    cprint.info(_("The area is: "))
    cprint.info(cirsector(r, a))
def ring():
    from area import ring as myprecious
    ro = int(input(_("What is the radius of the outer circle? ")))
    rs = int(input(_("What is the radius of the inner circle? ")))
    cprint.info(_("The area is: "))
    cprint.info(myprecious(ro, rs))
def ellipse():
    from area import ellipse as el
    a = int(input(_("What is the length of the major axis? ")))
    b = int(input(_("What is the length of the minor axis? ")))
    cprint.info(_("The area is: "))
    cprint.info(el(a, b))

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
            logging.error("User did valueerror typeerror while inputting areaInteractive choice")
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
