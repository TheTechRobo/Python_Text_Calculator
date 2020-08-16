def clearScreen():
    """
    Credit:
    https://www.sololearn.com/Discuss/764024/how-to-clear-the-screen-in-python-terminal
    """
    import os
    if os.name == "nt":
        print (chr(12))
    else:
        esc = chr(27)
        print(esc + '[2J' + esc + '[0;0H')
