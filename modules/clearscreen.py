def clearScreen():
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    #(Credit for the above: https://raw.githubusercontent.com/TheTechRobo/python-text-calculator/master/FOR%20CLEARING%20THE%20SCREEN%20AND%20PRESS%20ANY%20KEY%20TO%20CONTINUE.md
    print("\n\n")
