"""
Just a small module to call mathmod's functions and then parse the results.
"""

def main(Comandeer):
    globals()['_'] = Commandeer

import mathmod
from modules.cprint import cprint
import logging

class Builtins: 
    def getInput():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try: 
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the two numbers was not a number. (Dump: n1=%s, n2=%s)") % (n1, n2))
        return (n1, n2)

class theBasics:
    def addition():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.addition(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.subtraction(n1, n2)
        except ValueError as ename:
            logging.error("While parsing sub(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.multiplication(n1, n2)
        except ValueError as ename:
            logging.error("While parsing multi(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.division(n1, n2)
        except ZeroDivisionError:
            logging.error("User decided to divide by zero.")
            raise SyntaxError("yes, because dividing %s cookie(s) for %s friend(s) makes sense") % (n1, n2)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing div(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed division with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def mod(): #modulo
        n1, n2 = Builtins.getInput()
        result = mathmod.Misc.modulo(n1, n2)
        cprint.info(_("\nThat equals...\n%s\n") % result)
        logging.info("User attempted to modulo numbers %s and %s, and got result %s" % result)
class rootsAndTheOtherOne:
    def curoot():
        try:
            number = float(input(_("Number to be rooted? ")))
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)") % (n1, n2))
        try:
            nothernumber = mathmod.RootsAndExponents.cuRoot(number)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {"number": number, "error": ename})
            raise
        logging.info("Parsed curoot(%s) to get %s..." % (number, nothernumber))
        cprint.info(_("The answer is... %s") % nothernumber)
    def powerful():
        origin = input(_("Enter the original number: "))
        ex = input(_("Enter the exponent: "))
        try:
            float(origin)
            float(ex)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: origin=%s, ex=%s)") % (origin, ex))
        try:
            returnedNumber = mathmod.RootsAndExponents.exponent(origin, ex)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {"number": number, "error": ename})
            raise
        cprint.info(_("The answer is... %s") % returnedNumber)
        logging.info("User exponented number %s with %s, getting %s" % (origin, ex, returnedNumber))
    def sqroot():
        num = float(input(_("Number to be rooted?")))
        returnedNumber = mathmod.RootsAndExponents.sqRoot(num)
        cprint.info(_("That equals... %s") % returnedNumber)
        logging.info("user sqrooted number %s" % (returnedNumber))

class misc:
    def h():
        cprint.info(_('''
Current list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, "ord'ing", and convert bases (aka number systems). Type quit to quit.
Bugs? Head on over to https://github.com/thetechrobo/python-text-calculator/
To contribute: go to https://github.com/thetechrobo/python-text-calculator/
        '''))
    def vol():
        logging.warning("User ran `volume.py'. Log is barely tested for area and volume.")
        Volume.VolMain()
    def area():
        logging.warning("User ran `area.py'. Log is barely tested for area and volume.")
        Area.AreaMain()
    def fib():
        hi = input(_("Would you like...\n    1 - Calculate a fixed amount of fibonacci numbers.\n    2 - Calculate fibonacci indefinitely.\nType: "))
        if hi[0] == "1":
            cprint.info(_("Fixed it is."))
            from mathmod.fibonacci import CalculateFixedFibo
            amount = int(input(_("How many numbers of fibonacci would you like to calculate? ")))
            logging.info("About to run fixed fibonacci (amount=%s)" % amount)
            finalProduct = CalculateFixedFibo(amount)
            cprint.info(_("Your fibonacci numbers were..."))
            cprint.ok(finalProduct)
            logging.info("User did fixed fibo with amount of %s, and the results are in the next log entry!..." % amount)
            logging.info(finalProduct)
        else:
            cprint.info(_("Looped it is."))
            from mathmod.fibonacci import CalculateLoopedFibo
            logging.info("About to run looped fibonacci")
            cprint.ok(_("Press Control-C to stop."))
            try:
                CalculateLoopedFibo()
            except Exception as ename:
                logging.err("Exception %s in looped fibonacci" % ename)
                cprint.err(_("An error occured."))
            except KeyboardInterrupt:
                logging.info("Exited fibonacci loop.")
        logging.info("User ran fibonacci function")
    def showUserWhatIThink(whatDOyouthink):
        cprint.ok(_("I think you want me to: \n%s") % whatDOyouthink)
        isItCorrect = input(_("Is this correct? (Y/n)")).lower()
        if _("y") in isItCorrect:
            logging.info("Palc chose the right calculation (%s) for calc choice that should be shown above." % whatDOyouthink)
        elif "n" in isItCorrect:
            cprint.info(_("Try different wording. Or, if you want that calculation choice to be made right, file a ticket."))
            if _("y") in input(_("Would you like to file a ticket? (Y/n)\nType: ")).lower(): 
                import webbrowser
                webbrowser.open("http://github.com/thetechrobo/python-text-calculator/issues/new")
                logging.info("User chose to file a ticket because they didn't want Palc to %s" % whatDOyouthink)
                input(_("Press ENTER to continue..."))
                cprint.info(_("Proceeding with the function I thought it was."))
            else:
                cprint.info(_("OK, proceeding with the function I thought it was."))
        else:
            cprint.info(_("Defaulting to yes."))
            logging.info("Defaulting to yes for right calc (%s) for calc choice that should be shown above" % whatDOyouthink)
class Temperature:
    def tempCalc():
        message = """What is the %s temperature unit? 
    1 - Farenheit
    2 - Celsius
    3 - Kelvin
    4 - Rankine
                                                   \033[A\033[A\033[A\033[A\033[A"""
        source = int(input(_(message) % "source"))
        origin = float(input(_("Please enter the original temperature...")))
        destination = int(input(_(message % "destination")))
        print("                  ")
        try:
            yolo = mathmod.Misc.calculateTemperature(origin=origin, source=source, destination=destination)
        except ValueError:
            cprint.err(_("Invalid input(s)."))
            logging.error("User typed invalid temperature answer %s, %s" % (source, destination))
        cprint.info(_("That equals... \n%s                       ") % yolo)
        logging.info("User ran temperature calculator, with source %s, destination %s, and original number %s" % (source, destination, origin))
class Percentage:
    def percentage1():
        origin = float(input(_("What is the ORIGINAL NUMBER? ")))
        percent = float(input(_("What is the PERCENTAGE? ")))
        logging.info("Got percentage RN origin %s percent %s" % (origin, percent))
        cprint.info(_("That equals..."))
        try:
            cprint.info(mathmod.Misc.whatIsXPercentOf(percent, origin))
        except ValueError:
            cprint.err(_("You requested an impossible situation by entering 0 there - that would require division by 0."))
    def percentage2():
        origin = float(input(_("What is the number that would be 100%? ")))
        part = float(input(_("What is the number that you want to convert to percentage (i.e. this number out of the number that would be 100%)? ")))
        logging.info("Got percentage RN origin %s and %s" % (origin, part))
        cprint.info(_("That equals..."))
        try:
            cprint.info(mathmod.Misc.findPercentage(part, origin))
        except ValueError:
            cprint.err(_("You requested an impossible situation by entering 0 there - that would require division by 0."))
    def chooseOneTwo():
        chosenPercentageCalc = int(input(_('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage (i.e. how much percent of ___ is ___?).
Type: ''')))
        if chosenPercentageCalc == 1:
            Percentage.percentage1()
        elif chosenPercentageCalc == 2:
            Percentage.percentage2()
        else:
            cprint.err(_("You didn't type a valid answer. Abort."))
            logging.info("User did not answer correct percentage interpretation")

class Tax:
    def taxCalc():
        cprint.info(_('''1 - Ontario Sales Tax
2 - Quebec Sales Tax
3 - Yukon, Northwest Territories, Nunavut, and Alberta Sales Tax
4 - BC / Manitoba Sales Tax
5 - New Brunswick / Nova Scotia / Newfoundland / PEI Sales Tax
6 - Saskatchewan Sales Tax
7 - Custom Tax'''))
        whatPlace = int(input(_("Choose one: ")))
        if whatPlace == 1:
            percent = 13.0
        elif whatPlace == 2:
            percent = 14.975
        elif whatPlace == 3:
            percent = 5.0
        elif whatPlace == 4:
            percent = 12.0
        elif whatPlace == 5:
            percent = 15.0
        elif whatPlace == 6:
            percent = 11.0
        elif whatPlace == 7:
            percent = float(input(_("Please enter the tax percentage without the percent sign: ")))
        else:
            cprint.err(_("You did not type answer. Abort."))
            logging.error("User typed %s into tax...aka an invalid answer." % whatPlace)
            return
        originPrice = float(input(_("What is the original price (before tax)? ")))
        result = mathmod.Misc.tax(originPrice, percent)
        logging.info("User used Sales Tax %s Percent with originPrice %s, price %s" % (percent, originPrice, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % result))

def logarithm(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    while True:
        base = input(_("1 - Base 10\n2 - Natural (e) logarithm\nPick one: "))
        number = float(input(_("What is the number? ")))
        if base[0] == "1":
            result = mathmod.Misc.log(number, False)
            cprint.info(_("The result is... %s") % result)
            doNotLog = False
            break
        elif base[0] == "2":
            result = mathmod.Misc.log(number, True)
            cprint.info(_("The result is... %s") % result)
            doNotLog = False
            break
        else:
            cprint.err(_("The logarithm you typed is not available."))
            cprint.ok(_("Try again."))
            logging.info("User attempted to use a logarithm that is unavailable.")
            doNotLog = True
    if not doNotLog:
        logging.info("User used logarithm choice %s with number %s, getting a result of %s" % (base, number, result))

def base():
    cprint.info(_("Please wait a moment."))
    from modules.pythonradix import Converter
    cprint.info(_("Please enter the original base.\n\
HINT: Base 2 is binary, base 8 is octal, base 10 is decimal (normal), and base 16 is hex."))
    originalBase = int(input(_("Enter your choice: ")))
    cprint.info(_("Please enter the destination base.\n\
Again, base 2 is binary, 8 is octal, 10 is normal, and 16 is hex."))
    destinationBase = int(input(_("Enter your choice: ")))
    cprint.ok(_("Please wait a moment."), end="")
    converter = Converter(originalBase, destinationBase)
    number = input(_("\rPlease enter your original number - it should not have a decimal point. "))
    try:
        result = converter.convert(number)
    except Exception as ename:
        cprint.err(_("Your number was messed up, or maybe Palc screwed it up, or maybe python-radix is buggy.\nMake sure that you didn't include things like `0b' for"
                     "binary calculation. So instead of `0b100111' being your input, try `100111' instead."))
        logging.info("ERROR during base conversion! %s" % ename)
        return
    cprint.info(_("The result is... %s") % result)
    logging.info("Base conversion done, with origin base %s, des base %s, and origin number %s" % (originalBase, destinationBase, number))
    
class Memory:
    """the two memory functions will be moved here "later" but not right now."""

def readMyMemory():
    cprint.info(_("This is the remember function.\nIt will read a number that was previously stored in a file."))
    try:
        slot = str(int(input(_("What slot number did you use? "))))
        with open(slot, "r") as memory:
            theMem = memory.read()
            cprint.info(_("Number: %s" % theMem))
            logging.info("Retrieved number %s from memory slot %s" % (theMem, slot))
    except Exception as e:
        logging.info("There was an error retrieving the file from memory. (Err %s)" % e)
        cprint.err(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file? "
        "Do you have the correct permissions?"))
def remember():
    cprint.info(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info("Saved number %s to memory slot %s" % (toRemember, slot))

def calculateInterest(): 
    origin = int(input(_("What is the original number? ")))
    rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
    print()
    units = int(input(_('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
    number = mathmod.Misc.calculateInterest(units, rate, origin)
    logging.info("INTERESTCALC: origin: %s rate: %s howMany: %s answer: %s" % (origin, rate, units, number))
    cprint.info(_("The answer is: \n%s" % number))

class Area:
    class choices: #readability
        EQUILATERAL_TRIANGLE = 1
        RIGHT_ANGLE_TRIANGLE = 2
        ACUTE_TRIANGLE = 3
        OBTUSE_TRIANGLE = 4
        SQUARE = 5
        RECTANGLE = 6
        EVIL = 7
        PARALLELOGRAM = 8
        RHOMBUS = 9
        TRAPEZIUM = 10
        CIRCLE = 11
        SEMICIRCLE = 12
        CIRCULAR_SECTOR = 13
        RING = 14
        ELLIPSE = 15
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
            if choice == Area.choices.EVIL:
                cprint.err(_("I was too lazy to change 7."))
                logging.info("Lazy 7")
            elif choice == Area.choices.EQUILATERAL_TRIANGLE:
                from mathmod.area import area_equilateral_triangle as equtri
                a = float(input(_("What length is the side of the triangle? ")))
                area = equtri(a)
                logging.info("User used equalateral triangle area with origin %s answer %s" % (a, area))
            elif choice == Area.choices.RIGHT_ANGLE_TRIANGLE:
                from mathmod.area import area_right_triangle as righttri
                b = float(input(_("What length is the base of the triangle? ")))
                h = float(input(_("What length is the height of the triangle? ")))
                area = righttri(b=b, h=h)
                logging.info("User used Righttri area with variable b=%s, h=%s, answer=%s" % (b, h, area))
            elif choice == Area.choices.ACUTE_TRIANGLE:
                from mathmod.area import area_acute_triangle as actri
                a = float(input(_("What is the length of the first side? ")))
                b = float(input(_("what is the length of the second side? ")))
                c = float(input(_("What is the length of the third side? ")))
                area = actri(a, b, c)
                logging.info("User used Acutetri area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area)) 
            elif choice == Area.choices.OBTUSE_TRIANGLE:
                from mathmod.area import area_obtuse_triangle as obtri
                a = float(input(_("What is the length of the first side? ")))
                b = float(input(_("What is the length of the second side? ")))
                c = float(input(_("What is the length of the third side? ")))
                area = obtri(a, b, c)
                logging.info("User used Obtuse Triangle area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area))
            elif choice == Area.choices.SQUARE:
                from mathmod.area import area_square as sq
                a = float(input(_("What is the length of the side of the square? ")))
                area = sq(a)
                logging.info("User used Square area with variable a=%s, answer=%s" % (a, area))
            elif choice == Area.choices.RECTANGLE:
                from mathmod.area import area_rectangle as rec
                l = float(input(_("What is the length of the rectangle? ")))
                b = float(input(_("What is the height of the rectangle? ")))
                area = rec(l, b)
                logging.info("User used Rectangle area with variable l=%s, b=%s, answer=%s" % (l, b, area))
            elif choice == Area.choices.PARALLELOGRAM:
                from mathmod.area import area_parallelogram as para
                b = float(input(_("What is the length of the base? ")))
                h = float(input(_("What is the height of the shape? ")))
                area = para(b, h)
                logging.info("User used Parallelogram area with variable b=%s, h=%s, answer=%s" % (b, h, area))
            elif choice == Area.choices.RHOMBUS:
                from mathmod.area import area_rhombus as rhombu
                do = float(input(_("What is the length of the first diagonal? ")))
                ds = float(input(_("What is the length of the 2nd diagonal? ")))
                area = rhombu(do, ds)
                logging.info("User used Rhombus area with variable do=%s, ds=%s, answer=%s" % (do, ds, area))
            elif choice == Area.choices.TRAPEZIUM:
                from mathmod.area import area_trapezium as trapezi
                a = float(input(_("What is the length of the 1st set of parallel sides? ")))
                b = float(input(_("What is the length of the 2nd set of parallel sides? ")))
                h = float(input(_("What is the height of the trapezium? ")))
                area = trapezi(a, b, h)
                logging.info("User used Trapezium area with variable a=%s, b=%s, h=%s, answer=%s" % (a, b, h, area))
            elif choice == Area.choices.CIRCLE:
                from mathmod.area import area_circle as circl
                r = float(input(_("What is the radius of the circle? ")))
                area = circl(r)
                logging.info("User used Circle area with variable r=%s, answer=%s" % (r, area))
            elif choice == Area.choices.SEMICIRCLE:
                from mathmod.area import area_semicircle as semi
                r = float(input(_("What is the radius of the semicircle? ")))
                area = semi(r)
                logging.info("User used Semicircle area with variable r=%s, answer=%s" % (r, area))
            elif choice == Area.choices.CIRCULAR_SECTOR:
                from mathmod.area import area_circular_sector as cirsector
                r = float(input(_("What is the radius of the circular sector? ")))
                a = float(input(_("What is the angle of the circular sector *in degrees*? ")))
                area = cirsector(r, a)
                logging.info("User used Cirsector area with variable r=%s, a=%s answer=%s" % (r, a, area))
            elif choice == Area.choices.RING: #my precious!
                from mathmod.area import area_ring as myprecious
                ro = float(input(_("What is the radius of the outer circle? ")))
                rs = float(input(_("What is the radius of the inner circle? ")))
                area = myprecious(ro, rs)
                logging.info("User used Ring area with variable ro=%s, rs=%s answer=%s" % (ro, rs, area))
            elif choice == Area.choices.ELLIPSE:
                from mathmod.area import area_ellipse as el
                a = float(input(_("What is the length of the major axis? ")))
                b = float(input(_("What is the length of the minor axis? ")))
                area = el(a, b)
                logging.info("User used Ellipse area with variable a=%s, b=%s answer=%s" % (a, b, area))
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: 
                cprint.info(_("The area is: %s") % volume)
                break

class Volume:
    class choices: #readability
        CUBE = 1
        CUBOID = 2
        CYLINDER = 3
        HOLLOW_CYLINDER= 4
        CONE = 5
        SPHERE = 6
        EVIL = 7
        HOLLOW_SPHERE = 8
        TRIANGULAR_PRISM = 9
        PENTAGONAL_PRISM = 10
        HEXAGONAL_PRISM = 11
        SQUARE_BASED_PYRAMID = 12
        TRIANGULAR_PYRAMID = 13
        PENTAGON_BASED_PYRAMID = 14
        HEXAGON_BASED_PYRAMID = 15
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
            if choice == Volume.choices.EVIL:
                cprint.ok("Sorry, that was not an option. >:)")
                logging.info(">:) choice 7")
            elif choice == Volume.choices.CUBE:
                from mathmod.volume import vol_cube
                a = float(input(_("What length is the side of the cube? ")))
                volume = vol_cube(a)
                logging.info("User ran Cuvolu(m) a=%s answer=%s" % (a, volume))
            elif choice == Volume.choices.CUBOID:
                from mathmod.volume import vol_cuboid
                b = float(input(_("What length is the breadth of the cuboid? ")))
                h = float(input(_("What length is the height of the cuboid? ")))
                l = float(input(_("What length is the cuboid? ")))
                volume = vol_cuboid(b=b, h=h, l=l)
                logging.info("User ran Cuboid Volume l=%s b=%s h=%s answer=%s" % (l, b, h, volume))
            elif choice == Volume.choices.CYLINDER:
                from mathmod.volume import vol_cylinder
                r = float(input(_("What is the radius of the cylinder? ")))
                h = float(input(_("What is the height of the cylinder? ")))
                volume = vol_cylinder(r=r, h=h)
                logging.info("User ran Cylinder Volume r=%s h=%s answer=%s" % (r, h, volume))
            elif choice == Volume.choices.HOLLOW_CYLINDER:
                from mathmod.volume import vol_hollow_cylinder
                ro = float(input(_("What is the radius of the hollow space? ")))
                rs = float(input(_("What is the radius of the cylinder? ")))
                h = float(input(_("What is the height of the cylinder? ")))
                volume = vol_hollow_cylinder(ro=ro, rs=rs, h=h)
                logging.info("User ran Hollowcylinder Volume ro=%s rs=%s h=%s answer=%s" % (ro, rs, h, volume))
            elif choice == Volume.choices.CONE:
                from mathmod.volume import vol_cone
                r = float(input(_("What is the radius of the cone? ")))
                h = float(input(_("What is the height of the cone? ")))
                volume = vol_cone(r=r, h=h)
                logging.info("User ran Conevol r=%s h=%s answer=%s" % (r, h, volume))
            elif choice == Volume.choices.SPHERE:
                from mathmod.volume import vol_sphere
                r = float(input(_("What is the radius of the sphere? ")))
                volume = vol_sphere(r)
                logging.info("User ran sphere Volume r=%s answer=%s" % (r, volume))
            elif choice == Volume.choices.HOLLOW_SPHERE:
                from mathmod.volume import vol_hollow_sphere
                ro = float(input(_("What is the radius of the sphere? ")))
                rs = float(input(_("What is the radius of the hollow space? ")))
                volume = vol_hollow_sphere(ro=ro, rs=rs)
                logging.info("User ran Hollowsphere Volume ro=%s rs=%s answer=%s" % (ro, rs, volume))
            elif choice == Volume.choices.TRIANGULAR_PRISM:
                from mathmod.volume import vol_tri_prism
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the prism? ")))
                volume = vol_tri_prism(a=a, h=h)
                logging.info("User ran Triangle Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.PENTAGONAL_PRISM:
                from mathmod.volume import vol_penta_prism
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the prism? ")))
                volume = vol_penta_prism(a=a, h=h)
                logging.info("User ran PentaPrism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.HEXAGONAL_PRISM:
                from mathmod.volume import vol_hexa_prism
                a = float(input(_("What is the length of the side of the hexagon? ")))
                h = float(input(_("What is the height of the prism? ")))
                volume = vol_hexa_prism(a=a, h=h)
                logging.info("User ran Hexagon Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.SQUARE_BASED_PYRAMID:
                from mathmod.volume import vol_sqr_pyramid
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the pyramid? ")))
                volume = vol_sqr_pyramid(a=a, h=h)
                logging.info("User ran Square Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.TRIANGULAR_PYRAMID:
                from mathmod.volume import vol_tri_pyramid
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the pyramid? ")))
                volume = vol_tri_pyramid(a=a, h=h)
                logging.info("User ran Triangle Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.PENTAGON_BASED_PYRAMID:
                from mathmod.volume import vol_penta_pyramid
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the pyramid? ")))
                volume = vol_penta_pyramid(a=a, h=h)
                logging.info("User ran Pentapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.HEXAGON_BASED_PYRAMID:
                from mathmod.volume import vol_hexa_pyramid
                a = float(input(_("What is the length of the side of the base? ")))
                h = float(input(_("What is the height of the pyramid? ")))
                volume = vol_hexa_pyramid(a=a, h=h)
                logging.info("User ran Hexapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: 
                cprint.info(_("The volume is: %s") % volume)
                break

if __name__ == "__main__":
    print("Please don't run this file directly, it can only be used with Palc")
    try:
        import runpy
        runpy.run_path(path_name="palc.py")
    finally:
        print("Next time, run palc.py rather than this file.")
