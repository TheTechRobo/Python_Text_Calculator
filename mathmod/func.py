import logging
from cprint import cprint
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
def showUserWhatIThink(whatDOyouthink):
    cprint.ok(_("I think you want me to: "))
    cprint.ok(whatDOyouthink)
    isItCorrect = input(_("Is this correct? (Y/n)")).lower()
    if _("y") in isItCorrect:
        logging.info("Palc chose the right calculation (%s) for calc choice that (should be) shown above." % whatDOyouthink)
    elif "n" in isItCorrect:
        cprint.info(_("Try different wording. Or, if you want that calculation choice to be made right, file a ticket."))
        if _("y") in input(_("Would you like to file a ticket? (Y/n)\nType: ")).lower(): 
            import webbrowser
            webbrowser.open("http://github.com/thetechrobo/support/issues/new")
            logging.info("User chose to file a ticket because they didn't want Palc to %s" % whatDOyouthink)
            cprint.info(_("Proceeding with the function I thought it was."))
        else:
            cprint.info(_("OK, proceeding with the function I thought it was."))
    else:
        cprint.info(_("Defaulting to yes."))
        logging.info("Defaulting to yes for right calc (%s) for calc choice that should be shown above" % whatDOyouthink)
def power():
    showUserWhatIThink(_("use the exponent function"))
    origin = float(input(_("Original number?")))
    ex = float(input(_("Exponent? ")))
    cprint.info("=%s" % origin ** ex)
    logging.info("User exponented number %s with %s, getting %s" % (origin, ex, (origin ** ex)))
def h():
    cprint.info(_('''
Current list of commands: multiplication, division, addition, square, subtraction, modulo, area, volume, cube, exponents, root, logarithm, memory, interest calculator, fibonacci sequence, percentage calculator, convert temperature, "ord'ing", and convert bases (aka number systems). Type quit to quit.
Bugs? Head on over to https://github.com/thetechrobo/support/
To contribute: go to https://github.com/thetechrobo/python-text-calculator/
'''))
def mod(): #modulo
    try:
        bigger = int(input(_("\nType the first number (greater): ")))
        smaller = int(input(_("Type the second number (smaller): ")))
    except (TypeError, ValueError):
        cprint.err(_("\nError!"))
        cprint.err(_("Invalid input (code 1)\n"))
        logging.error("ERROR: attempted to modulo numbers %s and %s, but errored code 1." % (number1, number2))
    if(abs(bigger)<abs(smaller)):
        cprint.err(_("\nError!"))
        cprint.err(_("The second number entered is greater than the first number (code 2)\n"))
        logging.error("ERROR: attempted to modulo numbers %s and %s, but errored code 2." % (number1, number2))
    else:
        cprint.info(_("\nThat equals...\n%s" % (bigger - smaller * int(bigger / smaller))))
        logging.info("User attempted to modulo numbers %s and %s, and got result %s" % (bigger, smaller, (bigger-smaller*int(bigger/smaller))))
        print()
def base():
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
def log(): #https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python
    import math
    while True:
        base = input(_("What base would you like to use? \nCurrently supported: 10 (base 10), e (natural)"))
        if base == "10":
            cprint.info(_("Using base 10"))
            number = int(input(_("What is the number? ")))
            cprint.info(_("That equals:"))
            cprint.info(math.log10(number))
            logging.info("User used base 10 logarithm with number %s, getting a result of %s" % (number, (math.log10(number))))
            break
        elif base.lower() == "e":
            cprint.info(_("Using natural logarithm"))
            number = int(input(_("What is the number? ")))
            cprint.info("That equals...")
            cprint.info(math.log(number))
            logging.info("User used natural logarithm with number %s, getting a result of %s" % (number, (math.log(number))))
            break
        else:
            cprint.err(_("The logarithm you typed is not available."))
            cprint.ok(_("Try again."))
            logging.info("User attempted to use a logarithm that is unavailable.")
def remember():
    cprint.info(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info("Saved number %s to memory slot %s" % (toRemember, slot))
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
        cprint.err(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?"))
def percentage(percent, whole):
    if whole == 0:
        logging.error("User typed 0 as whole.")
        return (_("Please do not type in a zero as the whole."))
    return (percent * whole) / 100.0
def whatIsPercent():
    origin = float(input(_("what is the ORIGINAL NUMBER? ")))
    percent = float(input(_("What is the PERCENTAGE? ")))
    logging.info("Got percentage RN origin %s percent %s" % (origin, percent))
    cprint.info(_("That equals..."))
    cprint.info(percentage(percent, origin))
def getPercentage(part, whole):
    if whole == 0:
        logging.error("user typed whole zero")
        return (_("Please do not type in a zero as the whole."))
    return 100 * float(part)/float(whole)
def getPercentageRN():
    origin = float(input(_("What is the number that would be 100%? ")))
    part = float(input(_("What is the number that you want to convert to percentage (e.g. this number out of the number that would be 100%)? ")))
    logging.info("Got percentage RN origin %s and %s" % (origin, part))
    cprint.info(_("that equals:"))
    cprint.info(getPercentage(part, origin))
def calculateInterest():
    while True: 
        origin = int(input(_("What is the original number? ")))
        rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
        print()
        howMany = int(input(_('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
        inRealNumbers = percentage(whole=origin, percent=rate)
        number = origin + (inRealNumbers * howMany)
        logging.info("INTERESTCALC: origin: %s rate: %s howMany: %s answer: %s" % (origin, rate, howMany, number))
        cprint.info(_("The answer is: \n%s" % number))
        doItAgain = input(_("Would you like to do it again (Y/n)? "))
        doItAgain = doItAgain.lower()
        if doItAgain == _("y"):
            pass
        else:
            cprint.ok(_("Going back..."))
            break
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
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 13.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used Ontarian Sales Tax 13 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 2:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 14.975
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used Quebec Sales Tax 14.975 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 3:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 5.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used Alberta Sales Tax 5 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 4:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 12.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used Manitoba Sales Tax 12 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 5:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 15.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used PEI Sales Tax 15 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 6:
        originPrice = int(input(_("What is the original price (before tax)? ")))
        percent = 11.0
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        logging.info("User used Saskatchewan Sales Tax 11 PerCent  with originPrice %s sales tax %s, with price %s" % (originPrice, theSalesTax, newPrice))
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
    elif whatPlace == 7:
        originPrice = float(input(_("OK, enter the original price: ")))
        percent = float(input(_("Now enter the tax percentage without the percent sign: ")))
        theSalesTax = percentage(percent, originPrice)
        newPrice = theSalesTax + originPrice
        cprint.info(_("After tax, the price is: \n%s" % newPrice))
        logging.info("User did CustomTax %s PerCent with originPrice %s, sales tax %s, with newPrice %s" % (percent, originPrice, theSalesTax, newPrice))
    else:
        cprint.err(_("You did not type answer. Abort."))
        logging.error("User typed %s into tax...aka an invalid answer." % whatPlace)
def tempCalc():
    hi = int(input(_('''OPTIONS:
    1 - Farenheit to Celsius
    2 - Celsius to Farenheit
    3 - Farenheit to Kelvin
    4 - Celsius to Kelvin
    5 - Kelvin to Celsius
    6 - Kelvin to Farenheit
Type: ''')))
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
