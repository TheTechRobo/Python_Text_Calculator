import sys, logging, turbofunc
from cprint import cprint
def CleanInput(inp):
    return inp.replace('\u200b', '').replace('\\', '').replace('\'', '').strip().lower()
def GetNums():
    list = []
    n = 69
    while n != "":
        n = int(input().strip())
        list.append(n)
        cprint.info(_(string_2num), end="", flush=True)
def showUserWhatIThink(msg):
    cprint.ok(_("BTW, I parsed your choice as:\n%s") % msg)
    logging.debug("Parsed user choice as %s" % msg)
def parseCalc(calc):
    logging.info("User entered `%s'" % calc)
    calc = calc.replace('\u200b', '').replace('\\', '').replace('\'', '').strip().lower() #gets rid of the common stuff, without having to use core words and whatnot
    if "/" in calc or _("div") in calc:
        pass
    elif _("exit") in calc or _("quit") in calc or _("bye") in calc or _("leave") in calc:
        showUserWhatIThink("exit")
        sys.exit()
    elif _("help") in calc:
        cprint.info(helpText)
    else:
        cprint.err("UNKNOWN COMMAND - %s" % helpText.split('\n')[0]) #https://stackoverflow.com/a/11833277/9654083
        cprint.ok("I'll help!")
        cprint.info(helpText.split('\n')[2])
        cprint.ok(helpText.split('\n')[3])

def parse_division():
    logging.debug("Right here")
    nums = GetNums()

string_2num = "Please enter the next number, or enter a blank line to confirm your choices... "
helpText = """Using Palc but don't know what to do??
I'll help!
There are a bunch of commands you can use. These are:
\033[1mPlease enjoy Palc!\033[0m \033[94mFeedback or bug reports? Go to \033[4mgithub.com/thetechrobo/python-text-calculator/issues\033[0m\033[94m!\033[0m
"""#https://stackoverflow.com/a/17303428/9654083
