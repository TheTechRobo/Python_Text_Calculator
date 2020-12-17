"""
For area, import mathmod.area
For volume, mathmod.volume
For fibonacci, mathmod.fibonacci
These could be included in mathmod at any time, without warning.
"""

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

def confloat(n1, n2):
    """
    Used internally. Should not be used.
    """
    n1 = float(n1)
    n2 = float(n2)
    return (n1, n2)

def multi(n1, n2): #multiplication
    n1, n2 = confloat(n1, n2)
    return n1 * n2
def div(n1, n2): #division
    n1, n2 = confloat(n1, n2)
    return n1 / n2
def sub(n1, n2): #subtraction
    n1, n2 = confloat(n1, n2)
    return n1 - n2
def add(n1, n2): #addition
    n1, n2 = confloat(n1, n2)
    return n1 + n2
def mod(n1, n2):
    n1, n2 = confloat(n1, n2)
    return n1 % n2
def cuRoot(x):
    # all credit goes to https://stackoverflow.com/a/28014443/9654083
    x = float(x)
    if 0 <= x:
        return x ** (1./3.)
    return - (-x) ** (1./3.)
def sqRoot(x):
    x = float(x)
    return x ** 0.5
def exponent(n1, n2):
    """
    param n1: Original number
    param n2: exponent
    """
    origin, ex = confloat(n1, n2)
    return origin ** ex
def tax(n1, n2):
    """
    param n1: Original number
    param n2: Tax in percentage (without percentage sign)
    """
    origin, tax = confloat(n1, n2)
    usefulTax = (tax / 100) + 1
    answer = origin + tax
    return answer

def log(n1, e=True):
    """
    parameter n1: Original number
    parameter e: Use False if you want base 10 logarithm; True for e (natural). Defaults to natural.
    """
    import math
    n1 = float(n1)
    if e:
        return math.log(n1)
    if not e:
        return math.log10(n1)

def whatIsXPercentOf(x, whole):
    """
    whole = ORIGINAL NUMBER
    x = percent
    This finds x percent of whole.
    """
    if whole == 0:
        raise ValueError("Invalid input (0).")
        return #not sure if this is necessary but hey better safe than sorry
    return (x * whole) / 100.0
def findPercentage(part, whole):
    """
    whole = number that would be 100%
    part = number that you want to convert to percentage (i.e. this number out of the number that would be 100%)
    This converts `whole' to be 100%, and finds what percentage `part' is out of 100%. Yes its confusing. Bear with me.
    """
    if whole == 0:
        raise ValueError("Invalid input (0).")
        return #not sure if this is necessary but hey better safe than sorry
    return 100 * float(part) / float(whole)

def calculateInterest(units, rate, origin):
    '''
    units: if the rate is per month, and you want to calculate 3 months, you'd type 3 for this. If the rate is per year, and you want 2 years, you'd type 2 for this. And so on.
    rate: How much money per unit of time. So if you want to do 5% per unit of time, you'd type 5. 15%? Type 15.
    origin: Original number.
    '''
    inRealNumbers = percentage(whole=origin, x=rate)
    result = origin + (inRealNumbers * howMany)
    return result
class tax:
    pass
class temperature:
    pass
