"""
Just a small...thing to Parse Functions from mathmod. Nothing to see here.
"""

def main(theThing):
    global _
    _ = theThing

from mathmod.func import *
from mathmod.basicfunc import *
from modules.cprint import *
import logging

class theBasics:
    def addition(n1, n2):
        try: 
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
            raise ValueError(_("ERRID3: One or more of the two numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = add(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was raised. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise ValueError(ename)
        cprint.info(_("The response is...%s"))
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction(n1, n2):
        try:
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = sub(n1, n2)
        except ValueError as ename:
            logging.error("While parsing sub(%(n1)s, %(n2)s), a ValueError was raised. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise ValueError(ename)
        cprint.info(_("The response is...%s"))
        logging.info("Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication(n1, n2):
        try:
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = multi(n1, n2)
        except ValueError as ename:
            logging.error("While parsing multi(%(n1)s, %(n2)s), a ValueError was raised. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise ValueError(ename)
        cprint.info(_("The response is...%s"))
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division(n1, n2):
        """
        Will do 'later'
        """

"""
these will have to be moved into a class later but for backwards compatibility it is temporarily kept
"""
def uc():
    logging.warning("User ran `volume.py'. Log is barely-tested for area and volume.")
    VolMain()
def area():
    logging.warning("User ran `area.py'. Log is barely tested for area and volume.")
    AreaMain()
def fib():
    from mathmod.fibonacci import CalculateLoopedFibo
    logging.info("About to run fibonacci")
    CalculateLoopedFibo()
    logging.info("User ran fibonacci function")
def h():
    cprint.info(_('''
Current list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, "ord'ing", and convert bases (aka number systems). Type quit to quit.
Bugs? Head on over to https://github.com/thetechrobo/support/
To contribute: go to https://github.com/thetechrobo/python-text-calculator/
'''))
