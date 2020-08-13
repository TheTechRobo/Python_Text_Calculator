#CREDITS
#THANKS TO https://simpleit.rocks/python/how-to-translate-a-python-project-with-gettext-the-easy-way/ and https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/ for their gettext guides!

# THANKS TO @ErdoganOnal for their comment on this SO question: https://stackoverflow.com/questions/61621821/any-secure-alternatives-for-this?noredirect=1#comment109002742_61621821 That comment helped with the Press Any Key To Continue function
#(UPDATE::: That link is now dead, it is in the file FOR CLEARING THE SCREEN AND PRESS ANY KEY TO CONTINUE.md)

# THANKS TO https://stackoverflow.com/questions/33594958/is-it-possible-to-align-a-print-statement-to-the-center-in-python FOR showing how to ALIGN the PRINT STATEMENT

import six
if not six.PY3:
    print("You are using a currently unsupported version of Python. Your mileage may vary.")

# IMPORTS
import gettext #to translate Palc
from sys import exit as e #so that we can exit later on
from modules.cprint import cprint #printing in colour
from modules.clearscreen import clearScreen #clear the screen
from modules.pressanykey import pressanykey #for the press any key to continue
import time
import sys, os, logging #sys so I can exit, os so I can do I can't remember, logging so I can log.
logging.basicConfig(filename="palc.log", level=logging.DEBUG, format='%(levelname)s @ %(asctime)s %(message)s. Logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S') #set up logging, thanks for this website www.programcreek.com/python/example/136/logging.basicConfig for a few great examples!
#ask for language
language = input("English or/ou Francais? (do not add accents to letters/n'ajoute pas les accents aux lettres): ")
language = language.lower()
if language == "francais":
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
elif language == "english":
    try:
        logging.info("Set language to English")
        gettext.bindtextdomain('base', localedir="locales")
        lang_translations = gettext.translation('base', localedir='locales', languages=["en"])
    except (FileNotFoundError, IOError) as ename:
        logging.fatal("Could not get translation files. This is fatal. (%s)" % ename)
        cprint.fatal("Could not get translation files! Make sure that the `locales' directory exists!\nJe ne peux pas trouver la dossier `locales' ! ")
        cprint.info("This is not fatal with English translations, we can ignore it.")
        ignore = input("Ignore? (Y/n) ").lower()
        if "y" in ignore: #if user chooses to ignore
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
else:
    logging.fatal("USER DID NOT SPECIFY A LANGUAGE, ABORT!")
    cprint.fatal("You did not specify a language. Abort.\nTu n'a pas dit une language supporte.", interrupt=True)
    ignore = False
try:
    lang_translations.install()
    _ = lang_translations.gettext
except Exception as ename:
    logging.info("This is not necessary to be logged, but exception %s occured while installing Traductions" % ename)
#import func and basicfunc
logging.info("Attempting to import func.py and basicfunc.py.")
try:
    from mathmod.func import *
except Exception as e:
    logging.critical("Could not access file func.py (%s)" % e)
    cprint.fatal(_("I can't access the file func.py. This file is necessary for proper function of the Software."), interrupt=True)
logging.info("Successfully imported func.py")
try:
    if "y" in ignore:
        import mathmod.func as f
        f.main(_)
        del f
        import mathmod.basicfunc as b
        b.main(_)
        del b
        import areaInteractive as a
        a.main(_)
        del a
        import volInteractive as v
        v.main(_)
        del v
        import mathmod.fibonacci as fi
        fi.main(_)
        del fi
except Exception as ename:
    logging.info("Errored Running *.main(_) (errid %s)" % ename)
try:
    from mathmod.basicfunc import *
except Exception as e:
    logging.critical("Could Not Access basicfunc.py (%s)" % e)
    cprint.fatal(_("I can't access file basicfunc.py. This file is necessary for proper function of the Software."), interrupt=True)
logging.info("Successfully imported basicfunc.py!")
cprint.ok(_("Loading...............\n"))
time.sleep(2)
def palc():
    while True:
       pressanykey()
       clearScreen()
#CALCULATION CHOICE
       calc = input(_("What calculation do you wish to do? (Type `?' for a list of commands)\nType: "))
       logging.info("Got calc choice %s" % calc)
       calc = calc.lower() #make variable "calc" lowercase
#HELP
       if "?" in calc:
           logging.info("User needed help")
           h()
       elif _("help") in calc:
           logging.info("User needed help")
           h()
#TAX
       elif _("tax") in calc:
            showUserWhatIThink(_("calculate tax"))
            taxCalc()
#SQUARE
       elif _("sq") in calc:
            showUserWhatIThink(_("square a number"))
            n = int(input(_("Number to square? ")))
            cprint.info(n * n)
            logging.info("User squared number %s got result %s" % (n, (n * n)))
       elif "[]" in calc:
            showUserWhatIThink(_("square a number"))
            n = int(input(_("Number to square? ")))
            logging.info("User squared number %s got result %s" % (n, (n * n)))
            cprint.info(n * n)
#DIVISION
       elif "/" in calc:
            showUserWhatIThink(_("divide a number"))
            div()
       elif "div" in calc:
            showUserWhatIThink(_("divide a number"))
            div()
#SUBTRACTION
       elif "-" in calc:
            showUserWhatIThink(_("subtract a number from a number"))
            sub()
       elif _("sub") in calc:
            showUserWhatIThink(_("subtract a number from a number"))
            sub()
       elif "min" in calc:
            showUserWhatIThink(_("subtract a number from a number"))
            sub()
#ADDITION
       elif "+" in calc:
            showUserWhatIThink(_("add two numbers"))
            add()
       elif "add" in calc:
            showUserWhatIThink(_("add two numbers"))
            add()
       elif "plus" in calc:
            showUserWhatIThink(_("add two numbers"))
            add()
#MODULO
       elif "%" in calc:
            print(_("1 - Find the remainder of two numbers after division\n\
2 - Use the percentage calculator.\n\
Anything else - Back to menu."))
            pOrMod = input(_("Type: "))
            if pOrMod == "1":
                mod()
            elif pOrMod == "2":
                whichOne = int(input(_('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage.
Type: ''')))
                if whichOne == 1:
                    whatIsPercent()
                elif whichOne == 2:
                    getPercentageRN()
                else:
                    cprint.err(_("You didn't type a valid answer. Abort."))
                    logging.info("User did not answer correct percentage interpretation")
            else:
                cprint.info(_("going back."))
                logging.info("going back.")
       elif "mod" in calc:
            showUserWhatIThink(_("find the remainder of two numbers after division"))
            mod()
#AREA
       elif _("area") in calc:
            showUserWhatIThink(_("calculate area"))
            area()
       elif "#" in calc:
            showUserWhatIThink(_("calculate area"))
            area()
#VOLUME
       elif _("vol") in calc:
            showUserWhatIThink(_("use the volume calculator"))
            uc()
#CUBE
       elif "{}" in calc:
            showUserWhatIThink(_("cube a number"))
            cubedNumber = int(input(_("\nType the number to be cubed: ")))
            print()
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info("User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print()
       elif _("cube") in calc: 
            showUserWhatIThink(_("cube a number"))
            cubedNumber = int(input(_("\nType the number to be cubed: ")))
            print()
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info("User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print()
#EXIT
       elif _("quit") in calc:
            showUserWhatIThink(_("quit"))
            logging.info("User exited using `quit' command")
            e()
       elif "exit" in calc:
            showUserWhatIThink(_("exit"))
            logging.info("User exited using `exit' command")
            e()
#EXPONENTS
       elif "power" in calc:
            power()
       elif "ex" in calc:
            power()
       elif "^" in calc: #IDEA SOURCE: 3N4N's (first) Pull Request on the original repo
            power()
#MULTIPLICATION
       elif "*" in calc:
            showUserWhatIThink(_("multiply a number"))
            multi()
       elif "x" in calc:
            showUserWhatIThink(_("multiply a number"))
            multi()
       elif "multi" in calc:
            showUserWhatIThink(_("multiply a number"))
            multi()
#CUBE TWICE
       elif "{2}" in calc:
            cprint.err(_("The \" CUBE TWICE \" feature was discontinued."))
            logging.error("User attempted to use cube twice function but it's discontinued")
#ROOTS
       elif _("root") in calc:
            showUserWhatIThink(_("use the root function (opposite of exponents)"))
            root = input(_("Square root or cube root? (square/cube)\nType: "))
            root = root.lower()
            if _("square") in root:
                num = float(input(_("Number to be rooted?")))
                cprint.info(_("That equals.....\n%s" % (num ** 0.5)))
                logging.info("user sqrooted number %s" % (num**0.5))
            elif "cube" in root:
                cu()
            else:
                cprint.err(_("Currently I don't support the root you chose. Hopefully this will change :)"))
                logging.error("User used non-existent root (%s)" % root)
#EASTER EGG!
       elif "=" in calc:
            showUserWhatIThink(_("use the equals function (completely useless)"))
            number = int(input(_("\nType in a number: ")))
            if number == 42:
                cprint.info(_("=42 -- the answer to life, the universe, and everything"))
                logging.info("User got the easter egg")
            else:
                cprint.err(_("Do you really need a calculator for this?"))
                logging.info("User used the `=' feature for number %s" % number)
#NUMBER SYSTEMS
       elif "base" in calc:
            showUserWhatIThink(_("convert number systems"))
            base()
#ORD
       elif "ord" in calc:
           showUserWhatIThink(_("ord a character"))
           result = str(ord(input(_("Type in the character to ord: "))))
           logging.info("User ord'ed to get result %s" % result)
           cprint.info(_("The result is: \n%s" % result))
#LOGARITHM
       elif _("log") in calc:
           showUserWhatIThink(_("use the logarithm function"))
           log()
#MEMORY
       elif "mem" in calc:
            showUserWhatIThink(_("use the memory function"))
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
            showUserWhatIThink(_("use the fibonacci calculator"))
            cprint.ok(_("Starting fibonacci sequence. Please wait."))
            fib()
#PERCENTAGE
       elif _("percent") in calc: #SOURCE: https://stackoverflow.com/a/5998010/9654083
            showUserWhatIThink(_("use the percentage function"))
            whichOne = int(input(_('''1 - Calculate "What is x% of y?"
2 - Convert a number to percentage.
Type: ''')))
            if whichOne == 1:
                whatIsPercent()
            elif whichOne == 2:
                getPercentageRN()
            else:
                cprint.err(_("You didn't type a valid answer. Abort."))
                logging.info("User did not answer correct percentage interpretation (typed %s)" % whichOne)
#INTEREST
       elif _("interest") in calc:
            showUserWhatIThink(_("use the interest calculator"))
            calculateInterest()
#TEMPERATURE
       elif "temperature" in calc:
            showUserWhatIThink(_("use the temperature converter"))
            tempCalc()
#CONVERSIONS
       elif "conver" in calc:
            showUserWhatIThink(_("use the converter functions"))
            conversion = int(input(_("1 - Convert temperature units\nType: ")))
            if conversion == 1:
                tempCalc()
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
    cprint.err(_("\aERROR!".center(width)))
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    cprint.fatal(_("You typed in an invalid integer or float. Or maybe the program needs debugging. Either way, it's a pretty big error."))
    cprint.ok(_("Details are in the log."))
    e()
except SystemExit:
    cprint.ok(_("Looks like you exited."))
    logging.info("User exited with exception SystemExit")
except Exception as ename:
    width = os.get_terminal_size().columns
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    cprint.fatal(_("Unknown Error!".center(width)))
    for i in range(0, width):
        print("-", sep="", end="", flush=True)
    logging.info("Printed %s dashes" % width)
    logging.fatal("Unknown error (%s)" % ename)
    cprint.fatal(_("An unknown error occured. Please file an Issue at github.com/thetechrobo/support."))
finally:
    logging.info("Program stopped execution.")
#EOF
