from __future__ import print_function #we need to tell the user if they are using python 2. all this does is prevent Syntaxerrors.
import warnings, math, random
from decimal import Decimal
from enum import Enum, auto
import sys

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

if sys.version_info < (3,4):
    raise ImportError(
    "You are running Mathmod 0.11 on Python 2 or Python < 3.4. Mathmod 0.11 and up is no longer compatible with Python 2.x, and somehow you still got this version installed."
    "\nSorry about that; it should not have happened. Make sure you have pip >= 9.0 to avoid this kind of issue, as well as setuptools >= 24.2 (pip install pip setuptools --upgrade --user)\n"
    "\nYou have two options.\n 1 - Upgrade to Python 3.4 or higher. \n 2 - Install Mathmod 0.10.3 or later in the series of 0.10 (pip install mathmod<0.11). "
    "\nThanks for using Mathmod, and sorry for the inconvenience."
    )

def confloat(n1,n2):
    """
    Used internally. Should not be used.
    """
    n1 = float(n1)
    n2 = float(n2)
    return (n1, n2)

def _confloat(item):
    return float(item)

def multiplication(*args, n1=None,n2=None) -> float: #multiplication
        """
        please do not use n1 or n2 anymore, they're deprecated.
        """
        if n1 is not None or n2 is not None:
            n1,n2 = confloat(n1,n2)
            warnings.warn("The n1/n2 API is deprecated. Stop using it.")
            return n1 * n2
        nums = []
        for item in args:
            item = _confloat(item)
            nums.append(item)
        result = nums[0]
        for number in nums[1:]: #https://stackoverflow.com/a/34384791/9654083
            result = result * number
        return result
def division(*args, n1=None,n2=None) -> float: #division
        """
        please do not use n1 or n2 anymore, they're deprecated.
        """
        if n1 is not None or n2 is not None:
            n1,n2 = confloat(n1,n2)
            warnings.warn("This n1 and n2 API is deprecated. Stop using it.")
            return n1 / n2
        nums = []
        for item in args:
            item = _confloat(item)
            nums.append(item)
        result = nums[0]
        for number in nums[1:]:
            result = result / number
        return result
def subtraction(*args,n1=None,n2=None) -> float: #subtraction
        """
        please do not use n1 or n2 anymore, they're deprecated.
        """
        if n1 is not None or n2 is not None:
            n1,n2 = confloat(n1,n2)
            warnings.warn("This n1 and n2 API is deprecated. Stop using it.")
            return n1 - n2
        nums = []
        for item in args:
            item = _confloat(item)
            nums.append(item)
        result = nums[0]
        for number in nums[1:]:
            result = result - number
        return result
def addition(*args,n1=None,n2=None) -> float: #addition
        """
        please do not use n1 or n2 anymore, they're deprecated.
        """
        if n1 is not None or n2 is not None:
            n1,n2 = confloat(n1,n2)
            warnings.warn("This n1 and n2 API is deprecated. Stop using it.")
            return n1 * n2
        nums = []
        for item in args:
            item = _confloat(item)
            nums.append(item)
        result = nums[0]
        for number in nums[1:]:
            result = result + number
        return result
def factorial(num: int) -> int:
    fin = int(num)
    while num > 1:
        num -= 1
        fin = fin * num
    return fin
def root_general(origin: float, root: float, useDecimal=False) -> float:
    """
    Setting useDecimal to True may provide a more accurate calculation, but could be considerably slower.
    float('0.1') + float('0.2') = 0.30000000000000004, while float(Decimal('0.1') + Decimal('0.2')) = 0.3.
    """
    if useDecimal is True:
        origin = Decimal(origin)
        root = Decimal(root)
        one = Decimal('1')
    else:
        origin = float(origin)
        root = float(root)
        one = 1
    num = one / root
    res = origin ** num
    if useDecimal is True:
        return float(Decimal(res))
    return res
rootGeneral = root_general

def exponent(n1: float, exponent: float) -> float:
        """
        param n1: Original number
        param exponent: exponent
        """
        origin, ex = confloat(n1, exponent)
        return origin ** ex
power = exponent

def modulo(n1: float, n2: float) -> float:
        n1, n2 = confloat(n1, n2)
        return n1 % n2

class tax_types:
    """
    Presets for Tax Percentages.
    """
    class sales:
        class Canada:
            ontario = 13
            quebec = 14.975
            yukon = 5
            northwest_territories = 5
            nunavut = 5
            alberta = 5
            british_columbia = 12
            manitoba = 12
            new_brunswick = 15
            nova_scotia = 15
            newfoundland = 15
            prince_edward_island = 15
            saskatchewan = 11

def tax(n1: float, tax: float) -> float:
        """
        param n1: Original number
        param tax: Tax in percentage (without percentage sign)
        You can use the tax_types class for presets.
        """
        usefulTax = (tax / 100) + 1
        percentageTax = percent_of(tax, n1)
        answer = n1 + percentageTax
        return answer

class LogarithmModes(Enum):
    base10 = "Base 10"
    e      = "Natural (e)"
def log(n1: float, mode: LogarithmModes):
        """
        parameter n1: Original number
        parameter mode: Select the desired mode from the LogarithmModes enum.
        """
        n1 = float(n1)
        try:
            mode.value
        except AttributeError:
            raise TypeError("You have to use a mode from the Enum.")
        e = mode == LogarithmModes.e
        if e:
            return math.log(n1)
        if not e:
            return math.log10(n1)

def percent_of(x: float, whole: float) -> float:
        """
        whole = ORIGINAL NUMBER
        x = percent
        This finds x percent of whole.
        """
        if whole == 0:
            raise ValueError("Invalid input (0).")
        return (x * whole) / 100.0
whatIsXPercentOf, percentage_of = percent_of, percent_of
def find_percentage(part: float, whole: float) -> float:
        """
        whole = number that would be 100%
        part = number that you want to convert to percentage (i.e. this number out of the number that would be 100%)
        This converts `whole' to be 100%, and finds what percentage `part' is out of 100%. Yes its confusing. Bear with me.
        """
        if whole == 0:
            raise ValueError("Invalid input (0).")
        return 100 * float(part) / float(whole)
findPercentage = find_percentage
def interest(units: float, rate: float, origin: float) -> float:
        '''
        units: if the rate is per month, and you want to calculate 3 months, you'd type 3 for this. If the rate is per year, and you want 2 years, you'd type 2 for this. And so on.
        rate: How much money per unit of time. So if you want to do 5% per unit of time, you'd type 5. 15%? Type 15.
        origin: Original number.
        '''
        inRealNumbers = percentage_of(whole=origin, x=rate)
        interest = inRealNumbers * units
        result = origin + interest
        return {"interest": interest, "total": result}
def calculateInterest(units, rate, origin):
        '''
        DO NOT USE THIS FUNCTION.
        THIS FUNCTION WILL BE REMOVED IN MATHMOD 0.12 - DO NOT USE!!!!
        '''
        warnings.warn("Warning: This old interest function is deprecated, you'll need to change it in 0.12.\nIf you're an end user and don't know what this means, contact the developer about this issue so they can continue to use new versions of Mathmod.")
        return interest(units, rate, origin)
getInterest = calculateInterest

def spinner(choice_selection: list, number_of_times: int) -> list:
        """
        param numberOfTimes: Amount of times to conduct the spinner.
        param choiceSelection: An iterable of the choices. Should be in this format: ["choice1", "choice2", "etc"].
        Returns a list of the results.
        Thanks to TutorialsPoint (https://www.tutorialspoint.com/How-to-append-elements-in-Python-tuple) for showing how to append to a tuple.
        Thanks to StackOverflow for showing that I should use a tuple rather than a list. (https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each)
        """
        result = list()
        for i in range(0, number_of_times):
            c = random.choice(choice_selection)
            result.append(str(c))
        return result
Spinner = spinner
