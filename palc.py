# https://dzone.com/articles/listing-a-directory-with-python
MANYSPACE = "                                 "
# Basic Setup
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError
import sys
try:
    from cprint import cprint
    from runpy import run_path
    import turbofunc, gettext, time, logging, os, os.path, parsefunc
except Exception as ename:
    print("ERROR 0: COULD NOT LOAD NECESSARY MODULES.\nThis is a fatal error. (%s)" % ename)
    sys.exit(1)
logging.basicConfig(filename="palc.log", level=logging.DEBUG, format='%(levelname)s @ %(asctime)s: %(message)s. This was logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S') #set up logging.

logging.debug("Logging works!")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller (https://stackoverflow.com/questions/61718298/compiling-gettext-locales-with-pyinstaller-in-python-3-x)
"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
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
    time.sleep(0.4) #makes it more professional
    listing = os.listdir(resource_path("locales"))
    cprint.info("\rParsing list..." + MANYSPACE, end="", flush=True)
    settings = run_path("locales/config.py") #https://stackoverflow.com/a/37339817/9654083
    pos = 1
    time.sleep(0.5)
    print("\r" + MANYSPACE)
    for item in settings["GETTEXT_NAMES"]:
        cprint.info("%s. %s" % (pos, item))
    pos += 1
    del pos, run_path
    translation = int(input("Please type the number corresponding to the language of choice...")) - 1
    LANG = list(settings["GETTEXT_NAMES"])[translation]
    LANG = settings["GETTEXT_NAMES"][LANG]
    lang_translations = gettext.translation("base", localedir=resource_path("locales"), languages=[LANG])
    lang_translations.install()
    del translation, LANG, settings
except (KeyboardInterrupt, EOFError):
    sys.exit(0)

turbofunc.multiprint({"\nWelcome to ": cprint.info, "Palc": cprint.ok, "!" + MANYSPACE + "\n": cprint.info}, _=_, end="", flush=True)
time.sleep(1)
def mainloop():
    if sys.stdin.isatty:
        turbofunc.pressanykey()
        turbofunc.clearScreen()
    turbofunc.multiprint({"\nWelcome to ": cprint.info, "Palc": cprint.ok, "!" + MANYSPACE + "\n": cprint.info, "Please enter a command...": cprint.ok}, _=_, end="",flush=True)
    cprint.warn("\nEnter HELP for help")
    calc = input("                           \033[A\033[A")
    parsefunc.parseCalc(calc)
while True:
    try:
        mainloop()
    except ValueError:
        turbofunc.standTextOut("Oops!",cprint.warn,cprint.err)
        cprint.err("You raised a ValueError! This is typically caused by an erroneous input. If it wasn't, please file a bug report at github.com/thetechrobo/python-text-calculator/issues.")
    except TypeError:
        turbofunc.standTextOut("Oops!",cprint.warn,cprint.err)
        cprint.err("You raised a TyepError! This may be because of a bug in Palc. If you are sure that your inputs were correct, please file a bug report at github.com/thetechrobo/python-text-calculator/issues.")
    except EOFError:
        if sys.stdin.isatty:
            cprint.warn("Your batch script ended prematurely. Next time, run the command \"exit\".")
        else:
            cprint.warn("It's suggested to run EXIT instead of ^D." + MANYSPACE)
        cprint.info("Bye!" + MANYSPACE)
        sys.exit(0)
