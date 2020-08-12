# This file is for basic functions and small functions that would be in func.py.
import logging
from cprint import cprint
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
    n1, n2 = getNum()
    cprint.info(_("\nThat equals...\n%s" % (n1 * n2)))
    logging.info("User multiplied %s by %s and got result %s" % (n1, n2, (n1 * n2)))
def div(): #division
    n1, n2 = getNum()
    try:
        cprint.info(_("\nThat equals...\n%s" % (n1 / n2)))
        logging.info("User divvied %s by %s, getting a result of %s" % (n1, n2, (n1 / n2)))
    except ZeroDivisionError:
        cprint.err(_("Do not divide by zero!"))
        logging.error("User attempted to divide by zero.")
    except Exception as e:
        cprint.err(_("There was an unknown issue dividing your Numbers..."))
        logging.error("User had an issue divvying up %s by %s (%s)" % (n1,n2,e))
def sub(): #subtraction
    n1, n2 = getNum()
    cprint.info(_("\nThat equals...\n%s" % (n1 - n2)))
    logging.info("User subtracted %s by %s and got result %s" % (n1, n2, (n1 - n2)))
def add(): #addition
    n1, n2 = getNum()
    cprint.info(_("\nThat equals...\n%s" % (n1 + n2)))
    logging.info("User added %s to %s and got result %s" % (n1, n2, (n1 + n2)))

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
    from fibonacci import CalculateLoopedFibo
    logging.info("About to run fibonacci")
    CalculateLoopedFibo()
    logging.info("user ran fibonacci function")

#def sin():
    #which = input(_("Would you like sine or inverse sine? (sin / inverse)\nType:
