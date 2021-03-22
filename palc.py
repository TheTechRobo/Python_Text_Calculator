# Imports
try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError
import sys
try:
    import modules.clearscreen as clearscreen
    from modules.cprint import cprint
    import modules.standtextout as standtextout
    import modules.pressanykey as pressanykey
    import gettext, time, logging
except Exception as ename:
    print("ERROR 0: COULD NOT LOAD NECESSARY MODULES.\nThis is a fatal error. (%s)" % ename)
    sys.exit(1)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller (https://stackoverflow.com/questions/61718298/compiling-gettext-locales-with-pyinstaller-in-python-3-x)
"""
    import os.path
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

standtextout.standTextOut("Translation Selection", cprint.ok, cprint.info)

print("And that's it for now.")
