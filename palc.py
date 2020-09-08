"""
PALC INFO
CODE CREDITS
============
THANKS TO https://simpleit.rocks/python/how-to-translate-a-python-project-with-gettext-the-easy-way/ and https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/ for their gettext guides!
THANKS TO @ErdoganOnal for their comment on this SO question: https://stackoverflow.com/questions/61621821/any-secure-alternatives-for-this?noredirect=1#comment109002742_61621821 That comment helped with the Press Any Key To Continue function (UPDATE::: That link is now dead, it is in the file FOR CLEARING THE SCREEN AND PRESS ANY KEY TO CONTINUE.md)
THANKS TO https://stackoverflow.com/questions/33594958/is-it-possible-to-align-a-print-statement-to-the-center-in-python FOR showing how to ALIGN the PRINT STATEMENT
THANKS TO https://stackoverflow.com/a/13627881/9654083 for saving me MUCH TROUBLE with codefactor's "editing global before intiialization" or whatever

OTHER STUFF
===========
CREATED BY: lewiswatson55
FORKED BY: TheTechRobo
CONTRIBUTORS: See contributors.md
LICENSE: DBAD Clean v.1.2 (found in LICENSE.md)
"""
import six
if not six.PY3:
    print("You are using a currently unsupported version of Python. Your mileage may vary.")

# IMPORTS
try:
    import gettext #to translate Palc
    from sys import exit as e #for exiting
    from modules.cprint import cprint #printing in colour
    from modules.clearscreen import clearScreen #clear the screen
    from modules.pressanykey import pressanykey #for the press any key to continue
    import time
    import sys #for misc
    import os #for misc
    import logging #self explanatory
except Exception as ename:
    print("Errid 0: Could not load required modules! (%s)" % ename)
logging.basicConfig(filename="palc.log", level=logging.DEBUG, format='%(levelname)s @ %(asctime)s %(message)s. Logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S') #set up logging, thanks for this website www.programcreek.com/python/example/136/logging.basicConfig for a few great examples!
#ask for language
width = os.get_terminal_size().columns
for i in range(0, width):
    print("-", sep="", end="", flush=True)
cprint.info("\nLanguage Selection // Language")
for i in range(0, width):
    print("-", sep="", end="", flush=True)
cprint.info("\n1 - English // Anglais\n2 - Francais // French").lower()
while True:
    try:
        language = int(input("Type: "))
    except ValueError as ename:
        logging.info("ValueError in language select (%s)" % ename)
        cprint.err("Invalid input // Entree invalide")
    if language == 1 or language == 2:
        break
if language == 1:
    try:
        logging.info("Set language to English")
        gettext.bindtextdomain('base', localedir="locales")
        lang_translations = gettext.translation('base', localedir='locales', languages=["en"])
    except (FileNotFoundError, IOError) as ename:
        logging.fatal("Could not get translation files. (%s)" % ename)
        cprint.fatal("Could not get translation files! Make sure that the `locales' directory exists!\nJe ne peux pas trouver la dossier `locales' ! ")
        cprint.info("This is not fatal with English translations, we can ignore it.")
        ignore = input("Ignore? (Y/n) ").lower()
        if ignore[0] == "y": #if user chooses to ignore
            logging.info("User ignored error !")
            def _(theEnglishString): #define a function that does nothing except give the value back so that NameErrors dont occur
                return theEnglishString
    except Exception as ename:
        logging.fatal("Could not get translations. (%s)" % ename)
        cprint.fatal("Could not load translations!\nJe ne peux pas utiliser les traductions ! ")
        cprint.info("This is not fatal with English translations, we can ignore it.")
        ignore = input("Ignore? (Y/n) ").lower()
        if "y" in ignore: #if user chooses to ignore
            logging.info("User ignored error !")
            def _(theEnglishString): #define a function that does nothing except give the value back so that NameErrors dont occur
                return theEnglishString
elif language == 2:
    try:
        logging.info("Set language to French")
        gettext.bindtextdomain('base', localedir="locales")
        lang_translations = gettext.translation('base',localedir='locales', languages=["fr"])
    except (FileNotFoundError, IOError):
        logging.fatal("Could not get translations. This is fatal. (%s)" % ename)
        cprint.fatal("Could not get translation files! Make sure that the `locales' directory exists!\nJe ne peux pas trouver la dossier `locales' ! ", interrupt=True)
    except Exception as ename:
        logging.fatal("Could not get translations. (%s)" % ename)
        cprint.fatal("Could not load translations!\nJe ne peux pas utiliser les traductions ! ")
else:
    logging.fatal("USER DID NOT SPECIFY A LANGUAGE, ABORT!")
    cprint.fatal("You did not specify a language. Abort.\nTu n'a pas dit une language supporté.", interrupt=True)
try:
    lang_translations.install()
    _ = lang_translations.gettext
except Exception as ename:
    logging.info("This is not necessary to be logged, but exception %s occured while installing translations" % ename)
#import func and basicfunc
logging.info("Attempting to import func.py and parsefunc.py (DEPRECATION WARNING: Later func and basicfunc will not be necessary.)")
try:
    from parsefunc import *
except Exception as e:
    logging.critical("Could not access file parsefunc.py (%s)" % e)
    cprint.fatal(_("I can't access the file parsefunc.py. This file is necessary for proper function of the Software."), interrupt=True)
try:
    if ignore[0] == "y":
        modules = ['parsefunc', 'mathmod.func', 'areaInteractive', 'volInteractive', 'mathmod.fibonacci']
        for module in modules:
            try:
                exec("from %s import main")
                main(_)
            except Exception as ename:
                logging.info("Errored running %s.main(_) (errid %s)" % (module, ename))
except Exception as ename:
    logging.info("Exception doing the if ignore[0] == \"y\" bit (%s)" % ename)
    cprint.err(_("Unexpected error!"))
try:
    from mathmod.func import *
except Exception as ename:
    logging.critical("Could Not Access func.py (%s)" % ename)
    cprint.fatal(_("I can't access func.py. This file is necessary for proper function of the Software."), interrupt=True)
logging.info("Successfully imported func.py!")
cprint.ok(_("Loading...............\n"))
time.sleep(2)
def palc():
    while True:
       pressanykey(_("Press any key to continue..."))
       clearScreen()
#CALCULATION CHOICE
       calc = input(_("What calculation do you wish to do? (Type `?' for a list of commands)\nType: "))
       logging.info("Got calc choice %s" % calc)
       calc = calc.lower() #make variable "calc" lowercase
#HELP
       if "?" in calc:
           logging.info("User needed help")
           misc.h()
       elif _("help") in calc:
           logging.info("User needed help")
           misc.h()
#TAX
       elif _("tax") in calc:
            misc.misc.showUserWhatIThink(_("calculate tax"))
            taxCalc()
#SQUARE
       elif _("sq") in calc:
            misc.showUserWhatIThink(_("square a number"))
            n = int(input(_("Number to square? ")))
            cprint.info(n * n)
            logging.info("User squared number %s got result %s" % (n, (n * n)))
       elif "[]" in calc:
            misc.showUserWhatIThink(_("square a number"))
            n = int(input(_("Number to square? ")))
            logging.info("User squared number %s got result %s" % (n, (n * n)))
            cprint.info(n * n)
#DIVISION
       elif "/" in calc:
            misc.showUserWhatIThink(_("divide a number"))
            theBasics.division()
       elif "div" in calc:
            misc.showUserWhatIThink(_("divide a number"))
            theBasics.division()
#SUBTRACTION
       elif "-" in calc:
            misc.showUserWhatIThink(_("subtract a number from a number"))
            theBasics.subtraction()()
       elif _("sub") in calc:
            misc.showUserWhatIThink(_("subtract a number from a number"))
            theBasics.subtraction()
       elif "min" in calc:
            misc.showUserWhatIThink(_("subtract a number from a number"))
            theBasics.subtraction()
#ADDITION
       elif "+" in calc:
            misc.showUserWhatIThink(_("add two numbers"))
            theBasics.addition()
       elif "add" in calc:
            misc.showUserWhatIThink(_("add two numbers"))
            theBasics.addition()
       elif "plus" in calc:
            misc.showUserWhatIThink(_("add two numbers"))
            theBasics.addition()
#MODULO
       elif "%" in calc:
            print(_("1 - Find the remainder of two numbers after division\n\
2 - Use the percentage calculator.\n\
Anything else - Back to menu."))
            pOrMod = input(_("Type: "))
            if pOrMod == "1":
                mod()
            elif pOrMod == "2":
                Percentage.chooseOneTwo()
            else:
                cprint.info(_("going back."))
                logging.info("going back.")
       elif "mod" in calc:
            misc.showUserWhatIThink(_("find the remainder of two numbers after division"))
            mod()
#AREA
       elif _("area") in calc:
            misc.showUserWhatIThink(_("calculate area"))
            misc.area()
       elif "#" in calc:
            misc.showUserWhatIThink(_("calculate area"))
            misc.area()
#VOLUME
       elif _("vol") in calc:
            misc.showUserWhatIThink(_("use the volume calculator"))
            misc.vol()
#CUBE
       elif "{}" in calc:
            misc.showUserWhatIThink(_("cube a number"))
            cubedNumber = int(input(_("\nType the number to be cubed: ")))
            print()
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info("User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print()
       elif _("cube") in calc: 
            misc.showUserWhatIThink(_("cube a number"))
            cubedNumber = int(input(_("\nType the number to be cubed: ")))
            print()
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info("User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print()
#EXIT
       elif _("quit") in calc:
            misc.showUserWhatIThink(_("quit"))
            logging.info("User exited using `quit' command")
            e()
       elif "exit" in calc:
            misc.showUserWhatIThink(_("exit"))
            logging.info("User exited using `exit' command")
            e()
#EXPONENTS
       elif "power" in calc:
            misc.showUserWhatIThink(_("use the exponent function"))
            rootsAndTheOtherOne.powerful()
       elif "ex" in calc:
            misc.showUserWhatIThink(_("use the exponent function"))
            rootsAndTheOtherOne.powerful()
       elif "^" in calc: #IDEA SOURCE: 3N4N's (first) Pull Request on the original repo
            misc.showUserWhatIThink(_("use the exponent function"))
            rootsAndTheOtherOne.powerful()
#MULTIPLICATION
       elif "*" in calc:
            misc.showUserWhatIThink(_("multiply a number"))
            multi()
       elif "x" in calc:
            misc.showUserWhatIThink(_("multiply a number"))
            multi()
       elif "multi" in calc:
            misc.showUserWhatIThink(_("multiply a number"))
            multi()
#CUBE TWICE
       elif "{2}" in calc:
            cprint.err(_("The \"cube twice\" feature was discontinued as it was pointless. Sorry for the inconvenience."))
            logging.error("User attempted to use cube twice function but it's gone")
#ROOTS
       elif _("root") in calc:
            misc.showUserWhatIThink(_("use the root function (opposite of exponents)"))
            root = input(_("Square root or cube root? (square/cube)\nType: ")).lower()
            if _("square") in root:
                rootsAndTheOtherOne.sqroot()
            elif "cube" in root:
                rootsAndTheOtherOne.curoot()
            else:
                cprint.err(_("Currently I don't support the root you chose. Hopefully this will change :D"))
                logging.error("User used non-existent root (%s)" % root)
#EASTER EGG!
       elif "=" in calc:
            misc.showUserWhatIThink(_("use the equals function (completely useless)"))
            number = int(input(_("\nType in a number: ")))
            if number == 42:
                cprint.info(_("=42 -- the answer to life, the universe, and everything"))
                logging.info("User got the easter egg")
            else:
                cprint.info(_("Calculating..."))
                time.sleep(3)
                cprint.err(_("ERROR: Too big of a number, timed out!"))
                logging.info("User used the `=' feature for number %s" % number)
#NUMBER SYSTEMS
       elif "base" in calc:
            misc.showUserWhatIThink(_("convert number systems"))
            base()
#ORD
       elif "ord" in calc:
           misc.showUserWhatIThink(_("ord a character"))
           result = str(ord(input(_("Type in the character to ord: "))))
           logging.info("User ord'ed to get result %s" % result)
           cprint.info(_("The result is: \n%s" % result))
#LOGARITHM
       elif _("log") in calc:
           misc.showUserWhatIThink(_("use the logarithm function"))
           log()
#MEMORY
       elif "mem" in calc:
            misc.showUserWhatIThink(_("use the memory function"))
            memOrRecall = input(_("Would you like to set the memory or recall? (set / recall)\nType: "))
            if _("set") in memOrRecall.lower():
                remember()
            elif _("recall") in memOrRecall.lower():
                readMyMemory()
            else:
                cprint.err(_("You did not type an answer.\nAbort."))
                logging.error("User didn't type an answer in MEM function (typed %s)" % memOrRecall)
#FIBONACCI
       elif "fib" in calc:
            misc.showUserWhatIThink(_("use the fibonacci calculator"))
            cprint.ok(_("Starting fibonacci sequence. Please wait."))
            misc.fib()
#PERCENTAGE
       elif _("percent") in calc: #SOURCE: https://stackoverflow.com/a/5998010/9654083
            misc.showUserWhatIThink(_("use the percentage function"))
            Percentage.chooseOneTwo()
#INTEREST
       elif _("interest") in calc:
            misc.showUserWhatIThink(_("use the interest calculator"))
            calculateInterest()
#TEMPERATURE
       elif "temperature" in calc:
            misc.showUserWhatIThink(_("use the temperature converter"))
            Temperature.tempCalc()
#CONVERSIONS
       elif "conver" in calc:
            logging.info("use the converter functions")
            misc.showUserWhatIThink(_("use the converter functions"))
            conversion = int(input(_("1 - Convert temperature units\n2 - Convert bits and bytes and kilobytes and mebibytes and stuff\nType: ")))
            if conversion == 1:
                Temperature.tempCalc()
            else:
                cprint.err(_("Not developed yet, but maybe soon! :D"))
                logging.info("User typed %s into conver functions but Non Existent." % conversion)
#OTHERWISE
       elif calc == "":
            logging.error("User attempted to type nothing as a command")
            cprint.err(_("I can't heeeeaaaarrrrrr yooooouuuuuuuu"))
       elif calc == " ":
            logging.error("user said nothing")
            cprint.err(_("You speak quietly"))
       elif calc is None:
            logging.error("User attempted to type nothing as a command")
            cprint.err(_("I can't heeeaaaarrrrr youuuuuuuu"))
       else:
            logging.error("User typed an invalid command (%s)" % calc)
            cprint.err(_('''
I don't understand your request. Here are the currently supported calculations:
multiplication, division, subtraction, addition, modulo, square, area, volume, cube, power, root, ord, fibonacci, logarithm, memory, percentage calculator, interest calculator, temperature, and base. Sorry for the inconvenience
'''))
width = os.get_terminal_size().columns
for i in range(0, width):
    print("-", sep="", end="")
logging.info("Printed %s dashes" % width)
cprint.info(_("Welcome to Palc!").center(width))
for i in range(0, width):
    print("-", sep="", end="")
logging.info("Printed %s dashes" % width)
try:
    palc() #run all that code
except SyntaxError as ename: #easter eggz
    raise #raise exact same exception
except KeyboardInterrupt: #if ^C
    logging.info("KeyboardInterrupt")
    cprint.ok(_("\nNote that you CAN type `quit' instead of pressing the interrupt key"))
    sys.exit()
except EOFError: #if ^D
    logging.info("EOFError")
    cprint.ok(_("\nWhy ^D? Why not just type `quit'?"))
    sys.exit()
except (ValueError, TypeError) as ename:
    logging.critical("ValueError or TypeError: %s" % ename)
    width = os.get_terminal_size().columns
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    cprint.err(_("\aERROR!\a".center(width))) #\a means beep the computer :D
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    cprint.fatal(_("You typed in an invalid integer or float. Or maybe the program needs debugging. Either way, it's a pretty big error."), interrupt=True)
except SystemExit:
    cprint.ok(_("Looks like you exited."))
    logging.info("Not necessary to be logged, but SystemExit was thrown")
except Exception as ename:
    width = os.get_terminal_size().columns
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    cprint.fatal(_("\aUnknown Error!\a".center(width))) #\a makes a beep
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    logging.fatal("Unknown error (%s)" % ename)
    cprint.fatal(_("An unknown error occured. Please file an Issue at github.com/thetechrobo/support."))
finally:
    logging.info("Program finished.")
#EOF
