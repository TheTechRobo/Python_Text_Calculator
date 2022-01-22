import sys, logging, turbofunc, mathmod, mathmod.fibonacci, runpy, time, random, python_radix, simpleeval
import mathmod.area
import mathmod.volume as mv
from cprint_inter import cprint
from simpleeval import simple_eval

# Data for the Beta {{{
def express_fibonacci(num):
    fib = mathmod.fibonacci.CalculateFixedFibo(num)
    return fib[len(fib) - 1]
# }}}

class Vars:
    CommandRetry = True
def GetNums():
    string_2num = _("Please enter the next number; a blank line will confirm... ")
    nums = []
    newNums = []
    n = 69
    cprint.info(_("Please enter the first number..."), end="", flush=True)
    while n != "":
        n = turbofunc.CleanInput(input())
        nums.append(n)
        if n == "":
            continue
        cprint.info(string_2num, end="", flush=True)
    for item in nums:
        if item != "":
            newNums.append(float(item))
    logging.debug("newNums: " % newNums)
    logging.debug("nums: " % nums)
    return newNums
def showUserWhatIThink(msg):
    cprint.ok(_("Parsing input as \"%s\"") % msg)
    logging.debug(f"Parsed user choice as {msg}")
def parseCalc(calc):
    logging.info("User entered `%s'" % calc)
    calc = turbofunc.CleanInput(calc).lower()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "area". Translatate only part of the word if it uses multiple charatcers and is possible without being confused, e.g. modulo turns into mod
    if _("ar") in calc or "#" in calc:
        showUserWhatIThink(_("area"))
        area_interactive()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "volume". Translate only part of the word if possible without being confusing, e.g. modulo turns into mod
    elif _("vol") in calc:
        showUserWhatIThink(_("volume"))
        volume_interactive()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "division". Translate only a core part of the word if it uses multiple characters and is possible without being confused, like for example "modulo" turns into "mod"
    elif "/" in calc or _("div") in calc or "÷" in calc:
        showUserWhatIThink(_("division"))
        parse_division()
    # FOR TRANSLATORS: This is translated if statement w the meaning of "tax". Translate only a core part of the word if possible without ambiguity, e.g. modulo turns into mod
    elif _("tax") in calc:
        showUserWhatIThink(_("tax"))
        tax()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "power" or "exponent". Translate only a core part of the word if possible without ambiguity (e.g. modulo turns into mod)
    elif _("pow") in calc or "**" in calc or "expo" in calc:
        showUserWhatIThink(_("exponent"))
        exponent()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "modulo". Translate only a core part of the word if it uses multiple characters and is possible without being confused, like for example "modulo" turns into "mod".
    elif _("mod") in calc:
        showUserWhatIThink(_("modulo"))
        parse_modulo()
    # FOR TRANSLATORS: this is a translated if statement with the meaning of "subtraction" (or, in the case of "min", "minus"). Translate only  a core part of the word if possible without ambiguity, like for example "modulo" turns into "mod".
    elif _("sub") in calc or "-" in calc or _("min") in calc:
        showUserWhatIThink(_("subtraction"))
        parse_subtraction()
    elif _("add") in calc or "+" in calc or _("plus") in calc:
        showUserWhatIThink(_("addition"))
        parse_addition()
    elif _("mult") in calc or calc == "x" or "*" in calc:
        showUserWhatIThink(_("multiplication"))
        parse_multiplication()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "root". Translate only a core paert of the word if possible without ambiguity (e.g. modulo turns into mod)
    elif _("root") in calc:
        showUserWhatIThink(_("root (general)"))
        parse_any_root()
    # FOR TRANSLATORS: This == translated if statement with the meaning of "square root" or "square". Translate onyl a core part of the word if  possible without ambiguity (e.g. modulo turns into mod)
    elif _("sq") in calc:
        showUserWhatIThink(_("square root"))
        parse_square_root()
    # FOR TRANSLATORS: This is translated if statement w meaning of "cube root" or "cube". Translate only a core part of the word if possible without ambiguity e.g. modulo turns into mod.
    elif _("cu") in calc:
        showUserWhatIThink(_("cuberoot"))
        parse_cube_root()
    # FOR TRANSLATORS: this is a translated if statement with the meaning of "factorial". Translate only a core part of the word if possible without ambuguity, like for example "modulo" turns into "mod".
    elif _("fac") in calc or "!" in calc:
        showUserWhatIThink(_("factorial"))
        parse_factorial()
    # FOR TRANSLATORS: This is a translated if statement w the meaning of "radix" or "base"  translate only a core part of the word if possible without ambiguity, e.g. "modulo" turn sinto "mod".
    elif _("rad") in calc or _("bas") in calc:
        showUserWhatIThink(_("convert bases"))
        based()
    # FOR TRANSLATORS: This is a translated if statement with the meaning of "fibonacci" - translate only a core part of the word if possible without ambiguity, like for example "modulo" turns into "mod"
    elif _("fib") in calc:
        showUserWhatIThink(_("fibonacci"))
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
        showUserWhatIThink(_("leave"))
        sys.exit()
    #FOR TRANSLATORS: This is a translated if statement. If possible, use only a core part of the word(s) here, like for example "division" turns into "div".
    elif _("help") in calc or _("?") in calc or _("confus") in calc or _("huh") in calc or _("sos") in calc or _("what") in calc:
        h()
    elif _("no") in calc:
        cprint.warn(_("Ha... ha... not... funny... whoever you are."))
        sys.exit(random.choice((42,69))) #the funny number
    elif calc == "":
        cprint.ok("Wow...you're quiet.")
        turbofunc.multiprint({"get good lo-": cprint.err, "I didn't say anything\n": cprint.warn}, end="", flush=True, no=True)
    elif "beta" in calc:
        showUserWhatIThink(_("beta **UNSUPPORTED**"))
        cprint.warn("You are entering the BETA section of Palc.\nThis may or may not work.")
        cprint.err(_("This part of Palc is untranslated because it's meant to be used by Palc maintainers only. It is discouraged to use"))
        cprint.info("You are entering the BETA Expression Evaluation Mode, or EEM.")
        cprint.ok("Safe mode enabled.")
        logging.debug("EEM")
        calc2 = input("?")
        if calc2 == "SET MODE UNSAFE":
            logging.debug("EEM UNSAFE")
            cprint.warn("Unsafe mode enabled. Be very careful what you type here!\n"
                    "DO NOT COPYPASTE HERE UNLESS YOU KNOW *EXACTLY* WHAT YOU ARE DOING")
            cprint.ok(eval(input("UNSAFE MODE - ")))
            return
        functions = {
                "Palcfib": express_fibonacci,
        }
        try: simple_eval_ = simple_eval(calc2, functions=functions)
        except simpleeval.FunctionNotDefined:
            cprint.err(_("You can't use that function here."))
            return
        standResOut(simple_eval_)
    else:
        cprint.err(_("Sorry, that is not a valid command.\n"))
        h()

def parse_factorial():
    turbofunc.multiprint({_("Please enter the"): cprint.ok, _("number"): cprint.info, _("to"): cprint.ok, _("factorial"): cprint.info, "...": cprint.ok}, end=" ", no=True)
    num = int(turbofunc.CleanInput(input()))
    fin = mathmod.factorial(num)
    standResOut(fin)
    logging.info("Got res %s, num are %s." % (fin,num))

def parse_division():
    runMathmodFunc(mathmod.division)

def parse_multiplication():
    runMathmodFunc(mathmod.multiplication)

def parse_addition():
    runMathmodFunc(mathmod.addition)

def parse_subtraction():
    runMathmodFunc(mathmod.subtraction)

def parse_modulo():
    run2NumMathmodFunc(mathmod.modulo)

def parse_square_root():
    run1NumMathmodFunc(mathmod.square_root, _("square root"))

def parse_cube_root():
    run1NumMathmodFunc(mathmod.cube_root, _("cube root"))

def parse_any_root():
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("original "): cprint.ok, _("number") + " ...": cprint.info}, end="", flush=True, no=True)
    n1 = float(turbofunc.CleanInput(input()))
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("root"): cprint.ok, _("(e.g. type 2 for square, 3 for cube, 4 for quad, etc)..."): cprint.info}, end="", flush=True, no=True)
    n2 = float(turbofunc.CleanInput(input()))
    res = mathmod.root_general(n1,n2)
    standResOut(res)
    logging.info("Got res %s, nums are %s." % (res,(n1,n2)))

def standResOut(res):
    cprint.info(_("The results are in! They indicate an answer of... "))
    turbofunc.standTextOut("\033[1m%s\033[0m" % res, printMechanismDash=cprint.info, printMechanismString=cprint.ok)

def run1NumMathmodFunc(func, action):
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("number "): cprint.ok, _("to "): cprint.info, action: cprint.ok, " ...": cprint.info}, end="", no=True, flush=True)
    n1 = float(turbofunc.CleanInput(input()))
    res = func(n1)
    standResOut(res)
    logging.info("Got res %s, num are %s." % (res,n1))
def run2NumMathmodFunc(func):
    logging.debug("Right here")
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("first"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True, no=True)
    n1 = float(turbofunc.CleanInput(input()))
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("second"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True, no=True)
    n2 = float(turbofunc.CleanInput(input()))
    res = func(n1,n2)
    standResOut(res)
    logging.info("Got res %s, nums are %s." % (res,(n1,n2)))
def runMathmodFunc(func):
    logging.debug("Right here")
    nums = GetNums()
    try:
        res = func(*nums)
    except IndexError:
        raise ValueError
    standResOut(res)
    logging.info("Got res %s, *nums are %s." % (res,nums))

def _gen_entry(name, prompts, func):
    return {
            "name": name, "prompts": prompts, "function": func
            }

def _sus(sy, baka=""):
    extra = turbofunc.clear_length(_("Please enter the ")+sy +"... "+baka)
    extraa = (extra * " ") + (extra * "\b")
    turbofunc.multiprint({
        _("Please enter the "): cprint.info, sy: cprint.ok, "... "+baka+extraa: cprint.info
        }, no=True, flush=True, end="")
    return float(turbofunc.CleanInput(input()))

def exponent():
    origin = _sus(_("original number"))
    print("\033[1A", end="")
    exp = _sus(_("exponent"))
    standResOut(mathmod.exponent(origin, exp))

def generic_interactive(datums):
    cprint.warn(_("Please report any bugs you find!"))
    cprint.info(_("Select a shape..."))
    pos = 1
    for datum in datums:
        cprint.ok(f"{pos}. {datum['name']}")
        pos += 1
    while True:
        userInput = input(_("Type the number corresponding to your shape!"))
        try:
            inp = int(turbofunc.CleanInput(userInput)) - 1
            if inp < 0:
                raise ValueError("no")
            datums[inp] # pylint: disable=pointless-statement, locally-disabled
        except (ValueError, IndexError):
            cprint.err(_("Please enter an actual option, ok??"))
        else:
            break
    cprint.info(_("Ok, proceeding with %s...") % datums[inp]['name'])
    args = []
    for prompt in datums[inp]['prompts']:
        args.append(turbofunc.CleanInput(input(prompt)))
    res = datums[inp]['function'](*args)
    standResOut(res)

def volume_interactive():
    generic_interactive(
            [
                _gen_entry(_("Cuboid (e.g. cubes, rectangular solids,...)"), [_("Please enter the length of the base of the cuboid..."), _("Please enter the width of the base of the cuboid..."), _("Please enter the height of the cuboid...")], mv.volume_cuboid),
                _gen_entry(_("Cube"), [_("Please enter the length of the base...")], mv.volume_cube),
                _gen_entry(_("Cylinder"), [_("Please enter the radius of the circular base..."), _("Please enter the height of the cylinder...")], mv.volume_cylinder),
                _gen_entry(_("Hollow cylinder"), [_("Please enter the outer radius..."), _("Please enter the height OR length of the cylinder..."), _("Please enter the thickness of the cylinder...")], mv.volume_hollow_cylinder),
                _gen_entry(_("Prism"), [_("Please enter the area of the base..."), _("Please enter the height of the prism...")], mv.volume_prism),
                _gen_entry(_("Sphere"), [_("Please enter the radius of the sphere...")], mv.volume_sphere),
                _gen_entry(_("Hollow sphere"), [_("Please enter the total radius of the sphere..."), _("Please enter the radius of the hollow space...")], mv.volume_hollow_sphere),
                _gen_entry(_("Pyramid"), [_("Please enter the area of the base..."), _("Please enter the height of the pyramid, bottom to tip...")], mv.volume_pyramid),
                _gen_entry(_("Cone"), [_("Please enter the radius of the base..."), _("Please enter the height ")], mv.volume_right_circular_cone),
                _gen_entry(_("Ellipsoid"), [_("Please enter the 1st semi axe..."), _("Please enter the 2nd semi-axe..."), _("Please enter the 3rd semi-axe...")], mv.volume_ellipsoid),
                _gen_entry(_("Tetrahedron"), [_("Please enter the length of the edge of the tetrahedron...")], mv.volume_tetrahedron) # like Tetris
            ]
    )

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
def thing():
    while True:
        print("hi")
def tax():
    cprint.ok(_("Select your Tax Type"))
    cprint.info(_("1. Sales Tax"))
    cprint.warn(_("No other types are currently supported."))
    input(_("Type: "))
    print("\033[4A", end="")
    cprint.ok(_("You picked Sales Tax."))
    cprint.ok(_("Would you like to use a tax preset?"))
    cprint.info(_("1. Yes - I live in Canada"))
    cprint.info(_("2. No"))
    cprint.warn(_("No other types are currently supported."))
    while True:
        try:
            preset = int(input(_("Type: ")))
        except (TypeError, ValueError):
            cprint.err(_("That number is a bit sus. Sure you typed it in right?")) #idk that its a dead meme
        else:
            break
    print("\033[5A]", end="") if preset != 2 else print("", end="")
    if preset == 2:
        cprint.info(_("Ok, no preset it is."))
        percentage = float(input(_("Please type the percentage of tax in your local area.")))
    elif preset == 1:
        sussypresetlist = {
                "": -1,
                _("Ontario"): mathmod.tax_types.sales.Canada.ontario,
                _("Quebec"): mathmod.tax_types.sales.Canada.quebec,
                _("Yukon/Northwest Territories/Nunavut/Alberta"): mathmod.tax_types.sales.Canada.yukon,
                _("British Columbia/Manitoba"): mathmod.tax_types.sales.Canada.manitoba,
                _("New Brunswick/Nova Scotia/Newfoundland/Prince Edward Island"): mathmod.tax_types.sales.Canada.newfoundland,
                _("Saskatchewan"): mathmod.tax_types.sales.Canada.saskatchewan,
        }
        sus = list(sussypresetlist)
        ind = 0
        for su in sus: #s
            if ind == 0:
                ind += 1
                continue
            cprint.info(f"{ind}. {su}")
            ind += 1
        while True:
            try:
                presetterInd = int(input(_("Please enter the One You Want™")))
            except (ValueError, TypeError):
                cprint.err(_("Nice try, but you have to actually type a number."))
            else:
                try:
                    percentage = sussypresetlist[sus[presetterInd]]
                    if percentage is None:
                        raise IndexError
                except IndexError:
                    cprint.err(_("Nice try, but the number has to be in range."))
                    continue
                break
        origin = float(input(_("What is the original number?")))
        standResOut(mathmod.tax(origin, percentage))

def based():
    cprint.info(_("Please enter the original base."))
    cprint.ok(_("ProTip: 2 is binary, 8 is octal, 10 is decimal, 16 is hex, and 36 has all the letters in the alphabet."))
    cprint.warn(_("Don't type anything above %d. Additionally, typing anything below 2 will cause the conversion to either hang or fail.") % python_radix.python_radix.max_base)
    originalBase = int(turbofunc.CleanInput(input(_("Type: ")))) # that's a lotta brackets. HOW BOUT A LITTLE MORE
    print("\033[4A", end="")
    cprint.info(_("Please enter the destination base."))
    destinationBase = int(turbofunc.CleanInput(input("\n\n" + _("Type: "+"  \b\b"))))
    exp = lambda thingy : not (thingy > python_radix.python_radix.max_base or thingy < 2)
    if exp(originalBase) is False or exp(destinationBase) is False:
        return cprint.fatal(_("I told you not to do that."))
    logging.debug(f"loading converter for base {originalBase} => {destinationBase}")
    conv = python_radix.Converter(originalBase, destinationBase)
    print("\033[4A", end="") #https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
    cprint.info(_("Please enter the original number (it should not have a decimal point)."))
    number = turbofunc.CleanInput(input("\n\n" + _("Type: "+"  \b\b")))
    try:
        result = conv.convert(number)
    except Exception as ename:
        cprint.err(_("Failed to convert numbers. Remember to only put the digits in that base in! (%s)") % ename)
        return
    standResOut(result)

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
