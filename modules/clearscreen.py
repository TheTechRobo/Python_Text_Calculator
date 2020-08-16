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
    """This will work most of the time. Tries three times to clear the screen."""
    print(chr(27)+'[2j') #first attempt at clearing the screen w/ ansi escape codes
    print('\033c')#second attempt at clearing the screen w/ ansi escape codes
    print('\x1bc')#third attempt at clearing the screen w/ ansi escape codes

def clearScreenV1():
    """Harder to understand but a two-liner. Doesn't work if the user doesn't have `clear' or `cls' installed."""
    import os
    os.system("cls" if os.name == "nt" else "clear")
