# -*- coding: utf-8 -*-
u"""
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
LICENSE: GPL 3.0 (see LICENSE)
"""
from __future__ import absolute_import
try:
    import six
    if not six.PY3:
        print u"You are using a currently unsupported version of Python. Your mileage may vary."
except (ImportError, ModuleNotFoundError):
    print u"Can't find what version of Python you're running. Your mileage may vary."

def resource_path(relative_path):
    u""" Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(u".")

    return os.path.join(base_path, relative_path)

# IMPORTS
print u"Loading initial Palc files..."
try:
    import os.path
    import gettext #to translate Palc
    from sys import exit as e #for exiting
    from modules.cprint import cprint #printing in colour
    from modules.clearscreen import clearScreen #clear the screen
    from modules.pressanykey import pressanykey #for the press any key to continue
    from modules.standtextout import standTextOut #for the dash thing
    import time #self explanatory
    import sys #for misc
    import logging #self explanatory
except Exception, ename:
    print u"Errid 0: Could not load required modules! (%s)" % ename
    exit(1)
try:
    import colorama
    colorama.init() #will fix bugs on CMD
except ImportError:
    print u"I've detected you don't have colorama package installed. It's suggested, if you're on Windows, to install this package (`pip install colorama`), to increase the chances of Palc working correctly. This module is unnecessary for all other operating systems."
logging.basicConfig(filename=u"palc.log", level=logging.DEBUG, format=u'%(levelname)s @ %(asctime)s %(message)s. Logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt=u'%d/%m/%Y %H:%M:%S') #set up logging, thanks for this website www.programcreek.com/python/example/136/logging.basicConfig for a few great examples!
#ask for language
standTextOut(u"Language Selection // Language", sys.stdout.write, cprint.info)
cprint.info(u"1 - English // Anglais\n2 - Français // French")
while True:
    try:
        language = int(raw_input(u"Type: "))
    except ValueError, ename:
        logging.info(u"ValueError in language select (%s)" % ename)
        cprint.err(u"Invalid input // Entrée invalide")
        continue
    if language == 1:
        lCode = u"en"
        break
    elif language == 2:
        lCode = u"fr"
        break
if lCode not in [u"en", u"fr"]:
    logging.fatal(u"USER DID NOT SPECIFY A VALID LANGUAGE!")
    cprint.warn(u"This language doesn't exist. Did you mean...\nEnglish? // Ce language n'existe pas. Tu peut-être veux dire ...\nAnglais ? (Y/n) ")
    if raw_input()[0].lower() == u"y":
        logging.info(u"Nvm, they meant English.")
        ignore = u"n"
    else:
        cprint.fatal(u"Abort.", interrupt=True)
try:
    gettext.bindtextdomain(u"base", localedir=u"locales")
    lang_translations = gettext.translation(u"base", localedir=resource_path(u"locales"), languages=[lCode])
except Exception, ename:
    logging.fatal(u"Could not get translations. This is fatal. (%s)" % ename)
    cprint.fatal(u"Could not get translations! Make sure that the `locales' directory exists in the current working directory. // Les traductions sont inaccessables ou ne fonctionnes pas !")
    if lCode == u"en":
        cprint.info(u"This is not fatal with English translations, we can ignore it.")
        ignore = raw_input(u"Ignore? (Y/n): ").lower()
        if ignore[0] == u"n":
            cprint.fatal(u"Abort.", interrupt=True)
        else: #if user chooses to ignore
            cprint.info(u"Defaulting to YES.")
            logging.info(u"User ignored error!")
            def _(theEnglishString): #define a function that does nothing except give the value back so that NameErrors dont occur
                return theEnglishString
    else:
        e(1)
else:
    ignore = u"undefined"
cprint.ok(u"Loading Palc files...\n")
lang_translations.install()
_ = lang_translations.gettext #if both of these fail we're screwed anyway, and im NOT adding the ignoring support here
#import func and parsefunc
logging.info(u"Attempting to import parsefunc.py..")
try:
    from parsefunc import *
except Exception, e:
    logging.critical(u"Could not access file parsefunc.py (%s)" % e)
    cprint.fatal(_(u"I can't load the file parsefunc.py. This file is necessary for proper function of the Software."), interrupt=True)
try:
    if ignore[0] == u"y":
        from parsefunc import main
        main(_)
except Exception, ename:
    logging.info(u"Exception doing the if ignore[0] == \"y\" bit (%s)" % ename)
    cprint.err(_(u"Unexpected error! See below for details."))
    raise
time.sleep(1)
def palc():
    while True:
       pressanykey(_(u"Press any key to continue..."))
       clearScreen()
#CALCULATION CHOICE
       calc = raw_input(_(u"What calculation do you wish to do? (Type `?' for a list of commands)\nType: "))
       logging.info(u"Got calc choice %s" % calc)
       calc = calc.lower() #make variable "calc" lowercase
#HELP
       if u"?" in calc:
           logging.info(u"User needed help")
           misc.h()
       elif _(u"help") in calc:
           logging.info(u"User needed help")
           misc.h()
#TAX
       elif _(u"tax") in calc:
            misc.showUserWhatIThink(_(u"calculate tax"))
            Tax.taxCalc()
#SQUARE
       elif _(u"sq") in calc:
            misc.showUserWhatIThink(_(u"square a number"))
            n = int(raw_input(_(u"Number to square? ")))
            cprint.info(n * n)
            logging.info(u"User squared number %s got result %s" % (n, (n * n)))
       elif u"[]" in calc:
            misc.showUserWhatIThink(_(u"square a number"))
            n = int(raw_input(_(u"Number to square? ")))
            logging.info(u"User squared number %s got result %s" % (n, (n * n)))
            cprint.info(n * n)
#DIVISION
       elif u"/" in calc:
            misc.showUserWhatIThink(_(u"divide a number"))
            theBasics.division()
       elif _(u"div") in calc:
            misc.showUserWhatIThink(_(u"divide a number"))
            theBasics.division()
#SUBTRACTION
       elif u"-" in calc:
            misc.showUserWhatIThink(_(u"subtract a number from a number"))
            theBasics.subtraction()()
       elif _(u"sub") in calc:
            misc.showUserWhatIThink(_(u"subtract a number from a number"))
            theBasics.subtraction()
       elif _(u"min") in calc:
            misc.showUserWhatIThink(_(u"subtract a number from a number"))
            theBasics.subtraction()
#ADDITION
       elif u"+" in calc:
            misc.showUserWhatIThink(_(u"add two numbers"))
            theBasics.addition()
       elif _(u"add") in calc:
            misc.showUserWhatIThink(_(u"add two numbers"))
            theBasics.addition()
       elif _(u"plus") in calc:
            misc.showUserWhatIThink(_(u"add two numbers"))
            theBasics.addition()
       elif lCode == u"fr":
            if u"ajoute" in calc:
                misc.showUserWhatIThink(_(u"add two numbers"))
                theBasics.addition()
#MODULO
       elif u"%" in calc:
            print _(u"1 - Find the remainder of two numbers after division\n\
2 - Use the percentage calculator.\n\
Anything else - Back to menu.")
            pOrMod = raw_input(_(u"Type: "))
            if pOrMod == u"1":
                theBasics.mod()
            elif pOrMod == u"2":
                Percentage.chooseOneTwo()
            else:
                cprint.info(_(u"going back."))
                logging.info(u"going back.")
       elif _(u"mod") in calc:
            misc.showUserWhatIThink(_(u"find the remainder of two numbers after division"))
            theBasics.mod()
#AREA
       elif _(u"area") in calc:
            misc.showUserWhatIThink(_(u"calculate area"))
            misc.area()
       elif u"#" in calc:
            misc.showUserWhatIThink(_(u"calculate area"))
            misc.area()
#VOLUME
       elif _(u"vol") in calc:
            misc.showUserWhatIThink(_(u"use the volume calculator"))
            misc.vol()
#CUBE
       elif u"{}" in calc:
            misc.showUserWhatIThink(_(u"cube a number"))
            cubedNumber = int(raw_input(_(u"\nType the number to be cubed: ")))
            print
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info(u"User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print
       elif _(u"cube") in calc:
            misc.showUserWhatIThink(_(u"cube a number"))
            cubedNumber = int(raw_input(_(u"\nType the number to be cubed: ")))
            print
            cprint.info(cubedNumber ** 3) #Manually cube number
            logging.info(u"User cubed number %s got result %s" % (cubedNumber, (cubedNumber ** 3)))
            print
#SPINNER
       elif _(u"spin") in calc:
            misc.showUserWhatIThink(_(u"spin a spinner"))
            misc.spinner()
       elif _(u"spinner") in calc:
            misc.showUserWhatIThink(_(u"spin a spinner"))
            misc.spinner()
       elif _(u"roulette") in calc:
            misc.showUserWhatIThink(_(u"spin a spinner"))
            misc.spinner()
#EXIT
       elif _(u"quit") in calc:
            misc.showUserWhatIThink(_(u"quit"))
            logging.info(u"User exited using `quit' command")
            e()
       elif _(u"exit") in calc:
            misc.showUserWhatIThink(_(u"exit"))
            logging.info(u"User exited using `exit' command")
            e()
#EXPONENTS
       elif _(u"power") in calc:
            misc.showUserWhatIThink(_(u"use the exponent function"))
            rootsAndTheOtherOne.powerful()
       elif _(u"ex") in calc:
            misc.showUserWhatIThink(_(u"use the exponent function"))
            rootsAndTheOtherOne.powerful()
       elif u"^" in calc: #IDEA SOURCE: 3N4N's (first) Pull Request on the original repo
            misc.showUserWhatIThink(_(u"use the exponent function"))
            rootsAndTheOtherOne.powerful()
#MULTIPLICATION
       elif u"*" in calc:
            misc.showUserWhatIThink(_(u"multiply a number"))
            theBasics.multiplication()
       elif u"x" in calc:
            misc.showUserWhatIThink(_(u"multiply a number"))
            theBasics.multiplication()
       elif _(u"multi") in calc:
            misc.showUserWhatIThink(_(u"multiply a number"))
            theBasics.multiplication()
#CUBE TWICE
       elif u"{2}" in calc:
            cprint.err(_(u"The \"cube twice\" feature was discontinued as it was pointless. Sorry for the inconvenience."))
            logging.error(u"User attempted to use cube twice function but it's gone")
#ROOTS
       elif _(u"root") in calc:
            misc.showUserWhatIThink(_(u"use the root function (opposite of exponents)"))
            root = raw_input(_(u"Square root or cube root? (square/cube)\nType: ")).lower()
            if _(u"square") in root:
                rootsAndTheOtherOne.sqroot()
            elif _(u"cube") in root:
                rootsAndTheOtherOne.curoot()
            else:
                cprint.err(_(u"Currently I don't support the root you chose. Hopefully this will change :D"))
                logging.error(u"User used non-existent root (%s)" % root)
#EASTER EGG!
       elif u"=" in calc:
            misc.showUserWhatIThink(_(u"use the equals function (completely useless)"))
            number = int(raw_input(_(u"\nType in a number: ")))
            if number == 42:
                cprint.info(_(u"=42 -- the answer to life, the universe, and everything"))
                logging.info(u"User got the easter egg")
            else:
                cprint.info(_(u"Calculating..."))
                time.sleep(3)
                cprint.err(_(u"ERROR: Too big of a number, timed out!"))
                logging.info(u"User used the `=' feature for number %s" % number)
#NUMBER SYSTEMS
       elif _(u"base") in calc:
            misc.showUserWhatIThink(_(u"convert number systems"))
            misc.base()
#ORD
       elif _(u"ord") in calc:
           misc.showUserWhatIThink(_(u"ord a character"))
           result = unicode(ord(raw_input(_(u"Type in the character to ord: "))))
           logging.info(u"User ord'ed to get result %s" % result)
           cprint.info(_(u"The result is: \n%s" % result))
#LOGARITHM
       elif _(u"log") in calc:
           misc.showUserWhatIThink(_(u"use the logarithm function"))
           misc.logarithm()
#MEMORY
       elif _(u"mem") in calc:
            misc.showUserWhatIThink(_(u"use the memory function"))
            memOrRecall = raw_input(_(u"Would you like to set the memory or recall? (set / recall)\nType: "))
            if _(u"set") in memOrRecall.lower():
                misc.remember()
            elif _(u"recall") in memOrRecall.lower():
                misc.readMyMemory()
            else:
                cprint.err(_(u"You did not type an answer.\nAbort."))
                logging.error(u"User didn't type an answer in MEM function (typed %s)" % memOrRecall)
#FIBONACCI
       elif _(u"fib") in calc:
            misc.showUserWhatIThink(_(u"use the fibonacci calculator"))
            cprint.ok(_(u"Starting fibonacci sequence. Please wait."))
            misc.fib()
#PERCENTAGE
       elif _(u"percent") in calc: #SOURCE: https://stackoverflow.com/a/5998010/9654083
            misc.showUserWhatIThink(_(u"use the percentage function"))
            Percentage.chooseOneTwo()
#INTEREST
       elif _(u"interest") in calc:
            misc.showUserWhatIThink(_(u"use the interest calculator"))
            misc.calculateInterest()
#TEMPERATURE
       elif _(u"temperature") in calc:
            misc.showUserWhatIThink(_(u"use the temperature converter"))
            Temperature.tempCalc()
#CONVERSIONS
       elif _(u"conver") in calc:
            logging.info(u"use the converter functions")
            misc.showUserWhatIThink(_(u"use the converter functions"))
            conversion = int(raw_input(_(u"1 - Convert temperature units\n2 - Convert bits and bytes and kilobytes and mebibytes and stuff\nType: ")))
            if conversion == 1:
                Temperature.tempCalc()
            else:
                cprint.err(_(u"Not developed yet, but maybe soon! :D"))
                logging.info(u"User typed %s into conver functions but Non Existent." % conversion)
       elif u"raise" in calc:
           cprint.info(_(u"This feature has been disabled due to security reasons."))
           #exception = input("DEV ONLY - Which exception would you like to raise?")
           #exec("raise %s" % exception)
#OTHERWISE
       elif calc == u"":
            logging.error(u"User attempted to type nothing as a command")
            cprint.err(_(u"I can't heeeeaaaarrrrrr yooooouuuuuuuu"))
       elif calc == u" ":
            logging.error(u"user said nothing")
            cprint.err(_(u"You speak quietly"))
       elif calc is None:
            logging.error(u"User attempted to type nothing as a command")
            cprint.err(_(u"I can't heeeaaaarrrrr youuuuuuuu"))
       else:
            logging.error(u"User typed an invalid command (%s)" % calc)
            cprint.err(_(u'''
I don't understand your request. Here are the currently supported calculations:
multiplication, division, subtraction, addition, modulo, square, area, volume, cube, power, root, ord, fibonacci, logarithm, memory, percentage calculator, interest calculator, temperature, and base. Sorry for the inconvenience
'''))
standTextOut(_(u"Welcome to Palc!"), sys.stdout.write, cprint.info)
try:
    palc() #run all that code
except SyntaxError, ename: #easter eggz
    raise #raise exact same exception
except KeyboardInterrupt: #if ^C
    logging.info(u"KeyboardInterrupt")
    cprint.ok(_(u"\nNote that you CAN type `quit' instead of pressing the interrupt key"))
    e(0)
except EOFError: #if ^D
    logging.info(u"EOFError")
    cprint.ok(_(u"\nWhy ^D? Why not just type `quit'?"))
    e(0)
except (ValueError, TypeError), ename:
    logging.critical(u"ValueError or TypeError: %s" % ename)
    standTextOut(_(u"\aERROR!\a"), sys.stdout.write, cprint.err) #\a means beep the computer :D
    cprint.fatal(_(u"You typed in an invalid integer or float. Or maybe the program needs debugging. Either way, it's a pretty big error."), interrupt=True)
except SystemExit:
    cprint.ok(_(u"Looks like you exited."))
    logging.info(u"Not necessary to be logged, but SystemExit was thrown")
except Exception, ename:
    standTextOut(_(u"\aUnknown Error!\a"), sys.stdout.write, cprint.fatal) #\a makes a beep
    logging.fatal(u"Unknown error (%s)" % ename)
    cprint.fatal(_(u"An unknown error occured. Please file an Issue at github.com/thetechrobo/python-text-calculator/issues."))
finally:
    logging.info(u"Program finished.")
#EOF
