"""
Just a small module to call mathmod's functions and then parse the results.
"""

def main(Comandeer):
    globals()['_'] = Commandeer

import mathmod
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
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.addition(n1, n2)
        except ValueError as ename:
            logging.error("While parsing add(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed addition with %s as n1, %s as n2, answer = %s" % (n1, n2, returnedNumber))
    def subtraction():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.subtraction(n1, n2)
        except ValueError as ename:
            logging.error("While parsing sub(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed subtraction with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def multiplication():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.multiplication(n1, n2)
        except ValueError as ename:
            logging.error("While parsing multi(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            cprint.info(_("An exception was raised!\nValueError\n"))
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed multiplication with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def division():
        n1, n2 = Builtins.getInput()
        try:
            returnedNumber = mathmod.division(n1, n2)
        except ZeroDivisionError:
            logging.error("User decided to divide by zero.")
            raise SyntaxError("yes, because dividing %s cookie(s) for %s friend(s) makes sense" % (n1, n2))
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing div(%(n1)s, %(n2)s), a ValueError was thrown. (%(error)s)" % {"n1": n1, "n2": n2, "error": ename})
            raise
        cprint.info(_("The response is...%s") % returnedNumber)
        logging.info("Parsed division with %s as n1, %s as n2, answer as %s" % (n1, n2, returnedNumber))
    def mod(): #modulo
        n1, n2 = Builtins.getInput()
        result = mathmod.modulo(n1, n2)
        cprint.info(_("\nThat equals...\n%s\n" % result))
        logging.info("User attempted to modulo numbers %s and %s, and got result %s" % result)
class rootsAndTheOtherOne:
    def curoot():
        try:
            number = float(input(_("Number to be rooted? ")))
        except Exception as ename:
            cprint.err(_("ERRID 3: One or more of your numbers was not a number."))
            raise ValueError(_("ERRID3: One or more of the numbers was not a number. (Dump: n1=%s, n2=%s)" % (n1, n2)))
        try:
            nothernumber = mathmod.cuRoot(number)
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
            returnedNumber = mathmod.exponent(origin, ex)
        except ValueError as ename:
            cprint.err(_("An exception was raised!\nValueError\n"))
            logging.error("While parsing curoot(%(number)s), a ValueError was thrown. (%(error)s)" % {"number": number, "error": ename})
            raise
        cprint.info(_("The answer is... %s") % returnedNumber)
        logging.info("User exponented number %s with %s, getting %s" % (origin, ex, returnedNumber))
    def sqroot():
        num = float(input(_("Number to be rooted?")))
        returnedNumber = mathmod.sqRoot(num)
        cprint.info(_("That equals... %s" % returnedNumber))
        logging.info("user sqrooted number %s" % (returnedNumber))

class misc:
    def h():
        cprint.info(_('''
Current list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, "ord'ing", and convert bases (aka number systems). Type quit to quit.
Bugs? Head on over to https://github.com/thetechrobo/python-text-calculator/
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
                webbrowser.open("http://github.com/thetechrobo/python-text-calculator/issues/new")
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
        message = """What is the %s temperature unit? 
    1 - Farenheit
    2 - Celsius
    3 - Kelvin
    4 - Rankine
                                                   \033[A\033[A\033[A\033[A\033[A"""
        source = int(input(_(message % "source")))
        origin = float(input(_("Please enter the original temperature...")))
        destination = int(input(_(message % "destination")))
        print("                  ")
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
        elif source == 3 and destination == 1:
            yolo = origin - 273.15
            yolo = yolo * 9/5
            yolo = yolo + 32
        # TO FIGURE OUT THE FORMULA I JUST GOOGLED 5 ____ TO _____ AND LOOKED AT THE FORMULA IT SHOWS.
        else:
            cprint.err(_("Invalid response.\nIf you chose Rankine, it's because it's not currently supported."))
            logging.error("User typed invalid temperature answer %s, %s" % (source, destination))
        cprint.info(_("That equals... \n%s                       " % yolo))
        logging.info("User ran temperature calculator, with source %s, destination %s, and original number %s" % (source, destination, origin))
class Percentage:
    def percentage1():
        origin = float(input(_("What is the ORIGINAL NUMBER? ")))
        percent = float(input(_("What is the PERCENTAGE? ")))
        logging.info("Got percentage RN origin %s percent %s" % (origin, percent))
        cprint.info(_("That equals..."))
        try:
            cprint.info(mathmod.whatIsXPercentOf(percent, origin))
        except ValueError:
            cprint.err(_("You requested an impossible situation by entering 0 there - that would require division by 0."))
    def percentage2():
        origin = float(input(_("What is the number that would be 100%? ")))
        part = float(input(_("What is the number that you want to convert to percentage (i.e. this number out of the number that would be 100%)? ")))
        logging.info("Got percentage RN origin %s and %s" % (origin, part))
        cprint.info(_("That equals..."))
        try:
            cprint.info(mathmod.findPercentage(part, origin))
        except ValueError:
            cprint.err(_("You requested an impossible situation by entering 0 there - that would require division by 0."))
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

class Tax:
    def taxCalc():
        cprint.info(_('''1 - Ontario Sales Tax
2 - Quebec Sales Tax
3 - Yukon, Northwest Territories, Nunavut, and Alberta Sales Tax
4 - BC / Manitoba Sales Tax
5 - New Brunswick / Nova Scotia / Newfoundland / PEI Sales Tax
6 - Saskatchewan Sales Tax
7 - Custom Tax'''))
        whatPlace = int(input(_("Choose one: ")))
        if whatPlace == 1:
            percent = 13.0
        elif whatPlace == 2:
            percent = 14.975
        elif whatPlace == 3:
            percent = 5.0
        elif whatPlace == 4:
            percent = 12.0
        elif whatPlace == 5:
            percent = 15.0
        elif whatPlace == 6:
            percent = 11.0
        elif whatPlace == 7:
            percent = float(input(_("Please enter the tax percentage without the percent sign: ")))
        else:
            cprint.err(_("You did not type answer. Abort."))
            logging.error("User typed %s into tax...aka an invalid answer." % whatPlace)
            return
        originPrice = float(input(_("What is the original price (before tax)? ")))
        result = tax(originPrice, percent)
        logging.info("User used Sales Tax %s Percent with originPrice %s, price %s" % (percent, originPrice, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % result))

def logarithm(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    while True:
        base = input(_("1 - Base 10\n2 - Natural (e) logarithm\nPick one: "))
        number = float(input(_("What is the number? ")))
        if base[0] == "1":
            result = log(number, False)
            break
        elif base[0] == "2":
            result = log(number, True)
            break
        else:
            cprint.err(_("The logarithm you typed is not available."))
            cprint.ok(_("Try again."))
            logging.info("User attempted to use a logarithm that is unavailable.")
    logging.info("User used logarithm choice %s with number %s, getting a result of %s" % (base, number, result))

def base():
    """Will be improved "later"."""
    base = int(input('''What base would you like to convert to?
Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
Type 2, 8, 10, or 16: '''))
    if base == 2:
        origin = int(input(_("Type the original number: "))) #bin() the number
        printThis = "=" +str(bin(origin))
        logging.info("User binaried number %s, getting a result of %s" % (origin, printThis))
        cprint.info(printThis)
    elif base == 8:
            result = int(input(_("Type the original number: "))) #oct() the number
            printThis = "=" +str(oct(result))
            logging.info("User oct'ed number %s, getting a result of %s" % (result, printThis))
            cprint.info(printThis)
    elif base == 10:
        base = int(input(_('''Converting from a base to decimal (normal).
Example bases:
2 - Binary
8 - Oct
16 - Hexadecimal
Or, type 1 for ord.
Type: ''')))
        if base == 1:
            base2Print = "ord"
        else:
            base2Print = "base " + base
        original = int(input(_("Please enter the number to be converted from %s: " % base2Print)))
        if base == 1:
            eureka = chr(original)
        else:
            eureka = int(original, base)
        logging.info("User int'ed number %s from %s, getting a result of %s" % (original, base2Print, eureka))
        cprint.info(_("That equals...\n%s" % eureka))
        cprint.ok(_("TIP: If you got no answer, it might be that it was a Unicode character that it can't render. E.g. \\x06 would just be a blank space, like so: \x06"))
    elif base == 16:
        result = int(input(_("Type the original number: "))) #ask for original number
        printThis = "=" +hex(result)
        logging.info("User hexed number %s, getting a result of %s" % (result, printThis))
        cprint.info(printThis)

class Memory:
    """the two memory functions will be moved here "later" but not right now."""

def readMyMemory():
    cprint.info(_("This is the remember function.\nIt will read a number that was previously stored in a file."))
    try:
        slot = str(int(input(_("What slot number did you use? "))))
        with open(slot, "r") as memory:
            theMem = memory.read()
            cprint.info(_("Number: %s" % theMem))
            logging.info("Retrieved number %s from memory slot %s" % (theMem, slot))
    except Exception as e:
        logging.info("There was an error retrieving the file from memory. (Err %s)" % e)
        cprint.err(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file? "
        "Do you have the correct permissions?"))
def remember():
    cprint.info(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info("Saved number %s to memory slot %s" % (toRemember, slot))

def calculateInterest():
    while True: 
        origin = int(input(_("What is the original number? ")))
        rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
        print()
        units = int(input(_('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
        number = mathmod.calculateInterest(units, rate, origin)
        logging.info("INTERESTCALC: origin: %s rate: %s howMany: %s answer: %s" % (origin, rate, units, number))
        cprint.info(_("The answer is: \n%s" % number))
        doItAgain = input(_("Would you like to do it again (Y/n)? "))
        doItAgain = doItAgain.lower()
        if doItAgain[0] == _("y"):
            pass
        else:
            cprint.ok(_("Going back..."))
            return

if __name__ == "__main__":
    print("Please don't run this file directly, it can only be used with Palc")
    try:
        import runpy
        runpy.run_path(path_name="palc.py")
    finally:
        print("Next time, run palc.py rather than this file.")
