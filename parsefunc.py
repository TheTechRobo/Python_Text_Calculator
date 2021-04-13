import sys
def parseCalc(calc):
    calc = calc.replace('\u200b', '').replace('\\', '').replace('\'', '').strip().lower() #gets rid of the common stuff, without having to use core words and whatnot
    if "/" in calc or calc == _("division"):
        pass
    elif calc == _("exit") or calc == _("quit") or calc == _("bye") or calc == _("leave"):
        sys.exit()
    pass
