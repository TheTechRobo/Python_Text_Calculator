import logging
from modules.cprint import cprint

def main(Comandeer):
    globals()['_'] = Commandeer

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

def remember():
    cprint.info(_("This is the memory function.\nIt will save a number into a file that can be used later with Palc... Or you can just read it with a text editor."))
    toRemember = float(input(_("\nPlease enter the number to be saved: ")))
    slot = str(int(input(_("What slot would you like to use? (Hint: you can use any integer you want as long as you remember it)\nType: "))))
    toRemember = str(toRemember)
    memory = open(slot, "w+")
    memory.write(toRemember)
    logging.info("Saved number %s to memory slot %s" % (toRemember, slot))
def readMyMemory():
    cprint.info(_("This is the remember function.\nIt will read a number that was previously stored in a file."))
    try:
        slot = str(int(input(_("What slot number did you use? "))))
        with open(slot, "r") as memory:
            theMem = memory.read()
            cprint.info(_("Number: %s" % theMem))
            logging.info("Retrieved number %s from memory slot %s" % (theMem, slot))
    except Exception as e:
        logging.info("There was an error retrieving the file from memory. (Err %s)" % e)
        cprint.err(_("There was an error reading the file. Did you save the number by using the save function? Did you accidentally rename the file?"))
def whatIsXPercentOf(x, whole):
    """
    whole = ORIGINAL NUMBER
    x = percent
    This finds x percent of whole.
    """
    if whole == 0:
        logging.error("User typed 0 as whole")
        return (_("Please do not type in a zero as the whole."))
    return (x * whole) / 100.0
def findPercentage(part, whole):
    """
    whole = number that would be 100%
    part = number that you want to convert to percentage (i.e. this number out of the number that would be 100%)
    This converts `whole' to be 100%, and finds what percentage `part' is out of 100%. Yes its confusing. Bear with me.
    """
    if whole == 0:
        logging.error("User typed whole zero")
        return (_("Please do not type in a zero as the whole."))
    return 100 * float(part)/float(whole)
def calculateInterest():
    while True: 
        origin = int(input(_("What is the original number? ")))
        rate = float(input(_("What is the rate of interest in percentage (without the percent sign)? ")))
        print()
        howMany = int(input(_('''How many units of time would you like to calculate? 
Essentially, one unit of time could be one month, or one decade. It all depends on what you typed in the rate of interest question: it could be per year, per decade...we didn't ask.
It was up to you to type the correct amount in the rate question.
We have no idea what the rate represented: it could have been that rate per century for all we know.
This calculator wasn't programmed with the ability to track time.
So, with that out of the way, type the amount we should multiply the interest by (aka the amount of units of time).\nType it: ''')))
        inRealNumbers = percentage(whole=origin, percent=rate)
        number = origin + (inRealNumbers * howMany)
        logging.info("INTERESTCALC: origin: %s rate: %s howMany: %s answer: %s" % (origin, rate, howMany, number))
        cprint.info(_("The answer is: \n%s" % number))
        doItAgain = input(_("Would you like to do it again (Y/n)? "))
        doItAgain = doItAgain.lower()
        if doItAgain == _("y"):
            pass
        else:
            cprint.ok(_("Going back..."))
            break
