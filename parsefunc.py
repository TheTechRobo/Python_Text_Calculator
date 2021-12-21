import sys, logging, turbofunc, mathmod, mathmod.fibonacci, runpy, time, random
import mathmod.area
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
    if "test" in calc:
        area_interactive()
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
    # FOR TRANSLATORS: this is a translated if statement with the meaning of "factorial". Translate only a core part of the word if possible without ambuguity, like for example "modulo" turns into "mod".
    elif _("fac") in calc or "!" in calc:
        parse_factorial()
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
        logging.debug("EEM")
        from simpleeval import simple_eval
        calc2 = input("?")
        if calc2 == "SET MODE UNSAFE":
            logging.debug("EEM UNSAFE")
            cprint.warn("Unsafe mode enabled. Be very careful what you type here!")
            cprint.ok(eval(input("UNSAFE MODE - ")))
            return
        cprint.ok(simple_eval(calc2, functions={
            "Palcfib": express_fibonacci,
        }))
    else:
        cprint.err(_("Sorry, that is not a valid command.\n"))
        h()

def parse_factorial():
    turbofunc.multiprint({_("Please enter the"): cprint.ok, _("number"): cprint.info, _("to"): cprint.ok, _("factorial"): cprint.info, "...": cprint.ok}, end=" ")
    num = int(turbofunc.CleanInput(input()))
    fin = mathmod.factorial(num)
    cprint.ok(_("The results are in! They indicate an answer of..."))
    turbofunc.standTextOut("\033[1m%s\033[0m" % fin, printMechanismDash=cprint.info, printMechanismString=cprint.ok)
    logging.info("Got res %s, num are %s." % (fin,num))

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

def _gen_entry(name, prompts, func):
    return {
            "name": name, "prompts": prompts, "function": func
            }

def generic_interactive(datums):
    cprint.info("Select a shape...")
    pos = 1
    for datum in datums:
        print(f"{pos}. {datum['name']}")
    exit(1)

def area_interactive():
    calculation_list = [
            _gen_entry(_("Triangle"), [_("Please enter the length of the base of the triangle..."), _("Please enter the height of the base of the triangle...")], mathmod.area.area_triangle),
            _gen_entry(_("Square"), [_("Please enter the length of the square...")], mathmod.area.area_square),
            _gen_entry(_("Rectangle"), [_("Please enter the width of the rectangle..."), _("Please enter the height of the rectangle...")], mathmod.area.area_rectangle),
            _gen_entry(_("Parallelogram"), [_("Please enter the length of the base of the parallelogram..."), _("Please enter the height of the parallelogram...")], mathmod.area.area_parallelogram),
            _gen_entry(_("Trapezium / Trapezoid"), [_("Please enter the height of the shape..."), _("Please enter the length of the first base of the shape..."), _("Please enter the length of the second base of the shape...")], mathmod.area.area_trapezium),
            _gen_entry(_("Circle"), [_("Please enter the radius of the circle...")], mathmod.area.area_circle),
            _gen_entry(_("Semicircle"), [_("Please enter the radius of the semicircle...")], mathmod.area.area_semicircle),
            _gen_entry(_("Ellipse"), [_("Please enter the length of the semi-major axis..."), _("Please enter the length of the semi-minor axis...")], mathmod.area.area_ellipse),
            _gen_entry(_("Sector"), [_("Please enter the angle of the sector, in radians..."), _("Please enter the radius of the sector...")], mathmod.area.area_sector),
            _gen_entry(_("Rhombus"), [_("Please enter the length of any side of the rhombus..."), _("Please enter the height of the rhombus...")], mathmod.area.area_rhombus),
            _gen_entry(_("Ring"), [_("Please enter the radius of the inner circle..."), _("Please enter the radius of the outer circle...")], mathmod.area.area_ring),
            ]
    generic_interactive(calculation_list)

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
