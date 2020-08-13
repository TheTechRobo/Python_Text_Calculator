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
            cprint.err(_("ERROR: One or more of your two numbers was not a number. (Errid 3) (Dump: n1=%s, n2=%s)" % (n1, n2)))
            raise ValueError(_("ERRID 3: One or more of the two numbers was not a number. (n1=%s, n2=%s)" % (n1, n2)))
        try:
            returnedNumber = add(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was raised. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise ValueError(ename)
        cprint.info(_("The response is...%s"))
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s")
        return
    def subtraction(n1, n2):
        pass
    def multiplication(n1, n2):
        pass
    def division(n1, n2):
        pass
