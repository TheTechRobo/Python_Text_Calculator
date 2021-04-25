import sys, logging, turbofunc, mathmod
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
            newNums.append(float(item))
    logging.debug("newNums: " % newNums)
    logging.debug("nums: " % nums)
    return newNums
def showUserWhatIThink(msg):
    cprint.ok(_("BTW, I parsed your choice as: %s") % msg)
    logging.debug("Parsed user choice as %s" % msg)
def parseCalc(calc):
    logging.info("User entered `%s'" % calc)
    calc = turbofunc.CleanInput(calc).lower()
    if "/" in calc or _("div") in calc or "÷" in calc:
        parse_division()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "modulo". Translate only a core part of the word if it uses multiple characters and is possible without being confused, like for example "modulo" turns into "mod".
    elif _("mod") in calc:
        parse_modulo()
    elif _("sub") in calc or "-" in calc or _("min") in calc:
        parse_subtraction()
    elif _("add") in calc or "+" in calc:
        parse_addition()
    elif _("mult") in calc or calc == "x" or "*" in calc:
        parse_multiplication()
    elif _("exit") in calc or _("quit") in calc or _("bye") in calc or _("leave") in calc:
        showUserWhatIThink("exit")
        sys.exit()
    #FOR TRANSLATORS: This is a translated if statement. If possible, use only a core part of the word(s) here, like for example "division" turns into "div".
    elif _("help") in calc or _("?") in calc:
        cprint.info(helpText)
    elif _("no u") in calc:
        cprint.warn(_("Ha... ha... not... funny... whoever you are."))
        sys.exit(69)
    elif calc == "":
        cprint.ok("Wow...you're quiet.")
        turbofunc.multiprint({"get good lo-": cprint.err, "I didn't say anything\n": cprint.warn}, end="", flush=True)
    else:
        cprint.err("UNKNOWN COMMAND - %s" % helpText.split('\n')[0]) #https://stackoverflow.com/a/11833277/9654083
        cprint.ok("I'll help!")
        cprint.info(helpText.split('\n')[2])
        cprint.ok(helpText.split('\n')[3])

def parse_division():
    runMathmodFunc(mathmod.division)

def parse_multiplication():
    runMathmodFunc(mathmod.multiplication)

def parse_addition():
    runMathmodFunc(mathmod.addition)

def parse_subtraction():
    runMathmodFunc(mathmod.subtraction)

def parse_modulo():
    logging.debug("Right here")
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("first"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True)
    n1 = float(input())
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("first"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True)
    n2 = float(input())
    res = mathmod.modulo(n1,n2)
    cprint.info(_("The results are in! They indicate an answer of: "))
    cprint.ok("\033[1m%s\033[0m" % res)
    logging.info("Got res %s, nums are %s." % (res,(n1,n2)))

def runMathmodFunc(func):
    logging.debug("Right here")
    nums = GetNums()
    res = func(*nums)
    cprint.info(_("The results are in! They indicate an answer of..."))
    cprint.ok("\033[1m%s\033[0m" % res)
    logging.info("Got res %s, *nums are %s." % (res,nums))

string_2num = "Please enter the next number, or enter a blank line to confirm your choices... "
helpText = """Using Palc but don't know what to do??
I'll help!
There are a bunch of commands you can use. These are: addition, subtraction, multiplication, division, modulo.
Expressions (example: 1 + 3 / (2 * 6.4)) DO NOT WORK as of now.
\033[1mPlease enjoy Palc!\033[0m \033[94mFeedback or bug reports? Go to \033[4mgithub.com/thetechrobo/python-text-calculator/issues\033[0m\033[94m!\033[0m
"""#https://stackoverflow.com/a/17303428/9654083
