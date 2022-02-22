import sys, logging, turbofunc, mathmod, mathmod.fibonacci, mathmod.area
import runpy, time, random, python_radix, simpleeval, os,json, os.path, appdirs
import mathmod.volume as mv
from cprint_inter import cprint
from simpleeval import simple_eval

name = "Palc"
author = "TheTechRobo"

class Calculation:
    def __init__(self, function, core_words, what_i_think):
        self.function, self.core_words, self.what_i_think = \
                function, core_words, what_i_think
    def run(self):
        logging.debug(f"Parsing user input as `{self.what_i_think}'")
        cprint.ok(_("Parsing input as \"%s\"") % self.what_i_think)
        return self.function

CALCULATIONS = []

# Data for the Beta {{{
def express_fibonacci(num):
    fib = mathmod.fibonacci.CalculateFixedFibo(num)
    return fib[len(fib) - 1] #returns last item from the fibonacci list
# }}}

class Vars:
    CommandRetry = True
def GetNums(msg=None, msg2=None, post=float):
    if not msg:
        msg = _("Please enter the first number...")
    if not msg2:
        msg2 = _("Please enter the next number; a blank line will confirm...")
    nums = []
    newNums = []
    n = 69
    cprint.info(msg, end="", flush=True)
    while n != "":
        n = turbofunc.CleanInput(input())
        nums.append(n)
        if n == "":
            continue
        cprint.info(msg2, end=" ", flush=True)
    for item in nums:
        if item != "":
            newNums.append(post(item))
    logging.debug(f"newNums: {newNums}")
    logging.debug(f"nums: {nums}")
    return newNums
def parseCalc(calc):
    sudo()
    logging.info("User entered `%s'" % calc)
    calc = turbofunc.CleanInput(calc).lower()
    if calc == "":
        cprint.ok("Wow...you're quiet.")
        turbofunc.multiprint({"get good lo-": cprint.err, "I didn't say anything\n": cprint.warn}, end="", flush=True, no=True)
    else:
        parse_ceta(calc)

def parse_beta():
    cprint.warn("You are entering the BETA section of Palc. This may or may not work.")
    cprint.err(_("This part of Palc is untranslated because it's meant to be used by Palc maintainers only. It is discouraged to use"))
    cprint.info("You are entering the BETA Expression Evaluation Mode, or EEM.")
    cprint.ok("Safe mode enabled.")
    logging.debug("EEM")
    calc2 = input("?")
    if calc2 == "SET MODE UNSAFE":
        logging.warn("SET MODE UNSAFE has been run. Be very careful!")
        cprint.warn("Unsafe mode enabled. Be very careful what you type here!")
        cprint.err("DO NOT COPYPASTE HERE UNLESS YOU KNOW *EXACTLY* WHAT YOU ARE DOING")
        cprint.ok(eval(input("UNSAFE MODE - ")))
        return
    functions = {
            "Palcfib": express_fibonacci,
    }
    try:
        simple_eval_ = simple_eval(calc2, functions=functions)
    except simpleeval.FunctionNotDefined:
        cprint.err(_("You can't use that function here."))
        return
    standResOut(simple_eval_)

def clist():
    cprint.info(_("OK, here the list of commands!"))
    for calc in CALCULATIONS:
        cprint.ok(f"\t{calc.core_words}: {calc.what_i_think}", no=True)

def choose_percent_sign():
    cprint.info(_("1. Percentage.\n2. Modulo"))
    choice = _sus(_("mode you pick"), func=int)
    if choice == 1:
        percentage()
    elif choice == 2:
        parse_modulo()
    else:
        cprint.err(_("Invalid."))
def percentage():
    cprint.info(_("What would you like to do?"))
    cprint.info(_("\t1. Find X percent of Y."), no=True)
    cprint.info(_("\t2. Find what percentage X out of Y is."), no=True)
    choice = _sus(_("choice"), func=int)
    if choice == 1:
        x_percent_of_why()
    elif choice == 2:
        x_of_y()

def x_percent_of_why():
    part = _sus(_("percentage"))
    whole = _sus(_("whole"))
    standResOut(mathmod.percent_of(part, whole), text="percent_of", origin=f"part={part}, whole={whole}")

def x_of_y():
    part = _sus(_("part"))
    whole = _sus(_("total"))
    standResOut(mathmod.find_percentage(part, whole), text="find_percentage", origin=f"part={part}, whole={whole}")

def parse_fibonacci():
    cprint.info(_("Welcome to the fibonacci calculator."))
    cprint.ok("\t" + _("1 - Looped fibonacci (infinite)") + "\n" \
            + "\t" + _("2 - Calculate a certain number of fibonacci numbers."))
    choice = int(turbofunc.CleanInput(input(_("Select one: "))))
    if choice == 1:
        try:
            mathmod.fibonacci.CalculateLoopedFibo()
        except KeyboardInterrupt:
            print()
    elif choice == 2:
        num = int(turbofunc.CleanInput(input(_("Enter the number of fibonacci to calculate...")))) #NOW THATS A LOTTA PARENTHESIS!!!
        cprint.info(_("The results are in! They indicate an answer of..."))
        standResOut(str(mathmod.fibonacci.CalculateFixedFibo(num)), text="fibonacci", origin=num)

def parse_factorial():
    turbofunc.multiprint({_("Please enter the"): cprint.ok, _("number"): cprint.info, _("to"): cprint.ok, _("factorial"): cprint.info, "...": cprint.ok}, end=" ", no=True)
    num = int(turbofunc.CleanInput(input()))
    fin = mathmod.factorial(num)
    standResOut(fin, text = "factorial", origin=num)

def logarithm():
    cprint.info(_("Select the desired mode of logarithm. Options: "))
    count = 0
    modes = []
    for mode in mathmod.LogarithmModes:
        modes.append(mode)
        count += 1
        cprint.ok("%d.  %s" % (count, mode.value))
    ind = int(_sus(_("mode to process"))) - 1
    if (len(mathmod.LogarithmModes) - 1) < ind or ind < 0:
        return cprint.err(_("Nice try, but you need to type in a number that's in range"))
    num = _sus(_("original number"))
    standResOut(mathmod.log(num, modes[ind]), text=f"logarithm_{mode}", origin=num)

def calc_ord():
    char = _sus("character to ord", func=str)
    if len(char) > 1:
        raise ValueError("we need a CHARACTER, not a STRING of characters")
    standResOut(ord(char), text="ord", origin=char)

def calc_chr():
    code = _sus("number to chr", func=int)
    char = ord(code)
    standResOut(char, text="chr", origin=code)

def interest():
    orogin = _sus("original number")
    rate = _sus("interest rate")
    units = _sus("number of units of time")
    standResOut(mathmod.interest(units, rate, orogin), text="interest", origin=orogin)

def spinner():
    mydata = GetNums(_("Please enter the first item..."), _("Please enter the next item; a blank line will confirm..."), post=str)
    times = _sus(_("amount of times you want to spin"), func=int)
    standResOut(mathmod.spinner(mydata, times), text="spin", origin=f"number_of_times={times}, choices={mydata}")


def write_slot(slot, number, filename="slots.json"):
    appdir = appdirs.user_data_dir(name, author)
    path = os.path.join(appdir, filename)
    if not os.path.exists(path):
        if not os.path.exists(appdir):
            os.mkdir(appdir)
        with open(path, "w+") as file:
            file.write("{}")
    with open(path) as j:
        slojson = json.load(j)
    slot_exists = not (slojson.get(slot) is None)
    if slot_exists:
        cprint.warn(_("The slot %s already exists. Do you want to overwrite it?") % slot)
        overwrite = turbofunc.CleanInput(input(_("Type: ")))[0].lower() == "y"
        if overwrite:
            logging.info(f"Overwriting memory slot {slot}")
            cprint.warn(_("Ok, overwriting..."))
        else:
            return cprint.fatal(_("Abort."))
    slojson[slot] = number
    with open(path, "w") as fil:
        fil.write(json.dumps(slojson))
    standResOut(_("Finished."), text="write_slot", origin=slot)

def tax():
    cprint.ok(_("Select your Tax Type"))
    cprint.info(_("1. Sales Tax"))
    cprint.warn(_("No other types are currently supported."))
    input(_("Type: "))
    print("\033[4A", end="")
    cprint.ok(_("You picked Sales Tax."))
    cprint.ok(_("Would you like to use a tax preset?"))
    cprint.info(_("1. Yes - I live in Canada"))
    cprint.info(_("2. Yes - use a Memory Slot"))
    cprint.info(_("3. No"))
    cprint.warn(_("No other types are currently supported."))
    while True:
        try:
            preset = int(input(_("Type: ")))
        except (TypeError, ValueError):
            cprint.err(_("That number is a bit sus. Sure you typed it in right?")) #idc that its a dead meme
        else:
            break
    if preset != 3:
        print("\033[5A", end="")
    else:
        print("", end="")
    if preset == 3:
        cprint.info(_("Ok, no preset it is."))
        percentage = float(input(_("Please type the percentage of tax in your local area: ")))
    elif preset == 2:
        percentage = tax_slots()
        if percentage is None:
            cprint.fatal(_("Could not load Memory-Slot for some reason."))
            return False
    elif preset == 1:
        sussypresetlist = {
                _("Ontario"): mathmod.tax_types.sales.Canada.ontario,
                _("Quebec"): mathmod.tax_types.sales.Canada.quebec,
                _("Yukon/Northwest Territories/Nunavut/Alberta"): mathmod.tax_types.sales.Canada.yukon,
                _("British Columbia/Manitoba"): mathmod.tax_types.sales.Canada.manitoba,
                _("New Brunswick/Nova Scotia/Newfoundland/Prince Edward Island"): mathmod.tax_types.sales.Canada.newfoundland,
                _("Saskatchewan"): mathmod.tax_types.sales.Canada.saskatchewan,
        }
        sus = list(sussypresetlist)
        for ind, su in enumerate(sussypresetlist):
            cprint.info(f"{ind + 1}. {su}")
        while True:
            try:
                presetterInd = int(input(_("Please enter the One You Want™: "))) - 1
                if presetterInd < 0:
                    presetterInd = 32237
            except (ValueError, TypeError):
                cprint.err(_("Nice try, but you have to actually type a number."))
            else:
                try:
                    name = sus[presetterInd]
                    percentage = sussypresetlist[sus[presetterInd]]
                    if percentage is None:
                        raise IndexError
                except IndexError:
                    cprint.err(_("Nice try, but the number has to be in range."))
                    continue
                break
    origin = _sus("original number")
    standResOut(mathmod.tax(origin, percentage), text="tax", origin=f"origin={origin}, percentage={percentage}")



def tax_slots():
    cprint.info(_("M E M O R Y"))
    try:
        with open(os.path.join(appdirs.user_data_dir(name, author), "slots.json")) as f:
            j = json.load(f)
    except IOError:
        j = {}
    for title, current_slot in j.items():
        cprint.info(f"{title}: {current_slot}")
    else:
        cprint.err(_("No memory slots currently exist."))
    cprint.warn(_("To create a new slot, use the MEMORY command."))
    try:
        slot = turbofunc.CleanInput(input(_("Please enter a slot.")))
    except KeyboardInterrupt:
        cprint.err(_("Abort."))
        return None
    try:
        return float(j[slot])
    except KeyError:
        cprint.err(_("This slot does not exist."))
        return None

def mémoire():
    cprint.info(_("M E M O R Y"))
    slot = turbofunc.CleanInput(input(_("What is your memory slot of choice?")))
    cprint.ok(_("Read or Write?\n1 - Read\n2 - Write"))
    a = turbofunc.CleanInput(input(_("Type: ")))
    if int(a) == 1:
        try:
            with open(os.path.join(appdirs.user_data_dir(name, author), "slots.json")) as f:
                j = json.load(f)
            standResOut(j[slot], text="read_slot", origin=slot)
        except (KeyError, IOError):
            if os.path.isfile(str(slot)):
                cprint.warn(_("We have found a 0.7-style memory slot with this name. 0.7 memory slots were very crude. We won't read the slot for you unless you move it."))
                cprint.ok(_("Would you like to migrate the memory slot to 0.11 mode?"), end="")
                yn = True if turbofunc.CleanInput(input())[0].lower() == 'y' else False
                if yn:
                    cprint.info(_("Migrating memory slot..."))
                    with open(str(slot)) as data:
                        number = data.read()
                    write_slot(slot, number)
                    cprint.warn(_("Palc will now ignore the file; but if you want to delete it you'll have to do so yourself"))
                    return
                cprint.err(_("Abort."))
                cprint.fatal(_("We can't read the memory slot until you migrate it."))
                return
            cprint.fatal(_("Slot does not exist!"))
    elif int(a) == 2:
        write_slot(slot, turbofunc.CleanInput(input("Number? ")))
    else:
        cprint.ok(_("No"))
        raise SyntaxError("just no")

def parse_division():
    runMathmodFunc(mathmod.division)

def parse_multiplication():
    runMathmodFunc(mathmod.multiplication)

def parse_addition():
    runMathmodFunc(mathmod.addition)

def parse_subtraction():
    runMathmodFunc(mathmod.subtraction)

def parse_modulo():
    run2NumMathmodFunc(mathmod.modulo, ("n1", "n2"))

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
    standResOut(res, text="root", origin=f"origin={n1}, root={n2}")

def standResOut(res, text="?", origin="?"):
    logging.info(f"{text}({origin}): {res}")
    cprint.info(_("The results are in! They indicate an answer of... "))
    turbofunc.standTextOut("\033[1m%s\033[0m" % res, printMechanismDash=cprint.info, printMechanismString=cprint.ok)

def run1NumMathmodFunc(func, action):
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("number "): cprint.ok, _("to "): cprint.info, action: cprint.ok, " ...": cprint.info}, end="", no=True, flush=True)
    n1 = float(turbofunc.CleanInput(input()))
    res = func(n1)
    standResOut(res, text=func.__name__, origin=n1)
def run2NumMathmodFunc(func, signature):
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("first"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True, no=True)
    n1 = float(turbofunc.CleanInput(input()))
    turbofunc.multiprint({_("Please enter the "): cprint.info, _("second"): cprint.ok, _(" number") + " ...": cprint.info}, end="", flush=True, no=True)
    n2 = float(turbofunc.CleanInput(input()))
    res = func(n1,n2)
    standResOut(res, text=func.__name__, origin=f"{signature[0]}={n1}, {signature[1]}={n2}")
def runMathmodFunc(func):
    nums = GetNums()
    try:
        res = func(*nums)
    except IndexError:
        raise ValueError
    standResOut(res, text=func.__name__, origin=str(nums).lstrip("[").rstrip("]"))

def _gen_entry(name, prompts, func):
    return {
            "name": name, "prompts": prompts, "function": func
            }

def __sus(sy, baka=""):
    extra = turbofunc.clear_length(_("Please enter the ")+sy +"... "+baka)
    extraa = (extra * " ") + (extra * "\b")
    turbofunc.multiprint({
        _("Please enter the "): cprint.info, sy: cprint.ok, "... "+baka+extraa: cprint.info
        }, no=True, flush=True, end="")
    return turbofunc.CleanInput(input())

def _sus(*args, **kwargs):
    if not (func := kwargs.get("func")):
        func = float
    else:
        del kwargs["func"]
    return func(__sus(*args, **kwargs))

def exponent():
    origin = _sus(_("original number"))
    print("\033[1A", end="")
    exp = _sus(_("exponent"))
    standResOut(mathmod.exponent(origin, exp), text="exponent", origin=f"origin={origin}, exponent={exponent}")

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
    function = datums[inp]["function"]
    res = function(args)
    standResOut(res, text=function.__name__, origin=str(args).lstrip("[").rstrip("]"))

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
    standResOut(result, text="base", origin=f"origin={number}, base={destinationBase}") #after base

def h():
    cprint.ok(_("There are a bunch of commands you can use. Find them by typing in `list'."))
    cprint.warn(_("Expressions (such as: 1 + 3 / (2 * 6.4)) DO NOT WORK as of now."))
    cprint.info(_("\033[1mPlease enjoy Palc!\033[0m \033[94mFeedback or bug reports? Go to \033[4mgithub.com/thetechrobo/python-text-calculator/issues\033[0m\033[94m!\033[0m"))#https://stackoverflow.com/a/17303428/9654083

def add_calculations(*args):
    for i in args:
        CALCULATIONS.append(i)

def funny():
    cprint.warn(_("Ha... ha... not... funny... Jim."))
    sys.exit(random.choice((42,69)))

def sudo():
    add_calculations(
        Calculation(h, ("?", _("help"), _("idk"), _("confus"), _("sos"), _("what")),
            _("help")),
        Calculation(sys.exit, (_("exit"), _("quit"), _("bye"), _("leave")),
            _("exit Palc")),
        # FOR TRANSLATORS: This is a translated if statement with the meaning of "fibonacci"
        Calculation(parse_fibonacci, (_("fib"),),
            _("fibonacci")),
        # FOR TRANSLATORS: This is a translated if statement with the meaning of "factorial"
        Calculation(parse_factorial, ("!", _("fac")),
            _("factorial")),
        # FOR TRANSLATORS: Translated if statement (meaning of division)
        Calculation(parse_division, ("/", _("div"), "÷"),
            _("division")),
        Calculation(parse_multiplication, (_("mult"), "*"),
            _("multiplication")),
        Calculation(parse_addition, (_("add"), "+", _("plus")),
            _("addition")),
        Calculation(parse_subtraction, (_("sub"), "-", _("min")),
            _("subtraction")),
        Calculation(parse_modulo, (_("mod"),),
            _("modulo")),
        Calculation(parse_square_root, (_("sq"),),
            _("square root")),
        Calculation(parse_cube_root, (_("cu"),),
            _("cuberoot")),
        Calculation(parse_any_root, (_("root"),),
            _("root")),
        Calculation(exponent, (_("pow"), "**", _("expo")),
            _("exponent")),
        Calculation(volume_interactive, (_("vol"),),
            _("volume")),
        Calculation(area_interactive, (_("ar"),"#"),
            _("area")),
        Calculation(tax, (_("tax"),),
            _("tax")),
        Calculation(based, (_("rad"), _("base")),
            _("convert bases")),
        Calculation(funny, (_("no"),),
            _("be the most unfunny person ever")),
        Calculation(parse_beta, ("beta",),
            _("use the beta (UNSUPPORTED")),
        Calculation(mémoire, (_("mem"), _("save"), _("var"), _("load")),
            _("load or save a memory slot")),
        Calculation(logarithm, (_("loga"),),
            _("calculate logarithm")),
        Calculation(calc_ord, (_("ord"),),
            _("calculate the ASCII code of a character")),
        Calculation(calc_chr, (_("chr"),),
            _("calculate the character of an ASCII code")),
        Calculation(interest, (_("interest"), _("rate")),
            _("calculate interest rate")),
        Calculation(spinner, (_("spin"), _("random"), _("pick")),
            _("use the spinner")),
        Calculation(choose_percent_sign, ("%",), _("pick percentage sign")),
        Calculation(percentage, (_("perc"),),
            _("pick percentage mode")),
        Calculation(clist, (_("list"), _("commands")),
            _("list available calculations")),
        )

def parse_ceta(calcc):
    for calc in CALCULATIONS:
        for word in calc.core_words:
            if word in calcc:
                return calc.run()() #im literally only doing this bc it looks stupid
    cprint.err(_("Sorry, but I didn't quite get that."))
    h()

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
