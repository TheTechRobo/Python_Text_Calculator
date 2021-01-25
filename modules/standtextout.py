from __future__ import print_function
import os
import sys
if not hasattr(os, 'get_terminal_size'):
    def get_terminal_size():
        try:
            stty_size = subprocess.check_output(
                ['stty', 'size'],
                stderr=subprocess.PIPE,
            ).decode('utf-8')
            lines_str, columns_str = stty_size.split()
            return (int(columns_str), int(lines_str))
        except Exception:
            return (80, 24)

    os.get_terminal_size = get_terminal_size

if sys.version_info[:2] < (3, 3):
    old_print = print
    def print(*args, **kwargs):
        flush = kwargs.pop('flush', False)
        old_print(*args, **kwargs)
        if flush:
            file = kwargs.get('file', sys.stdout)
            # Why might file=None? IDK, but it works for print(i, file=None)
            file.flush() if file is not None else sys.stdout.flush()

def standTextOut(string, printMechanismDash=print, printMechanismString=print):
    """
    param string: the string to sandwich in between the dashes.
    param printMechanismDash: how it will output the dashes. e.g. do `logging.info' to output it with logging.info. Defaults to print.
        ***IF YOU CHOOSE A PRINT MECHANISM IT NEEDS TO BE IMPORTED IN YOUR ORIGINAL PROGRAM, **NOT** THIS MODULE! How does it work?! you pass the function of output and it uses it.
    param printMechanismString: how it will output the string that is sandwidched in between the dashes. Defaults to print.
        ***READ THE ABOVE IMPORTANT NOTICE (of printMechanismDash)!!!***
    """
    try: #python3
        width = os.get_terminal_size().columns
    except Exception:
        width = os.get_terminal_size()[0]
    dashes = "-" * width
    printMechanismDash(dashes)
    printMechanismString(string.center(width))
    printMechanismDash(dashes)

def standTextOut_Return(string):
    """
    Will return the finished string so you can output it the way you want.
    """
    try: #python3
        width = os.get_terminal_size().columns
    except Exception:
        width = os.get_terminal_size()[0]
    result = "-" * width
    result = (result + "\n" + string.center(width))
    result = (result + "\n" + ("-" * width))
    return result
