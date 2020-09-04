"""
Just a small module to call mathmod's functions and then parse the results.
"""

def main(theThing):
    global _
    _ = theThing

from mathmod.func import *
from mathmod.basicfunc import *
from modules.cprint import cprint
import logging

class theBasics:
    def addition():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try: 
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the two numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = add(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try:
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number." % (n1, n2)))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = sub(n1, n2)
        except ValueError as ename:
            logging.error("While parsing sub(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try:
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = multi(n1, n2)
        except ValueError as ename:
            logging.error("While parsing multi(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try:
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = multi(n1, n2)
        except ZeroDivisionError:
            logging.error("User decided to divide by zero.")
            raise SyntaxError("yes, because dividing %s cookie(s) for %s friend(s) makes sense" % (n1, n2))
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing div(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
class rootsAndTheOtherOne:
    def curoot():
        try:
            number = float(input(_("Number to be rooted? ")))
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            nothernumber = cuRoot(number)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {"number": number, "error": ename})
            raise
        logging.info("Parsed curoot(%s) to get %s..." % (number, nothernumber))
        cprint.info(_("The answer is... %s") % nothernumber)
    def powerful():
        origin = input(_("Original number?"))
        ex = input(_("Exponent? "))
        try:
            float(origin)
            float(ex)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: origin=%s, ex=%s)" % (origin, ex)))
        try:
            returnedNumber = exponent(origin, ex)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {"number": number, "error": ename})
            raise
        cprint.info(_("The answer is... %s") % returnedNumber)
        logging.info("User exponented number %s with %s, getting %s" % (origin, ex, returnedNumber))
    def sqroot():
        num = float(input(_("Number to be rooted?")))
        returnedNumber = sqRoot(num)
        cprint.info(_("That equals... %s" % returnedNumber))
        logging.info("user sqrooted number %s" % (returnedNumber))

class misc:
    def h():
        cprint.info(_('''
Current list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, "ord'ing", and convert bases (aka number systems). Type quit to quit.
Bugs? Head on over to https://github.com/thetechrobo/support/
To contribute: go to https://github.com/thetechrobo/python-text-calculator/
        '''))
    def vol():
        logging.warning("User ran `volume.py'. Log is barely tested for area and volume.")
        VolMain()
    def area():
        logging.warning("User ran `area.py'. Log is barely tested for area and volume.")
        AreaMain()
    def fib():
        hi = int(input(_("Would you like...\n1 - Calculate a fixed amount of fibonacci numbers.\n2 - Calculate fibonacci indefinitely.")))
        if hi[0] == 1:
            cprint.info(_("Fixed it is."))
            from mathmod.fibonacci import CalculateFixedFibo
            amount = int(input(_("How many numbers of fibonacci would you like to calculate?")))
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
            CalculateLoopedFibo()
        logging.info("User ran fibonacci function")
    class Temperature:
        def tempCalc():
            message = "OPTIONS:\n    1 - Farenheit to Celsius\n    2 - Celsius to Farenheit\n    Farenheit to Kelvin\n    Celsius to Kelvin\n    Kelvin to Celsius\n    Kelvin to Farenheit\nType: "
            hi = int(input(_(message)))
            if hi == 1:
                hello = float(input(_("Please enter the FAHRENHEIT temperature: ")))
                #howdy = float(input(_("Please enter the CELSIUS temperature: ")))
                yolo = hello - 32
                yolo = yolo * 5/9
                cprint.info(_("That equals...\n%s" % yolo))
                logging.info("User did F to C with F=%s, result=%s" % (hello, yolo))
            elif hi == 2:
                howdy = float(input(_("Please enter the CELSIUS temperature: ")))
                yolo = howdy * 9/5
                yolo = yolo + 32
                cprint.info(_("That equals...\n%s" % yolo))
                logging.info("User did C to F with C=%s, result=%s" % (howdy, yolo))
            elif hi == 3:
                salut = float(input(_("Please enter the FAHRENHEIT temperature: ")))
                #convert to celsius
                yolo = salut - 32
                yolo = yolo * 5/9
                #convert from celsius to kelvin
                yolo = yolo + 273.15
                cprint.info(_("That equals...\n%s" % yolo))
            elif hi == 4:
                howdy = float(input(_("Please enter the CELSIUS temperature: ")))
                yolo = howdy + 273.15 #convert to kelvin
                cprint.info(_("That equals...\n%s" % yolo))
            elif hi == 5:
                ciao = float(input(_("Please enter the KELVIN temperature: ")))
                yolo = ciao - 273.15 #do the opposite of celsius to kelvin
                cprint.info(_("That equals...\n%s" % yolo))
            elif hi == 6:
                ciao = float(input(_("Please enter the KELVIN temperature: ")))
                yolo = ciao - 273.15
                yolo = yolo * 9/5
                yolo = yolo + 32
                cprint.info(_("That equals...\n%s" % yolo))
            # TO FIGURE OUT THE FORMULA I JUST GOOGLED 5 ____ TO _____ AND LOOKED AT THE FORMULA IT SHOWS.
            else:
                cprint.err(_("Invalid response."))
                logging.error("User typed invalid temperature answer %s" % hi)
