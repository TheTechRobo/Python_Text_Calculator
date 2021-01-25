from __future__ import division
from __future__ import print_function #we need to tell the user if they are using python 2.
"""
For area, import mathmod.area
For volume, mathmod.volume
For fibonacci, mathmod.fibonacci
These could be included in mathmod at any time. They'd be in classes.
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

class Arithmetic:
    @staticmethod
    def multiplication(n1, n2): #multiplication
        n1, n2 = confloat(n1, n2)
        return n1 * n2
    @staticmethod
    def division(n1, n2): #division
        n1, n2 = confloat(n1, n2)
        return n1 / n2
    @staticmethod
    def subtraction(n1, n2): #subtraction
        n1, n2 = confloat(n1, n2)
        return n1 - n2
    @staticmethod
    def addition(n1, n2): #addition
        n1, n2 = confloat(n1, n2)
        return n1 + n2
class ExponentsAndRoots:
    @staticmethod
    def cuRoot(x):
        # all credit goes to https://stackoverflow.com/a/28014443/9654083
        x = float(x)
        if 0 <= x:
            return x ** (1./3.)
        return - (-x) ** (1./3.)
    @staticmethod
    def sqRoot(x):
        x = float(x)
        return x ** 0.5
    @staticmethod
    def exponent(n1, n2):
        """
        param n1: Original number
        param n2: exponent
        """
        origin, ex = confloat(n1, n2)
        return origin ** ex
class Misc:
    @staticmethod
    def modulo(n1, n2):
        n1, n2 = confloat(n1, n2)
        return n1 % n2
    @staticmethod
    def tax(n1, n2):
        """
        param n1: Original number
        param n2: Tax in percentage (without percentage sign)
        """
        origin, tax = confloat(n1, n2)
        usefulTax = (tax / 100) + 1
        answer = origin + tax
        return answer
    @staticmethod
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

    @staticmethod
    def whatIsXPercentOf(x, whole):
        """
        whole = ORIGINAL NUMBER
        x = percent
        This finds x percent of whole.
        """
        if whole == 0:
            raise ValueError("Invalid input (0).")
        return (x * whole) / 100.0
    @staticmethod
    def findPercentage(part, whole):
        """
        whole = number that would be 100%
        part = number that you want to convert to percentage (i.e. this number out of the number that would be 100%)
        This converts `whole' to be 100%, and finds what percentage `part' is out of 100%. Yes its confusing. Bear with me.
        """
        if whole == 0:
            raise ValueError("Invalid input (0).")
        return 100 * float(part) / float(whole)

    @staticmethod
    def calculateInterest(units, rate, origin):
        '''
        units: if the rate is per month, and you want to calculate 3 months, you'd type 3 for this. If the rate is per year, and you want 2 years, you'd type 2 for this. And so on.
        rate: How much money per unit of time. So if you want to do 5% per unit of time, you'd type 5. 15%? Type 15.
        origin: Original number.
        '''
        inRealNumbers = percentage(whole=origin, x=rate)
        result = origin + (inRealNumbers * howMany)
        return result
    @staticmethod
    def calculateTemperature(origin, source, destination):
        """
        origin: Original Number
        source: 
          - 1 for Farenheit
          - 2 for Celsius
          - 3 for Kelvin
          - 4 for Rankine
        destination: 
          - 1 for Farenheit
          - 2 for Celsius
          - 3 for Kelvin
          - 4 for Rankine
        It would start at 0 but it would require some code changes in parsefunc so whatever. \__(^_^)__/
        """
        origin = float(origin)
        source = int(source)
        destination = int(destination)
        if source == 1 and destination == 2:
            yolo = origin - 32
            yolo = yolo * 5/9
        elif source == 2 and destination == 1:
            yolo = origin * 9/5
            yolo = yolo + 32
        elif source == 1 and destination == 3:
            #convert to celsius
            yolo = origin - 32
            yolo = yolo * 5/9
            #convert from celsius to kelvin
            yolo = yolo + 273.15
        elif source == 2 and destination == 3:
            yolo = origin + 273.15 #convert to kelvin
        elif source == 3 and destination == 2:
            yolo = origin - 273.15 #do the opposite of celsius to kelvin
        elif source == 3 and destination == 1: #kelvin to farenheit
            yolo = origin - 273.15
            yolo = yolo * 9/5
            yolo = yolo + 32
        elif source == 4 and destination == 1: #rankine to farenheit
            yolo = origin - 459.67
        elif source == 4 and destination == 2: #rankine to celsius
            yolo = (origin - 491.67) * 5/9
        elif source == 4 and destination == 3: #rankine to kelvin
            yolo = origin * 5/9
        elif source == 1 and destination == 4: #farenheit to rankine
            yolo = origin + 459.67
        elif source == 2 and destination == 4: #celsius to rankine
            yolo = origin * 9/5 + 491.67
        elif source == 3 and destination == 4: #kelvin to rankine
            yolo = origin * 1.8
        #elif source == destination: 
            #raise ValueError("bruh moment.")
            #pass
        # TO FIGURE OUT THE FORMULA I JUST GOOGLED 5 ____ TO _____ AND LOOKED AT THE FORMULA IT SHOWS.
        else:
            raise ValueError("MATHMOD: Invalid input(s).")
        return yolo
    @staticmethod
    def Spinner(numberOfTimes, choiceSelection):
        """
        param numberOfTimes: Amount of times to conduct the spinner.
        param choiceSelection: An iterable of the choices. Should be in this format: ["choice1", "choice2", "etc"].
        Returns a TUPLE of the results.
        Thanks to TutorialsPoint (https://www.tutorialspoint.com/How-to-append-elements-in-Python-tuple) for showing how to append to a tuple.
        Thanks to StackOverflow for showing that I should use a tuple rather than a list. (https://stackoverflow.com/questions/1708510/list-vs-tuple-when-to-use-each)
        """
        import random
        result = list()
        for i in range(0, numberOfTimes):
            c = random.choice(choiceSelection)
            result.append( (str(c) + " ") )
        resultAsTuple = tuple(result)
        del random, result #the garbage won't do
        return resultAsTuple
