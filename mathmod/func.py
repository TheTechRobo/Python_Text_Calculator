import logging
from modules.cprint import cprint

def main(Comandeer):
    globals()['_'] = Commandeer

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

def whatIsXPercentOf(x, whole):
    """
    whole = ORIGINAL NUMBER
    x = percent
    This finds x percent of whole.
    """
    if whole == 0:
        raise ValueError("Invalid input (0).")
        return #not sure if this is necessary but hey better safe than sorry
    return (x * whole) / 100.0
def findPercentage(part, whole):
    """
    whole = number that would be 100%
    part = number that you want to convert to percentage (i.e. this number out of the number that would be 100%)
    This converts `whole' to be 100%, and finds what percentage `part' is out of 100%. Yes its confusing. Bear with me.
    """
    if whole == 0:
        raise ValueError("Invalid input (0).")
        return #not sure if this is necessary but hey better safe than sorry
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
