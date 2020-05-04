#SETUP
import logging
logging.basicConfig(filename="palc.log", level=logging.DEBUG)
from sys import exit
import time
try:
    from root import *
except:
    logging.error("Could not access file root.py")
    print("I can't find file root.py, and thus you cannot calculate roots.")
try:
    from func import *
except:
    logging.critical("Could not access file func.py")
    exit("I can't access the file func.py. This file is necessary for proper function of the Software.")
print("Loading...............\n")
time.sleep(2)
def palc():
    while True:
       for i in range (0, 13): #13 blank lines
            print()
#CALCULATION CHOICE
       calc = input("What calculation do you wish to do? (Type `?' for a list of commands)\nType: ")
       calc = calc.lower() #make variable "calc" lowercase
#HELP
       if calc == "?":
           logging.info("User needed help")
           help()
       elif "help" in calc:
           logging.info("User needed help")
           help()
#MULTIPLICATION
       elif "*" in calc:
            multi()
       elif "x" in calc:
            multi()
#SQUARE
       elif "sq" in calc:
            n = int(input("Number? "))
            print(n * n)
            logging.info(("User squared number ", n, " got result ", (n * n)))
       elif "[]" in calc:
            n = int(input("Number? "))
            logging.info(("User squared number ", n, " got result ", (n * n)))
            print(n * n)
#DIVISION
       elif "/" in calc:
            div()
       elif "div" in calc:
            div()
#SUBTRACTION
       elif calc in "-":
            sub()
       elif calc in "sub":
            sub()
       elif calc in "min":
            sub()
#ADDITION
       elif calc in "+":
            add()
       elif calc in "add":
            add()
#MODULO
       elif calc in "%":
            mod()
       elif calc in "mod":
            mod()
#AREA
       elif calc in "ar":
            area()
       elif calc in "#":
            area()
#VOLUME
       elif calc in "vol":
            uc()
#CUBE
       elif calc in "{}":
            cubedNumber = int(input("\nType the number to be cubed: "))
            print()
            print(cubedNumber ** 3) #Manually cube number
            logging.info(("User cubed number ", cubedNumber, " got result ", (cubedNumber ** 3)))
            print()
#EXIT
       elif calc in "exit":
            logging.info("User exited using `exit' command")
            exit("Looks like you exited.")
#EXPONENTS
       elif calc in "ex":
            origin = int(input("Original number?"))
            ex = int(input("Exponent? "))
            print(origin ** ex)
            logging.info(("User exponented number ", origin, " with ", ex, "getting ", (origin ** ex)))
#ROOTS
       elif calc in "root":
            root = input("Square root or cube root?(square/cube)")
            root = root.lower()
            if root == "square":
                num = input("Number to be rooted?")
                print("That equals.....\n", num ** 0.5)
                logging.info(("user sqrooted number ", (num**0.5)))
            elif root == "cube":
                cu()
            else:
                print("Currently I don't support the root you chose. Hopefully this will change :)")
#EASTER EGG!
       elif calc in "=":
            print()
            number = int(input("Type in a number: "))
            if number == 42:
                print("=42 -- the answer to life, the universe, and everything")
                logging.info("User got the easter egg")
            else:
                print("=" +number)
                logging.info("User used the `=' feature for number ", number)
#NUMBER SYSTEMS
       elif calc in "base":
            base()
#ORD
       elif calc in "ord":
           logging.info(("User ord'ed to get result ", result))
           result = str(ord(int(input("Type in the number to ord: "))))
           print("=", result)
#LOGARITHM
       elif calc in "log":
           log()
#MEMORY
       elif calc in "mem":
            memOrRecall = input("Would you like to set the memory or recall? (set / recall)\nType: ")
            if memOrRecall.lower() in "set":
                remember()
            elif memOrRecall.lower() in "recall":
                readMyMemory()
            else:
                print("You did not type an answer.\nAbort.")
                logging.error("User didn't type an answer in MEM function")
#OTHERWISE
       elif calc in "":
            logging.error("User attempted to type nothing as a command")
            print("Type something!")
       elif calc is None:
            logging.error("User attempted to type nothing as a command")
            print("Type something!")
       else:
            logging.error("User typed an invalid command")
            print('''
            I don't understand your request. Here are the currently supported calculations: 
            * or x; / or div; -, min, or sub; + or add; % or mod (modulo); sq or [] (square); ar or # (area); vol (volume); {} (cube); ex (exponents); root (roots); = (equals); log (logarithm); mem (memory); and base (convert number system). Sorry for the inconvenience
            ''')
print("\nWelcome to Palc!")
try:
    palc() #run all that code
except KeyboardInterrupt: #if ^C
    logging.info("KeyboardInterrupt")
    exit("\nNote that you CAN type `exit' instead of the interrupt key")
except EOFError: #if ^D
    logging.info("EOFError")
    exit("\nWhy ^D? Why not just type `exit'?")
except (ValueError, TypeError):
    logging.critical("ValueError or TypeError")
    print("You typed in an invalid integer or float.")
#except:
    #logging.critical("Unknown Error")
    #print("An unknown error occured. For debugging info, see Line 164") #To debug, comment lines 162, 163 and 164
#EOF
