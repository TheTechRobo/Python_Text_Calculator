import sys, logging, turbofunc
from cprint import cprint
def GetNums():
    nums = []
    newNums = []
    n = 69
    cprint.info(_("Please enter the first number..."), end="", flush=True)
    while n != "":
        n = turbofunc.CleanInput(input())
        nums.append(n)
        if n == "":
            continue
        cprint.info(_(string_2num), end="", flush=True)
    for item in nums:
        if item != "":
            newNums.append(int(item))
    logging.debug("newNums: " % newNums)
    logging.debug("nums: " % nums)
    return newNums
def showUserWhatIThink(msg):
    cprint.ok(_("BTW, I parsed your choice as: %s") % msg)
    logging.debug("Parsed user choice as %s" % msg)
def parseCalc(calc):
    logging.info("User entered `%s'" % calc)
    calc = turbofunc.CleanInput(calc).lower()
    if "/" in calc or _("div") in calc:
        parse_division()
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
