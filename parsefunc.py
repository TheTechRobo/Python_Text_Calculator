import sys, logging, turbofunc
from cprint import cprint
def showUserWhatIThink(msg):
    cprint.ok(_("BTW, I parsed your choice as:\n%s") % msg)
    logging.debug("Parsed user choice as %s" % msg)
def parseCalc(calc):
    logging.info("User entered `%s'" % calc)
    calc = calc.replace('\u200b', '').replace('\\', '').replace('\'', '').strip().lower() #gets rid of the common stuff, without having to use core words and whatnot
    if "/" in calc or _("div") in calc:
        pass
    elif _("exit") in calc or _("quit") in calc or _("bye") in calc or _("leave") in calc:
        sys.exit()
    pass
