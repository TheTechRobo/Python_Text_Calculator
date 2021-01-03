def clearScreen():
    """
    Credit:
    https://www.sololearn.com/Discuss/764024/how-to-clear-the-screen-in-python-terminal
    """
    import os
    if os.name == "nt": #Windows
        print(chr(12))
    else: #linux/macos
        esc = chr(27)
        print(esc + '[2J' + esc + '[0;0H')

def clearScreenOld():
    """This will NOT work on windows unless you have colorama package. Tries three times to clear the screen."""
    print(chr(27)+'[2j') #first attempt at clearing the screen w/ ansi escape codes
    print('\033c')#second attempt at clearing the screen w/ ansi escape codes
    print('\x1bc')#third attempt at clearing the screen w/ ansi escape codes

def clearScreenV1():
    """Harder to understand but not many lines (can be shortened to two by putting imports on the same line, and removing the del statement). Doesn't work if the user doesn't have `clear' or `cls' installed."""
    import os
    import subprocess
    subprocess.Popen(["cls" if os.name == "nt" else "clear"], shell=False)
    del os, subprocess
