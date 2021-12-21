# https://dzone.com/articles/listing-a-directory-with-python
MANYSPACE = "                                 " #todo: check terminal size then subtract character count from it
oldCalc = "no u"
# Basic Setup
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError
import sys
try:
    from cprint import cprint
    import turbofunc, gettext, time, logging, os, os.path, parsefunc, runpy
except Exception as ename:
    if "No module named 'parsefunc'" in str(ename):
        cprint.fatal("\n\n\nERROR 0: COULD NOT LOAD PARSEFUNC.\nThis is a fatal error. Please contact TheTechRobo.\n\n")
        sys.exit(8)
    print("ERROR 0: COULD NOT LOAD NECESSARY MODULES.\nThis is a fatal error. (%s)\nHINT: Try `pip install -r requirements.txt'." % ename)
    sys.exit(1)
logging.basicConfig(filename="palc.log", level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s. This was logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S') #set up logging.

logging.debug("Logging works!")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller https://stackoverflow.com/a/44352931/9654083"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

try:
    import colorama
    colorama.init() #fixes bugs in CMD
except (ImportError, ModuleNotFoundError):
    import platform
    if platform.system() == "Windows" or platform.system() == "":
        print("I have noticed that you may be running on Windows without colorama installed (pip install colorama).\nIf you experience issues with Palc like seeing weird characters instead of colours, try installing colorama.")

# Modular Translation Scheme
try:
    turbofunc.standTextOut("Translation Selection", cprint.ok, cprint.info)
    cprint.info("Checking for locales... Please stand by." + MANYSPACE, end="", flush=True)
    time.sleep(0.3) #makes it more professional
    listing = os.listdir(resource_path("locales"))
    cprint.info("\rParsing list..." + MANYSPACE, end="", flush=True)
    settings = runpy.run_path(resource_path("locales/CONFIG/config.py")) #https://stackoverflow.com/a/37339817/9654083
    time.sleep(0.3)
    print("\r" + MANYSPACE)
    pos = 1
    for item in settings["GETTEXT_NAMES"]:
        cprint.info("%s. %s" % (pos, item))
        pos += 1
    pos -= 1
    input_invalid_eh = True
    while input_invalid_eh:
        try:
            #todo: use turbofunc sanitise input
            translation = int(turbofunc.CleanInput(input("Please type the number corresponding to the language of choice...")))
            if translation > pos or translation < 1:
                raise ValueError
        except ValueError:
            if "translation" in globals():
                pass
                #print("\ntranslationinglobals\n")
            else:
                translation = ""
            if translation == "":
                translation = "(blank)"
            cprint.err("\033[F %s: Invalid input, try again." % translation + MANYSPACE * 2)
            input_invalid_eh = True
        else:
            input_invalid_eh = False
    logging.debug("Selected translation %s" % (translation - 1))
    LANG = list(settings["GETTEXT_NAMES"])[translation - 1]
    LANG = settings["GETTEXT_NAMES"][LANG]
    lang_translations = gettext.translation("base", localedir=resource_path("locales"), languages=[LANG])
    lang_translations.install()
    del translation, LANG, settings, pos, runpy, input_invalid_eh
except (KeyboardInterrupt, EOFError):
    sys.exit(0)

turbofunc.multiprint({_("\nWelcome to "): cprint.info, _("Palc"): cprint.ok, "!" + MANYSPACE + "\n": cprint.info}, _=_, end="", flush=True)
time.sleep(1)
def mainloop():
    calc = []
    global oldCalc
    if sys.stdin.isatty():
        turbofunc.pressanykey()
        turbofunc.clearScreen()
        turbofunc.multiprint({_("\nWelcome to "): cprint.info, _("Palc"): cprint.ok, "!%s\n" % MANYSPACE: cprint.info, _("Please enter a command..."): cprint.ok}, _=_, end="",flush=True)
        cprint.warn("\nEnter HELP for help", flush=True)
        string = ("                           \033[A\033[A")
        while True:
            keypress = turbofunc.pressanykey(string=string, decodeGetchToUnicode=True)
            if keypress == "\r" or keypress == "\n" or keypress == "\r\n":
                print()
                a = ""
                for i in calc:
                    a += i
                calc = a
                del a
                parsefunc.parseCalc(calc)
                break
            if keypress == "\x7f" or keypress == "\b":
                if len(calc) == 0:
                    string = ""
                    continue
                print("\b ", end="")
                string = "\b"
                calc = calc[:-1] #https://stackoverflow.com/a/15478161/9654083
                continue
            if keypress == "\x1b":
                if oldCalc == "no u":
                    cprint.warn(_("\nHa...ha...not...funny...whoever you are."))
                    sys.exit(69)
                calc += oldCalc
                print(oldCalc, end="", flush=True)
                continue
            if keypress == "\x03":
                raise KeyboardInterrupt
            if keypress == "\x04":
                raise EOFError
            else:
                print(keypress, end="", flush=True)
                calc += keypress
            string = ""
    else:
        time.sleep(1.4)
        calc = input(_("Waiting for command..."))
        time.sleep(0.8)
        parsefunc.parseCalc(calc)
    logging.debug("calc: %s" % calc)
    logging.debug("oldcalc: %s" % oldCalc)
    oldCalc = calc
while True:
    try:
        mainloop()
    except ValueError as ename:
        turbofunc.standTextOut(_("Oops!"),cprint.warn,cprint.err)
        logging.info("VALUEERROR: %s" % ename)
        cprint.err(_("You raised a ValueError! This is typically caused by an erroneous input. If it wasn't, please file a bug report at github.com/thetechrobo/python-text-calculator/issues.\nFor further information, get a backtrace."))
        if input(_("Get a backtrace? ")).lower().strip()[0] == "y":
            raise
        cprint.warn(_("Aborting backtrace."))
    except TypeError as ename:
        turbofunc.standTextOut(_("Oops!"),cprint.warn,cprint.err)
        logging.info("TYPEERROR: %s" % ename)
        cprint.err(_("You raised a TypeError! This is odd. If you are sure that your inputs were correct, please file a bug report at github.com/thetechrobo/python-text-calculator/issues.\nFor further information, get a backtrace."))
        if input(_("Get a backtrace? ")).lower().strip()[0] == "y":
            raise
        cprint.warn(_("Aborting backtrace."))
    except EOFError as ename:
        if not sys.stdin.isatty():
            cprint.warn("Your batch script ended prematurely. Next time, run the command \"exit\".")
        else:
            cprint.warn("It's suggested to run EXIT instead of ^D." + MANYSPACE)
        turbofunc.standTextOut(_("Bye!"), printMechanismString=cprint.ok)
        sys.exit(0)
    except KeyboardInterrupt as ename:
        print()
        turbofunc.standTextOut(_("Bye!"), printMechanismString=cprint.ok)
        sys.exit(0)
    except Exception as ename:
        turbofunc.standTextOut("Oops!", cprint.warn,cprint.err)
        cprint.warn(_("Unknown error!"))
        if input(_("Get a backtrace? ")).lower().strip()[0] == "y":
            raise
