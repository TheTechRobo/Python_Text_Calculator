def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller https://stackoverflow.com/a/44352931/9654083"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# https://dzone.com/articles/listing-a-directory-with-python

oldCalc = "no u"
# Basic Setup
try:
    import sys, turbofunc, gettext, time, logging, platform, os, os.path, runpy
    import parsefunc
    from cprint_inter import cprint
except Exception as ename:
    if "parsefunc" in ename:
        raise
    print("ERROR 0: COULD NOT LOAD NECESSARY MODULES.\nThis is a fatal error. (%s)\nHINT: Try `pip install -r requirements.txt'." % ename)
    sys.exit(8)

try:
    import colorama
    colorama.init() #fixes bugs in CMD
except (ImportError, ModuleNotFoundError):
    if platform.system() == "Windows" or platform.system() == "":
        print("I have noticed that you may be running on Windows without colorama installed (pip install colorama).\nIf you experience issues with Palc like seeing weird characters instead of colours, try installing colorama.")

logging.basicConfig(filename="palc.log", level=logging.INFO, format='%(levelname)s @ %(asctime)s: %(message)s. This was logged on line %(lineno)d in function %(funcName)s, file %(filename)s.', datefmt='%d/%m/%Y %H:%M:%S') #set up logging.
logging.debug("Logging works!")

# Modular Translation Scheme
try:
    turbofunc.standTextOut("Translation Selection", cprint.ok, cprint.info)
    cprint.info("Checking for locales... Please stand by.", end="", flush=True)
    listing = os.listdir(resource_path("locales"))
    time.sleep(0.211)
    cprint.info("\rParsing list...", end="", flush=True)
    settings = runpy.run_path(resource_path("locales/CONFIG/config.py")) #https://stackoverflow.com/a/37339817/9654083
    print("\r" + "\n\033[1A", end="")
    pos = 1
    for item in settings["GETTEXT_NAMES"]:
        cprint.info("%s. %s" % (pos, item))
        pos += 1
    pos -= 1
    time.sleep(0.3)
    input_invalid_eh = True
    while input_invalid_eh:
        try:
            translatio = turbofunc.CleanInput(input("Please type the number corresponding to the language of choice..."))
            translation = int(translatio)
            if translation > pos or translation < 1:
                raise ValueError
        except ValueError:
            if not ("translation" in globals()):
                translation = translatio
            if translation == "":
                translation = "(blank)"
            cprint.err("\033[F %s: Invalid input, try again." % translation)
            input_invalid_eh = True
            del translation, translatio
        else:
            input_invalid_eh = False
    logging.debug("Selected translation %s" % (translation - 1))
    LANG = list(settings["GETTEXT_NAMES"])[translation - 1]
    LANG = settings["GETTEXT_NAMES"][LANG]
    lang_translations = gettext.translation("base", localedir=resource_path("locales"), languages=[LANG])
    lang_translations.install()
    del translatio, translation, LANG, settings, pos, runpy, input_invalid_eh
except (KeyboardInterrupt, EOFError):
    sys.exit(0)

turbofunc.multiprint({_("\nWelcome to "): cprint.info, _("Palc"): cprint.ok, "!" + "\n": cprint.info}, _=_, no=True, end="", flush=True)
time.sleep(1)
def mainloop():
    calc = []
    global oldCalc
    if sys.stdin.isatty():
        turbofunc.pressanykey()
        turbofunc.clearScreen()
        turbofunc.multiprint({"\n" + _("Welcome to "): cprint.info, _("Palc"): cprint.ok, "!\n": cprint.info, _("Please enter a command..."): cprint.ok}, no=True, _=_, end="",flush=True)
        cprint.warn("\nEnter HELP for help", flush=True)
        string = ("                           \033[A\033[A")
        while True:
            keypress = turbofunc.pressanykey(string=string, decodeGetchToUnicode=True)
            if keypress == "\r" or keypress == "\n" or keypress == "\r\n":
                print()
                parsefunc.parseCalc("".join(calc)) #https://www.geeksforgeeks.org/python-convert-list-characters-string/
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
            if keypress == "\x04": # pylint: disable=no-else-raise
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
            cprint.warn("It's suggested to run EXIT instead of ^D.")
        turbofunc.standTextOut(_("Bye!"), printMechanismString=cprint.ok)
        sys.exit(0)
    except KeyboardInterrupt as ename:
        print()
        turbofunc.standTextOut(_("Bye!"), printMechanismString=cprint.ok)
        sys.exit(0)
    except ZeroDivisionError:
        turbofunc.standTextOut("Oops!", cprint.warn, cprint.err)
        # FOR TRANSLATORS: **PLEASE** keep the \033[1m and \033[0m and \n
        cprint.err(_("I see you divided by 0. \033[1mPlease don't do that\033[0m"), end="")
        # FOR TRANSLATORS: This is not a typo. It is a continuation of "Please don't do that".
        cprint.err(_(", as it doesn't work."))
        cprint.info(_("Think of it as Siri does. Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends."))
        cprint.warn(_("Boom. Roasted."))
    except Exception as ename:
        turbofunc.standTextOut("Oops!", cprint.warn,cprint.err)
        cprint.warn(_("Unknown error!"))
        if input(_("Get a backtrace? ")).lower().strip()[0] == "y":
            raise
