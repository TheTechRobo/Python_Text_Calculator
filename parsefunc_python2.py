u"""
Just a small module to call mathmod's functions and then parse the results.
"""

from __future__ import with_statement
from __future__ import absolute_import
from io import open
def main(Comandeer):
    globals()[u'_'] = Commandeer

import mathmod
from modules.cprint import cprint
import logging

class Builtins(object): 
    def getInput():
        n1 = raw_input(_(u"Please enter the first number: "))
        n2 = raw_input(_(u"Please enter the second number: "))
        try: 
            float(n1)
            float(n2)
        except Exception, ename:
            cprint.err(_(u"ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_(u"ERRID3: One or more of the two numbers was not a number. (Dump: n1=%s, n2=%s)") % (n1, n2))
        return (n1, n2)

class theBasics(object):
    def addition():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.addition(n1, n2)
        except ValueError, ename:
            logging.error(u"While parsing add(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {u"n1": n1, u"n2": n2, u"error": ename})
            cprint.info(_(u"An exception was raised!\nValueError\n"))
            raise
        cprint.info(_(u"The response is...%s") % returnedNumber)
        logging.info(u"Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.subtraction(n1, n2)
        except ValueError, ename:
            logging.error(u"While parsing sub(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {u"n1": n1, u"n2": n2, u"error": ename})
            cprint.info(_(u"An exception was raised!\nValueError\n"))
            raise
        cprint.info(_(u"The response is...%s") % returnedNumber)
        logging.info(u"Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.multiplication(n1, n2)
        except ValueError, ename:
            logging.error(u"While parsing multi(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {u"n1": n1, u"n2": n2, u"error": ename})
            cprint.info(_(u"An exception was raised!\nValueError\n"))
            raise
        cprint.info(_(u"The response is...%s") % returnedNumber)
        logging.info(u"Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.Arithmetic.division(n1, n2)
        except ZeroDivisionError:
            logging.error(u"User decided to divide by zero.")
            raise SyntaxError(u"yes, because dividing %s cookie(s) for %s friend(s) makes sense") % (n1, n2)
        except ValueError, ename:
            cprint.err(_(u"An exception was raised!\nValueError\n"))
            logging.error(u"While parsing div(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {u"n1": n1, u"n2": n2, u"error": ename})
            raise
        cprint.info(_(u"The response is...%s") % returnedNumber)
        logging.info(u"Parsed division with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def mod(): #modulo
        n1, n2 = Builtins.getInput()
        result = mathmod.Misc.modulo(n1, n2)
        cprint.info(_(u"\nThat equals...\n%s\n") % result)
        logging.info(u"User attempted to modulo numbers %s and %s, and got result %s" % result)
class rootsAndTheOtherOne(object):
    def curoot():
        try:
            number = float(raw_input(_(u"Number to be rooted? ")))
        except Exception, ename:
            cprint.err(_(u"ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_(u"ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)") % (n1, n2))
        try:
            nothernumber = mathmod.RootsAndExponents.cuRoot(number)
        except ValueError, ename:
            cprint.err(_(u"An exception was raised!\nValueError\n"))
            logging.error(u"While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {u"number": number, u"error": ename})
            raise
        logging.info(u"Parsed curoot(%s) to get %s..." % (number, nothernumber))
        cprint.info(_(u"The answer is... %s") % nothernumber)
    def powerful():
        origin = raw_input(_(u"Enter the original number: "))
        ex = raw_input(_(u"Enter the exponent: "))
        try:
            float(origin)
            float(ex)
        except Exception, ename:
            cprint.err(_(u"ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_(u"ERRID3: One or more of the numbers was not a number. (Dump: origin=%s, ex=%s)") % (origin, ex))
        try:
            returnedNumber = mathmod.RootsAndExponents.exponent(origin, ex)
        except ValueError, ename:
            cprint.err(_(u"An exception was raised!\nValueError\n"))
            logging.error(u"While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {u"number": number, u"error": ename})
            raise
        cprint.info(_(u"The answer is... %s") % returnedNumber)
        logging.info(u"User exponented number %s with %s, getting %s" % (origin, ex, returnedNumber))
    def sqroot():
        num = float(raw_input(_(u"Number to be rooted?")))
        returnedNumber = mathmod.RootsAndExponents.sqRoot(num)
        cprint.info(_(u"That equals... %s") % returnedNumber)
        logging.info(u"user sqrooted number %s" % (returnedNumber))

class misc(object):
    def h():
        cprint.info(_(u"\nCurrent list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, "
                      u"tax calculator, spinner, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, \"ord'ing\", and convert "
                      u"bases (aka number systems). Type quit to quit."
                      u"Bugs? Head on over to https://github.com/thetechrobo/python-text-calculator/issues"
                      u"To contribute: go to https://github.com/thetechrobo/python-text-calculator/"))
    def vol():
        logging.warning(u"User ran `volume.py'.")
        Volume.VolMain()
    def area():
        logging.warning(u"User ran `area.py'.")
        Area.AreaMain()
    def fib():
        hi = raw_input(_(u"Would you like...\n    1 - Calculate a fixed amount of fibonacci numbers.\n    2 - Calculate fibonacci indefinitely.\nType: "))
        if hi[0] == u"1":
            cprint.info(_(u"Fixed it is."))
            from mathmod.fibonacci import CalculateFixedFibo
            amount = int(raw_input(_(u"How many numbers of fibonacci would you like to calculate? ")))
            logging.info(u"About to run fixed fibonacci (amount=%s)" % amount)
            finalProduct = CalculateFixedFibo(amount)
            cprint.info(_(u"Your fibonacci numbers were..."))
            cprint.ok(finalProduct)
            logging.info(u"User did fixed fibo with amount of %s, and the results are in the next log entry!..." % amount)
            logging.info(finalProduct)
        else:
            cprint.info(_(u"Looped it is."))
            from mathmod.fibonacci import CalculateLoopedFibo
            logging.info(u"About to run looped fibonacci")
            cprint.ok(_(u"Press Control-C to stop."))
            try:
                CalculateLoopedFibo()
            except Exception, ename:
                logging.err(u"Exception %s in looped fibonacci" % ename)
                cprint.err(_(u"An error occured."))
            except KeyboardInterrupt:
                logging.info(u"Exited fibonacci loop.")
        logging.info(u"User ran fibonacci function")
    def showUserWhatIThink(whatDOyouthink):
        cprint.ok(_(u"I think you want me to: \n%s") % whatDOyouthink)
        isItCorrect = raw_input(_(u"Is this correct? (Y/n)")).lower()
        if _(u"y") in isItCorrect:
            logging.info(u"Palc chose the right calculation (%s) for calc choice that should be shown above." % whatDOyouthink)
        elif u"n" in isItCorrect:
            cprint.info(_(u"Try different wording. Or, if you want that calculation choice to be made right, file a ticket."))
            if _(u"y") in raw_input(_(u"Would you like to file a ticket? (Y/n)\nType: ")).lower(): 
                import webbrowser
                webbrowser.open(u"http://github.com/thetechrobo/python-text-calculator/issues/new")
                logging.info(u"User chose to file a ticket because they didn't want Palc to %s" % whatDOyouthink)
                raw_input(_(u"Press ENTER to continue..."))
                cprint.info(_(u"Proceeding with the function I thought it was."))
            else:
                cprint.info(_(u"OK, proceeding with the function I thought it was."))
        else:
            cprint.info(_(u"Defaulting to yes."))
            logging.info(u"Defaulting to yes for right calc (%s) for calc choice that should be shown above" % whatDOyouthink)
    def readMyMemory():
        cprint.info(_(u"This is the remember function.\nIt will read a number that was previously stored in a file."))
        try:
            slot = unicode(int(raw_input(_(u"What slot number did you use? "))))
            with open(slot, u"r") as memory:
                theMem = memory.read()
                cprint.info(_(u"Number: %s" % theMem))
                logging.info(u"Retrieved number %s from memory slot %s" % (theMem, slot))
        except Exception, e:
            logging.info(u"There was an error retrieving the file from memory. (Err %s)" % e)
            cprint.err(_(u"There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file? "
            u"Do you have the correct permissions?"))
    def remember():
        cprint.info(_(u"This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
        toRemember = float(raw_input(_(u"\nPlease enter the number to be saved: ")))
        slot = unicode(int(raw_input(_(u"What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
        toRemember = unicode(toRemember)
        memory = open(slot, u"w+")
        memory.write(toRemember)
        logging.info(u"Saved number %s to memory slot %s" % (toRemember, slot))
    def calculateInterest(): 
        origin = int(raw_input(_(u"What is the original number? ")))
        rate = float(raw_input(_(u"What is the rate of interest in percentage (without the percent sign)? ")))
        print
        units = int(raw_input(_(u'''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
        number = mathmod.Misc.calculateInterest(units, rate, origin)
        logging.info(u"INTERESTCALC: origin: %s rate: %s howMany: %s answer: %s" % (origin, rate, units, number))
        cprint.info(_(u"The answer is: \n%s" % number))
    def base():
        cprint.info(_(u"Please wait a moment."))
        from modules.pythonradix import Converter
        cprint.info(_(u"Please enter the original base.\n\
HINT: Base 2 is binary, base 8 is octal, base 10 is decimal (normal), and base 16 is hex."))
        originalBase = int(raw_input(_(u"Enter your choice: ")))
        cprint.info(_(u"Please enter the destination base.\n\
Again, base 2 is binary, 8 is octal, 10 is normal, and 16 is hex."))
        destinationBase = int(raw_input(_(u"Enter your choice: ")))
        cprint.ok(_(u"Please wait a moment."), end=u"")
        converter = Converter(originalBase, destinationBase)
        number = raw_input(_(u"\rPlease enter your original number - it should not have a decimal point. "))
        try:
            result = converter.convert(number)
        except Exception, ename:
            cprint.err(_(u"Your number was messed up, or maybe Palc screwed it up, or maybe python-radix is buggy.\nMake sure that you didn't include things like `0b' for"
                        u"binary calculation. So instead of `0b100111' being your input, try `100111' instead."))
            logging.info(u"ERROR during base conversion! %s" % ename)
            return
        cprint.info(_(u"The result is... %s") % result)
        logging.info(u"Base conversion done, with origin base %s, des base %s, and origin number %s" % (originalBase, destinationBase, number))
    def logarithm(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
        base = raw_input(_(u"1 - Base 10\n2 - Natural (e) logarithm\nPick one: "))
        number = float(raw_input(_(u"What is the number? ")))
        if base[0] == u"1":
            result = mathmod.Misc.log(number, False)
            cprint.info(_(u"The result is... %s") % result)
            doNotLog = False
        elif base[0] == u"2":
            result = mathmod.Misc.log(number, True)
            cprint.info(_(u"The result is... %s") % result)
            doNotLog = False
        else:
            cprint.err(_(u"The logarithm you typed is not available."))
            cprint.ok(_(u"Try again."))
            logging.info(u"User attempted to use a logarithm that is unavailable.")
            doNotLog = True
        if doNotLog:
            return
        logging.info(u"User used logarithm choice %s with number %s, getting a result of %s" % (base, number, result))
    def spinner():
        choices = raw_input(_(u"Please enter your choices separated by commas. Example: First part of spinner, SecondPartOfSpinner, 3, 4, 5, 6, The End\nType: ")).strip().split(u", ") #https://www.w3schools.com/python/ref_string_split.asp
        times = int(raw_input(_(u"How many times to conduct the spinner? ")))
        output = mathmod.Misc.Spinner(times, choices)
        cprint.ok(_(u"Your results were...\n%s") % output)
        logging.info(u"Spinner: choices %s, times %s, output %s" % (choices, times, output))
class Temperature(object):
    def tempCalc():
        message = u"""What is the %s temperature unit? 
    1 - Farenheit
    2 - Celsius
    3 - Kelvin
    4 - Rankine
                                                   \033[A\033[A\033[A\033[A\033[A"""
        source = int(raw_input(_(message) % u"source"))
        origin = float(raw_input(_(u"Please enter the original temperature...")))
        destination = int(raw_input(_(message % u"destination")))
        print u"                  "
        try:
            yolo = mathmod.Misc.calculateTemperature(origin=origin, source=source, destination=destination)
        except ValueError:
            cprint.err(_(u"Invalid input(s)."))
            logging.error(u"User typed invalid temperature answer %s, %s" % (source, destination))
        cprint.info(_(u"That equals... \n%s                       ") % yolo)
        logging.info(u"User ran temperature calculator, with source %s, destination %s, and original number %s" % (source, destination, origin))
class Percentage(object):
    def percentage1():
        origin = float(raw_input(_(u"What is the ORIGINAL NUMBER? ")))
        percent = float(raw_input(_(u"What is the PERCENTAGE? ")))
        logging.info(u"Got percentage RN origin %s percent %s" % (origin, percent))
        cprint.info(_(u"That equals..."))
        try:
            cprint.info(mathmod.Misc.whatIsXPercentOf(percent, origin))
        except ValueError:
            cprint.err(_(u"You requested an impossible situation by entering 0 there - that would require division by 0."))
    def percentage2():
        origin = float(raw_input(_(u"What is the number that would be 100%? ")))
        part = float(raw_input(_(u"What is the number that you want to convert to percentage (i.e. this number out of the number that would be 100%)? ")))
        logging.info(u"Got percentage RN origin %s and %s" % (origin, part))
        cprint.info(_(u"That equals..."))
        try:
            cprint.info(mathmod.Misc.findPercentage(part, origin))
        except ValueError:
            cprint.err(_(u"You requested an impossible situation by entering 0 there - that would require division by 0."))
    def chooseOneTwo():
        chosenPercentageCalc = int(raw_input(_(u'''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage (i.e. how much percent of ___ is ___?).
Type: ''')))
        if chosenPercentageCalc == 1:
            Percentage.percentage1()
        elif chosenPercentageCalc == 2:
            Percentage.percentage2()
        else:
            cprint.err(_(u"You didn't type a valid answer. Abort."))
            logging.info(u"User did not answer correct percentage interpretation")

class Tax(object):
    def taxCalc():
        cprint.info(_(u'''1 - Ontario Sales Tax
2 - Quebec Sales Tax
3 - Yukon, Northwest Territories, Nunavut, and Alberta Sales Tax
4 - BC / Manitoba Sales Tax
5 - New Brunswick / Nova Scotia / Newfoundland / PEI Sales Tax
6 - Saskatchewan Sales Tax
7 - Custom Tax'''))
        whatPlace = int(raw_input(_(u"Choose one: ")))
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
            percent = float(raw_input(_(u"Please enter the tax percentage without the percent sign: ")))
        else:
            cprint.err(_(u"You did not type answer. Abort."))
            logging.error(u"User typed %s into tax...aka an invalid answer." % whatPlace)
            return
        originPrice = float(raw_input(_(u"What is the original price (before tax)? ")))
        result = mathmod.Misc.tax(originPrice, percent)
        logging.info(u"User used Sales Tax %s Percent with originPrice %s, price %s" % (percent, originPrice, newPrice))
        cprint.info(_(u"After tax, the price is: \n%s" % result))

class Area(object):
    class choices(object): #readability
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
    selectionMessage = u'''Options:
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
15 - Ellipse'''
    def AreaMain():
        cprint.info(_(Area.selectionMessage))
        while True:
            try:
                choice = int(raw_input(_(u"Please type one: ")))
            except (ValueError, TypeError):
                cprint.err(_(u"Please type an integer"))
                logging.error(u"User did ValueError // TypeError while inputting areaInteractive choice")
            if choice == Area.choices.EVIL:
                cprint.err(_(u"I was too lazy to change 7."))
                logging.info(u"Lazy 7")
                area = u"NULL"
            elif choice == Area.choices.EQUILATERAL_TRIANGLE:
                from mathmod.area import area_equilateral_triangle as equtri
                a = float(raw_input(_(u"What length is the side of the triangle? ")))
                area = equtri(a)
                logging.info(u"User used equalateral triangle area with origin %s answer %s" % (a, area))
            elif choice == Area.choices.RIGHT_ANGLE_TRIANGLE:
                from mathmod.area import area_right_triangle as righttri
                b = float(raw_input(_(u"What length is the base of the triangle? ")))
                h = float(raw_input(_(u"What length is the height of the triangle? ")))
                area = righttri(b=b, h=h)
                logging.info(u"User used Righttri area with variable b=%s, h=%s, answer=%s" % (b, h, area))
            elif choice == Area.choices.ACUTE_TRIANGLE:
                from mathmod.area import area_acute_triangle as actri
                a = float(raw_input(_(u"What is the length of the first side? ")))
                b = float(raw_input(_(u"what is the length of the second side? ")))
                c = float(raw_input(_(u"What is the length of the third side? ")))
                area = actri(a, b, c)
                logging.info(u"User used Acutetri area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area)) 
            elif choice == Area.choices.OBTUSE_TRIANGLE:
                from mathmod.area import area_obtuse_triangle as obtri
                a = float(raw_input(_(u"What is the length of the first side? ")))
                b = float(raw_input(_(u"What is the length of the second side? ")))
                c = float(raw_input(_(u"What is the length of the third side? ")))
                area = obtri(a, b, c)
                logging.info(u"User used Obtuse Triangle area with variable a=%s, b=%s, c=%s, answer=%s" % (a, b, c, area))
            elif choice == Area.choices.SQUARE:
                from mathmod.area import area_square as sq
                a = float(raw_input(_(u"What is the length of the side of the square? ")))
                area = sq(a)
                logging.info(u"User used Square area with variable a=%s, answer=%s" % (a, area))
            elif choice == Area.choices.RECTANGLE:
                from mathmod.area import area_rectangle as rec
                l = float(raw_input(_(u"What is the length of the rectangle? ")))
                b = float(raw_input(_(u"What is the height of the rectangle? ")))
                area = rec(l, b)
                logging.info(u"User used Rectangle area with variable l=%s, b=%s, answer=%s" % (l, b, area))
            elif choice == Area.choices.PARALLELOGRAM:
                from mathmod.area import area_parallelogram as para
                b = float(raw_input(_(u"What is the length of the base? ")))
                h = float(raw_input(_(u"What is the height of the shape? ")))
                area = para(b, h)
                logging.info(u"User used Parallelogram area with variable b=%s, h=%s, answer=%s" % (b, h, area))
            elif choice == Area.choices.RHOMBUS:
                from mathmod.area import area_rhombus as rhombu
                do = float(raw_input(_(u"What is the length of the first diagonal? ")))
                ds = float(raw_input(_(u"What is the length of the 2nd diagonal? ")))
                area = rhombu(do, ds)
                logging.info(u"User used Rhombus area with variable do=%s, ds=%s, answer=%s" % (do, ds, area))
            elif choice == Area.choices.TRAPEZIUM:
                from mathmod.area import area_trapezium as trapezi
                a = float(raw_input(_(u"What is the length of the 1st set of parallel sides? ")))
                b = float(raw_input(_(u"What is the length of the 2nd set of parallel sides? ")))
                h = float(raw_input(_(u"What is the height of the trapezium? ")))
                area = trapezi(a, b, h)
                logging.info(u"User used Trapezium area with variable a=%s, b=%s, h=%s, answer=%s" % (a, b, h, area))
            elif choice == Area.choices.CIRCLE:
                from mathmod.area import area_circle as circl
                r = float(raw_input(_(u"What is the radius of the circle? ")))
                area = circl(r)
                logging.info(u"User used Circle area with variable r=%s, answer=%s" % (r, area))
            elif choice == Area.choices.SEMICIRCLE:
                from mathmod.area import area_semicircle as semi
                r = float(raw_input(_(u"What is the radius of the semicircle? ")))
                area = semi(r)
                logging.info(u"User used Semicircle area with variable r=%s, answer=%s" % (r, area))
            elif choice == Area.choices.CIRCULAR_SECTOR:
                from mathmod.area import area_circular_sector as cirsector
                r = float(raw_input(_(u"What is the radius of the circular sector? ")))
                a = float(raw_input(_(u"What is the angle of the circular sector *in degrees*? ")))
                area = cirsector(r, a)
                logging.info(u"User used Cirsector area with variable r=%s, a=%s answer=%s" % (r, a, area))
            elif choice == Area.choices.RING: #my precious!
                from mathmod.area import area_ring as myprecious
                ro = float(raw_input(_(u"What is the radius of the outer circle? ")))
                rs = float(raw_input(_(u"What is the radius of the inner circle? ")))
                area = myprecious(ro, rs)
                logging.info(u"User used Ring area with variable ro=%s, rs=%s answer=%s" % (ro, rs, area))
            elif choice == Area.choices.ELLIPSE:
                from mathmod.area import area_ellipse as el
                a = float(raw_input(_(u"What is the length of the major axis? ")))
                b = float(raw_input(_(u"What is the length of the minor axis? ")))
                area = el(a, b)
                logging.info(u"User used Ellipse area with variable a=%s, b=%s answer=%s" % (a, b, area))
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: 
                cprint.info(_(u"The area is: %s") % area)
                break

class Volume(object):
    selectionMessage = u'''Options:
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
15 - Hexagon-based pyramid'''
    class choices(object): #readability
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
        cprint.info(_(Volume.selectionMessage))
        while True:
            try:
                choice = int(raw_input(_(u"Please type one: ")))
            except (ValueError, TypeError), ename:
                cprint.err(u"Please type an integer")
                logging.error(u"User did a ValueError or TypeError while inputting choice in volinteractive (%s)" % ename)
            if choice == Volume.choices.EVIL:
                cprint.ok(u"Sorry, that was not an option. >:)")
                logging.info(u">:) choice 7")
                volume = u"NULL"
            elif choice == Volume.choices.CUBE:
                from mathmod.volume import vol_cube
                a = float(raw_input(_(u"What length is the side of the cube? ")))
                volume = vol_cube(a)
                logging.info(u"User ran Cuvolu(m) a=%s answer=%s" % (a, volume))
            elif choice == Volume.choices.CUBOID:
                from mathmod.volume import vol_cuboid
                b = float(raw_input(_(u"What length is the breadth of the cuboid? ")))
                h = float(raw_input(_(u"What length is the height of the cuboid? ")))
                l = float(raw_input(_(u"What length is the cuboid? ")))
                volume = vol_cuboid(b=b, h=h, l=l)
                logging.info(u"User ran Cuboid Volume l=%s b=%s h=%s answer=%s" % (l, b, h, volume))
            elif choice == Volume.choices.CYLINDER:
                from mathmod.volume import vol_cylinder
                r = float(raw_input(_(u"What is the radius of the cylinder? ")))
                h = float(raw_input(_(u"What is the height of the cylinder? ")))
                volume = vol_cylinder(r=r, h=h)
                logging.info(u"User ran Cylinder Volume r=%s h=%s answer=%s" % (r, h, volume))
            elif choice == Volume.choices.HOLLOW_CYLINDER:
                from mathmod.volume import vol_hollow_cylinder
                ro = float(raw_input(_(u"What is the radius of the hollow space? ")))
                rs = float(raw_input(_(u"What is the radius of the cylinder? ")))
                h = float(raw_input(_(u"What is the height of the cylinder? ")))
                volume = vol_hollow_cylinder(ro=ro, rs=rs, h=h)
                logging.info(u"User ran Hollowcylinder Volume ro=%s rs=%s h=%s answer=%s" % (ro, rs, h, volume))
            elif choice == Volume.choices.CONE:
                from mathmod.volume import vol_cone
                r = float(raw_input(_(u"What is the radius of the cone? ")))
                h = float(raw_input(_(u"What is the height of the cone? ")))
                volume = vol_cone(r=r, h=h)
                logging.info(u"User ran Conevol r=%s h=%s answer=%s" % (r, h, volume))
            elif choice == Volume.choices.SPHERE:
                from mathmod.volume import vol_sphere
                r = float(raw_input(_(u"What is the radius of the sphere? ")))
                volume = vol_sphere(r)
                logging.info(u"User ran sphere Volume r=%s answer=%s" % (r, volume))
            elif choice == Volume.choices.HOLLOW_SPHERE:
                from mathmod.volume import vol_hollow_sphere
                ro = float(raw_input(_(u"What is the radius of the sphere? ")))
                rs = float(raw_input(_(u"What is the radius of the hollow space? ")))
                volume = vol_hollow_sphere(ro=ro, rs=rs)
                logging.info(u"User ran Hollowsphere Volume ro=%s rs=%s answer=%s" % (ro, rs, volume))
            elif choice == Volume.choices.TRIANGULAR_PRISM:
                from mathmod.volume import vol_tri_prism
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the prism? ")))
                volume = vol_tri_prism(a=a, h=h)
                logging.info(u"User ran Triangle Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.PENTAGONAL_PRISM:
                from mathmod.volume import vol_penta_prism
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the prism? ")))
                volume = vol_penta_prism(a=a, h=h)
                logging.info(u"User ran PentaPrism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.HEXAGONAL_PRISM:
                from mathmod.volume import vol_hexa_prism
                a = float(raw_input(_(u"What is the length of the side of the hexagon? ")))
                h = float(raw_input(_(u"What is the height of the prism? ")))
                volume = vol_hexa_prism(a=a, h=h)
                logging.info(u"User ran Hexagon Prism Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.SQUARE_BASED_PYRAMID:
                from mathmod.volume import vol_sqr_pyramid
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the pyramid? ")))
                volume = vol_sqr_pyramid(a=a, h=h)
                logging.info(u"User ran Square Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.TRIANGULAR_PYRAMID:
                from mathmod.volume import vol_tri_pyramid
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the pyramid? ")))
                volume = vol_tri_pyramid(a=a, h=h)
                logging.info(u"User ran Triangle Pyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.PENTAGON_BASED_PYRAMID:
                from mathmod.volume import vol_penta_pyramid
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the pyramid? ")))
                volume = vol_penta_pyramid(a=a, h=h)
                logging.info(u"User ran Pentapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            elif choice == Volume.choices.HEXAGON_BASED_PYRAMID:
                from mathmod.volume import vol_hexa_pyramid
                a = float(raw_input(_(u"What is the length of the side of the base? ")))
                h = float(raw_input(_(u"What is the height of the pyramid? ")))
                volume = vol_hexa_pyramid(a=a, h=h)
                logging.info(u"User ran Hexapyramid Volume a=%s h=%s answer=%s" % (a, h, volume))
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: 
                cprint.info(_(u"The volume is: %s") % volume)
                break

if __name__ == u"__main__":
    print u"Please don't run this file directly, it can only be used with Palc"
    try:
        import runpy
        runpy.run_path(path_name=u"palc.py")
    finally:
        print u"Next time, run palc.py rather than this file."
