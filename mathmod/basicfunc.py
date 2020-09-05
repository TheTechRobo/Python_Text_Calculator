# This file is for basic functions and small functions that would be in func.py but are too small to fit.

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

def multi(n1, n2): #multiplication
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
def cuRoot(x):
    # all credit goes to https://stackoverflow.com/a/28014443/9654083
    if 0 <= x:
        return x ** (1./3.)
    return - (-x) ** (1./3.)
def sqRoot(x):
    return x ** 0.5
def exponent(n1, n2):
    origin = float(n1)
    ex = float(n2)
    return (origin ** ex)
