from __future__ import print_function
def pressanykey(string="Press any key to continue..."):
    """
    SOURCE: https://raw.githubusercontent.com/TheTechRobo/python-text-calculator/master/FOR%20CLEARING%20THE%20SCREEN%20AND%20PRESS%20ANY%20KEY%20TO%20CONTINUE.md
    (set noGettext to True if you get an error that _ is not defined)
    """
    import sys
    try:
        import msvcrt
        windows = True
    except ImportError:
        import tty
        import termios
        windows = False
    print(string, end="", flush=True)
    if windows:
       msvcrt.getch()
    else:
       fd = sys.stdin.fileno()
       settings = termios.tcgetattr(fd)
       try:
           tty.setraw(sys.stdin.fileno())
           sys.stdin.read(1)
       finally:
           termios.tcsetattr(fd, termios.TCSADRAIN, settings)
