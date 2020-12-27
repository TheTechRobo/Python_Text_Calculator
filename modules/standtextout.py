import os

def standTextOut(string, printMechanismDash=print, printMechanismString=print):
    """
    param string: the string to sandwich in between the dashes.
    param printMechanismDash: how it will output the dashes. e.g. do `logging.info' to output it with logging.info. Defaults to print.
        ***IF YOU CHOOSE A PRINT MECHANISM IT NEEDS TO BE IMPORTED IN YOUR ORIGINAL PROGRAM, **NOT** THIS MODULE! How does it work?! you pass the function of output and it uses it.
    param printMechanismString: how it will output the string that is sandwidched in between the dashes. Defaults to print.
        ***READ THE ABOVE IMPORTANT NOTICE (of printMechanismDash)!!!***
    """
    width = os.get_terminal_size().columns
    dashes = "-" * width
    printMechanismDash(dashes)
    printMechanismString(string.center(width))
    printMechanismDash(dashes)

def standTextOut_Return(string):
    """
    Will return the finished string so you can output it the way you want.
    """
    width = os.get_terminal_size().columns
    result = "-" * width
    result = (result + "\n" + string.center(width))
    result = (result + "\n" + ("-" * width))
    return result
