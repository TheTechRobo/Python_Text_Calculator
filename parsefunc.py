import sys, logging, turbofunc, mathmod, mathmod.fibonacci, runpy, time, random
from cprint import cprint
MANYSPACE = "                    "

# Data for the Beta {{{
def express_fibonacci(num):
    fib = mathmod.fibonacci.CalculateFixedFibo(num)
    return fib[len(fib) - 1]
# }}}

class Vars:
    CommandRetry = True
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
    # FOR TRANSLATORS: this is a translated if statement with the meaning of "subtraction" (or, in the case of "min", "minus"). Translate only  a core part of the word if possible without ambiguity, like for example "modulo" turns into "mod".
    elif _("sub") in calc or "-" in calc or _("min") in calc:
        parse_subtraction()
    elif _("add") in calc or "+" in calc or _("plus") in calc:
        parse_addition()
    elif _("mult") in calc or calc == "x" or "*" in calc:
        parse_multiplication()
    elif _("fib") in calc:
        choice = input(_("Welcome to the fibonacci calculator.\n\t1 - Looped fibonacci (infinite)\n\t2 - Calculate a certain number of fibonacci numbers.\nSelect one: "))
        if int(turbofunc.CleanInput(choice)) == 1:
            try:
                mathmod.fibonacci.CalculateLoopedFibo()
            except KeyboardInterrupt:
                print()
        elif int(turbofunc.CleanInput(choice)) == 2:
            num = int(turbofunc.CleanInput(input(_("Enter the number of fibonacci to calculate...")))) #NOW THATS A LOTTA PARENTHESIS!!!
            cprint.info(_("The results are in! They indicate an answer of..."))
            turbofunc.standTextOut(str(mathmod.fibonacci.CalculateFixedFibo(num)))
    elif _("exit") in calc or _("quit") in calc or _("bye") in calc or _("leave") in calc:
        showUserWhatIThink("exit")
        sys.exit()
    #FOR TRANSLATORS: This is a translated if statement. If possible, use only a core part of the word(s) here, like for example "division" turns into "div".
    elif _("help") in calc or _("?") in calc or _("confus") in calc or _("huh") in calc or _("sos") in calc or _("what") in calc:
        h()
    elif _("no") in calc:
        cprint.warn(_("Ha... ha... not... funny... whoever you are."))
        sys.exit(random.choice((42,69))) #the funny number
    elif calc == "":
        cprint.ok("Wow...you're quiet.")
        turbofunc.multiprint({"get good lo-": cprint.err, "I didn't say anything\n": cprint.warn}, end="", flush=True)
    elif "beta" in calc:
        cprint.warn("You are entering the BETA section of Palc.\nThis may or may not work.")
        cprint.err(_("This part of Palc is untranslated because it's meant to be used by Palc maintainers only. It is discouraged to use"))
        cprint.info("You are entering the BETA Expression Evaluation Mode, or EEM.")
        cprint.ok("Safe mode enabled.")
        from simpleeval import simple_eval
        calc2 = input("?")
        if calc2 == "SET MODE UNSAFE":
            cprint.warn("Unsafe mode enabled. Be very careful what you type here!")
            cprint.ok(eval(input("UNSAFE MODE - ")))
            return
        cprint.ok(simple_eval(calc2, functions={
            "Palcfib": express_fibonacci,
        }))
    else:
        #TODO: add a list of all calcs and change this to elif calc not in ("blah", "yak", "ok")
          # then change "else" to raise a ValueError "This calculation exists, but is not implemented. Contact the developer."
        cprint.err(_("Sorry, that is not a valid command.\n"))
        h()

def parse_division():
    try:
        runMathmodFunc(mathmod.division)
    except ZeroDivisionError:
        turbofunc.standTextOut("Oops!")
        # FOR TRANSLATORS: **PLEASE** keep the \033[1m and \033[0m and \n
        cprint.err(_("I see you divided by 0. \033[1mPlease don't do that\033[0m"), end="")
        # FOR TRANSLATORS: This is not a typo. It is a continuation of "Please don't do that".
        cprint.err(_(", as it doesn't work."))
        cprint.info(_("Think of it as Siri does. Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends."))
        cprint.ok(_("Boom. Roasted."))

def parse_multiplication():
    runMathmodFunc(mathmod.multiplication)

def parse_addition():
    runMathmodFunc(mathmod.addition)

def parse_subtraction():
    runMathmodFunc(mathmod.subtraction)

def parse_modulo():
    run2NumMathmodFunc(mathmod.modulo)

def run2NumMathmodFunc(func):
    logging.debug("Right here")
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("first"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True)
    n1 = float(turbofunc.CleanInput(input()))
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("second"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True)
    n2 = float(turbofunc.CleanInput(input()))
    res = func(n1,n2)
    cprint.info(_("The results are in! They indicate an answer of... "))
    turbofunc.standTextOut("\033[1m%s\033[0m" % res, printMechanismDash=cprint.info, printMechanismString=cprint.ok)
    logging.info("Got res %s, nums are %s." % (res,(n1,n2)))
def runMathmodFunc(func):
    logging.debug("Right here")
    nums = GetNums()
    try:
        res = func(*nums)
    except IndexError:
        raise ValueError
    cprint.ok(_("The results are in! They indicate an answer of..."))
    turbofunc.standTextOut("\033[1m%s\033[0m" % res, printMechanismDash=cprint.info, printMechanismString=cprint.ok)
    logging.info("Got res %s, *nums are %s." % (res,nums))

string_2num = "Please enter the next number; a blank line will confirm... "
def h():
    cprint.ok(_("There are a bunch of commands you can use. These are: addition, subtraction, multiplication, division, modulo, and fibonacci."))
    cprint.warn(_("Expressions (such as: 1 + 3 / (2 * 6.4)) DO NOT WORK as of now."))
    cprint.info(_("\033[1mPlease enjoy Palc!\033[0m \033[94mFeedback or bug reports? Go to \033[4mgithub.com/thetechrobo/python-text-calculator/issues\033[0m\033[94m!\033[0m"))#https://stackoverflow.com/a/17303428/9654083
if __name__ == "__main__":
    cprint.warn("Do not run parsefunc on its own. Attempting to run Palc...")
    time.sleep(3)
    try:
        runpy.run_path("palc.py")
    except Exception as ename:
        cprint.err("Failed. Raising backtrace...")
        raise
else:
    del runpy
