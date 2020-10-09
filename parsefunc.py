"""
Just a small module to call mathmod's functions and then parse the results.
"""

def main(Comandeer):
    globals()['_'] = Commandeer

from mathmod.func import *
from mathmod.basicfunc import *
from modules.cprint import cprint
import logging

class Builtins: 
    def getInput():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        try: 
            float(n1)
            float(n2)
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the two numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        return (n1, n2)

class theBasics:
    def addition():
        n1 = input(_("Please enter the first number: "))
        n2 = input(_("Please enter the second number: "))
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = add(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = sub(n1, n2)
        except ValueError as ename:
            logging.error("While parsing sub(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = multi(n1, n2)
        except ValueError as ename:
            logging.error("While parsing multi(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s"))
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division():
        n1, n2 = Builtins.getInput()
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
        logging.info("Parsed division with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def mod(): #modulo
        n1, n2 = Builtins.getInput()
        result = mod(n1, n2)
        cprint.info(_("\nThat equals...\n%s\n" % result))
        logging.info("User attempted to modulo numbers %s and %s, and got result %s" % result))
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
        hi = int(input(_("Would you like...\n    1 - Calculate a fixed amount of fibonacci numbers.\n    2 - Calculate fibonacci indefinitely.\nType: ")))
        if hi[0] == 1:
            cprint.info(_("Fixed it is."))
            from mathmod.fibonacci import CalculateFixedFibo
            amount = int(input(_("How many numbers of fibonacci would you like to calculate? ")))
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
            cprint.ok(_("Press Control-C to stop."))
            try:
                CalculateLoopedFibo()
            except Exception as ename:
                logging.err("Exception %s in looped fibonacci" % ename)
                cprint.err(_("An error occured."))
            except KeyboardInterrupt:
        logging.info("User ran fibonacci function")
    def showUserWhatIThink(whatDOyouthink):
        cprint.ok(_("I think you want me to: \n%s" % whatDOyouthink))
        isItCorrect = input(_("Is this correct? (Y/n)")).lower()
        if _("y") in isItCorrect:
            logging.info("Palc chose the right calculation (%s) for calc choice that should be shown above." % whatDOyouthink)
        elif "n" in isItCorrect:
            cprint.info(_("Try different wording. Or, if you want that calculation choice to be made right, file a ticket."))
            if _("y") in input(_("Would you like to file a ticket? (Y/n)\nType: ")).lower(): 
                import webbrowser
                webbrowser.open("http://github.com/thetechrobo/support/issues/new")
                logging.info("User chose to file a ticket because they didn't want Palc to %s" % whatDOyouthink)
                input(_("Press ENTER to continue..."))
                cprint.info(_("Proceeding with the function I thought it was."))
            else:
                cprint.info(_("OK, proceeding with the function I thought it was."))
        else:
            cprint.info(_("Defaulting to yes."))
            logging.info("Defaulting to yes for right calc (%s) for calc choice that should be shown above" % whatDOyouthink)
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
class Percentage:
    def percentage1():
        origin = float(input(_("What is the ORIGINAL NUMBER? ")))
        percent = float(input(_("What is the PERCENTAGE? ")))
        logging.info("Got percentage RN origin %s percent %s" % (origin, percent))
        cprint.info(_("That equals..."))
        cprint.info(whatIsXPercentOf(percent, origin))
    def percentage2():
        origin = float(input(_("What is the number that would be 100%? ")))
        part = float(input(_("What is the number that you want to convert to percentage (i.e. this number out of the number that would be 100%)? ")))
        logging.info("Got percentage RN origin %s and %s" % (origin, part))
        cprint.info(_("That equals..."))
        cprint.info(findPercentage(part, origin))
    def chooseOneTwo():
        chosenPercentageCalc = int(input(_('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage (i.e. how much percent of ___ is ___?).
Type: ''')))
        if chosenPercentageCalc == 1:
            Percentage.percentage1()
        elif chosenPercentageCalc == 2:
            Percentage.percentage2()
        else:
            cprint.err(_("You didn't type a valid answer. Abort."))
            logging.info("User did not answer correct percentage interpretation")
if __name__ == "__main__":
    print("Please don't run this file directly, it can only be used with Palc")
    try:
        import runpy
        runpy.run_path(path_name="palc.py")
    finally:
        print("Next time, run palc.py rather than this file.")
