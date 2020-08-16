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
