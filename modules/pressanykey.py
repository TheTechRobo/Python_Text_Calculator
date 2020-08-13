def pressanykey():
    """
    SOURCE: https://raw.githubusercontent.com/TheTechRobo/python-text-calculator/master/FOR%20CLEARING%20THE%20SCREEN%20AND%20PRESS%20ANY%20KEY%20TO%20CONTINUE.md
    """
    import sys
    try:
        import msvcrt
        windows = True
    except ImportError:
        import tty
        import termios
        windows = False
    print("Press any key to continue...", end="", flush=True)
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
