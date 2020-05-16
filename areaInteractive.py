from area import *
if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")
logging.info("User used areaInteractive...")
def equ_triangle():
    a = int(input(_("What length is the side of the triangle? ")))
    print(_("The area is: "))
    print(equtri(a))
def right_triangle():
    b = int(input(_("What length is the base of the triangle? ")))
    h = int(input(_("What length is the height of the triangle? ")))
    print(_("The area is: "))
    print(righttri(b, h))
def acute_triangle():
    a = int(input(_("What is the length of the first side? ")))
    b = int(input(_("what is the length of the second side? ")))
    c = int(input(_("What is the length of the third side? ")))
    print(_("The area is: "))
    print(actri(a, b, c))
def obtuse_triangle():
    a = int(input(_("What is the length of the first side? ")))
    b = int(input(_("what is the length of the second side? ")))
    c = int(input(_("What is the length of the third side? ")))
    print(_("The area is: "))
    print(obtri(a, b, c))
def square():
    a = int(input(_("What is the length of the side of the square? ")))
    print(_("The area is: "))
    print(sq(a))
def rectangle():
    from area import rectangle as rec
    l = int(input(_("What is the length of the rectangle? ")))
    b = int(input(_("What is the height of the rectangle? ")))
    print(_("The area is: "))
    print(rec(l, b))
def parallelogram():
    from area import parallelogram as para
    b = int(input(_("What is the length of the base? ")))
    h = int(input(_("What is the height of the shape? ")))
    print(_("The area is: "))
    print(para(b, h))
def rhombus():
    from area import rhombus as rhombu
    do = int(input(_("What is the length of the first diagonal? ")))
    ds = int(input(_("What is the length of the 2nd diagonal? ")))
    print(_("The area is: "))
    print(rhombu(do, ds))
def trapezium():
    from area import trapezium as trapezi
    a = int(input(_("What is the length of the 1st set of parallel sides? ")))
    b = int(input(_("What is the length of the 2nd set of parallel sides? ")))
    h = int(input(_("What is the height of the trapezium? ")))
    print(_("The area is: "))
    print(trapezi(a, b, h))
def circle():
    from area import circle as circl
    r = int(input(_("What is the radius of the circle? ")))
    print(_("The area is: "))
    print(circl(r))
def semicircle():
    from area import semicircle as semi
    r = int(input(_("What is the radius of the semicircle? ")))
    print(_("The area is: "))
    print(semi(r))
def sector():
    r = int(input(_("What is the radius of the circular sector? ")))
    a = int(input(_("What is the angle of the circular sector *in degrees*? ")))
    print(_("The area is: "))
    print(cirsector(r, a))
def ring():
    from area import ring as myprecious
    ro = int(input(_("What is the radius of the outer circle? ")))
    rs = int(input(_("What is the radius of the inner circle? ")))
    print(_("The area is: "))
    print(myprecious(ro, rs))
def ellipse():
    from area import ellipse as el
    a = int(input(_("What is the length of the major axis? ")))
    b = int(input(_("What is the length of the minor axis? ")))
    print(_("The area is: "))
    print(el(a, b))
print(_('''Options:
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
        print(_("Please type an integer"))
    if choice == 7:
        print(_("I was too lazy to change 7."))
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
        #print(_("I cannot figure out what variable `a' is for, line 182 in `area.py' if anyone wants to help"))
        break
    elif choice == 14:
        ring() #my precious!
        break
    elif choice == 15:
        ellipse()
        break
