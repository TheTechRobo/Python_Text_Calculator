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
def div(n1, n2): #division
    n1 = float(n1)
    n2 = float(n2)
    return (n1 / n2)
def sub(n1, n2): #subtraction
    n1 = float(n1)
    n2 = float(n2)
    return (n1 - n2)
def add(n1, n2): #addition
    n1 = float(n1)
    n2 = float(n2)
    return (n1 + n2)


"""
Will do these ones later
"""
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

def power():
    showUserWhatIThink(_("use the exponent function"))
    origin = float(input(_("Original number?")))
    ex = float(input(_("Exponent? ")))
    cprint.info("=%s" % origin ** ex)
    logging.info("User exponented number %s with %s, getting %s" % (origin, ex, (origin ** ex)))

#def sin():
    #which = input(_("Would you like sine or inverse sine? (sin / inverse)\nType:
