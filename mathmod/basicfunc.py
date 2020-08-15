# This file is for basic functions and small functions that would be in func.py but are too small to be worth it.
import logging
from modules.cprint import cprint
from areaInteractive import *
from volInteractive import *

def main(Comandeer):
    global _
    _ = Comandeer

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")
def getNum(): #ask for two numbers and then return to function
    n1 = int(input(_("Please enter the first number: ")))
    n2 = int(input(_("Please enter the second number: ")))
    logging.info("Palc got two numbers: %s and %s" % (n1, n2))
    return n1, n2

def multi(): #multiplication
    n1 = float(n1)
    n2 = float(n2)
    return (n1 * n2)
def div(): #division
    """
    Will do later
    """
    n1, n2 = getNum()
    try:
        cprint.info(_("\nThat equals...\n%s" % (n1 / n2)))
        logging.info("User divvied %s by %s, getting a result of %s" % (n1, n2, (n1 / n2)))
    except ZeroDivisionError:
        cprint.err(_("Yes, because dividing %s cookies for 0 friends makes sense." % n1))
        logging.error("User attempted to divide by zero.")
    except Exception as e:
        cprint.err(_("There was an unknown issue dividing your Numbers..."))
        logging.error("User had an issue divvying up %s by %s (%s)" % (n1,n2,e))
def sub(n1, n2): #subtraction
    n1 = float(n1) #I _could_ write a function (replacing `getNum()') that would take both numbers and return a tuple with the float'ed numbers, so it could be called like `n1, n2 = getNum(n1, n2)' but i'm too lazy ;D
    n2 = float(n2)
    return (n1 - n2)
def add(n1, n2): #addition
    n1 = float(n1)
    n2 = float(n2)
    return (n1 + n2)


"""
Will do these ones later
"""
def uc():
    logging.warning("User ran `volume.py'. Log is barely-tested for area and volume.")
    VolMain()
def area():
    logging.warning("User ran `area.py'. Log is barely tested for area and volume.")
    AreaMain()

def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0 <= x:
        return x**(1./3.)
    return -(-x)**(1./3.)
def curoot():
    number = float(input(_("Number to be rooted? ")))
    nothernumber = cubeInternal(number)
    logging.info("User curooted number %s to get %s..." % (number, nothernumber))
    cprint.info("=%s" % nothernumber)
def cu(): #backwards-compatibility
    curoot()

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

def power():
    showUserWhatIThink(_("use the exponent function"))
    origin = float(input(_("Original number?")))
    ex = float(input(_("Exponent? ")))
    cprint.info("=%s" % origin ** ex)
    logging.info("User exponented number %s with %s, getting %s" % (origin, ex, (origin ** ex)))

#def sin():
    #which = input(_("Would you like sine or inverse sine? (sin / inverse)\nType:
