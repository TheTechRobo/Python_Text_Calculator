from __future__ import print_function #so that it doesnt quit with invalid syntax; we need to tell the user.
#FIBONACCI
import sys, time
if sys.version_info < (3,4):
    raise ImportError(
    "You are running Mathmod 0.11 on Python 2 or Python < 3.4. Mathmod 0.11 and up is no longer compatible with Python 2.x, and somehow you still got this version installed."
    "\nSorry about that; it should not have happened. Make sure you have pip >= 9.0 to avoid this kind of issue, as well as setuptools >= 24.2 (pip install pip setuptools --upgrade --user)\n"
    "\nYou have two options.\n 1 - Upgrade to Python 3.4 or higher. \n 2 - Install Mathmod 0.10.3 or later in the 0.10 series (pip install mathmod<0.11). "
    "\nThanks for using Mathmod, and sorry for the inconvenience."
    )

def calculate_fixed_fibonacci(amount: int) -> list:
    """
    This is manual fibonacci mode -- that is, you choose how many numbers it does and returns a list of fibonacci up to that amount of calculations. Instead of it in a while loop and printing the numbers to the screen.
    Set `amount' to how many numbers of fibonacci you want to calculate.
    """
    amount = int(amount)
    if amount == 1:
        return [0,]
    if amount == 2:
        return [0,1]
    theList = [0, 1]
    num0 = 0
    num1 = 1
    hi = 0
    amount -= 2 #because we have already added the first two numbers
    for i in range(0, amount):
        num = num0 + num1 #set variable num to the sum of num0 and num1.
        if hi == 0:
            num0 = num
            hi = 1
        else: #every other time this loops it will run this instead of the previous block
            num1 = num # set num1 to num
            hi = 0 #next time it wont do this block it'll do the previous one
        theList.append(num)
    return theList
CalculateFixedFibo = calculate_fixed_fibonacci

def calculate_endless_fibonacci() -> list:
    """
    This is looped fibonacci which is indefinite.
    """
    final = list()
    print("0, 1", end=", ")
    num0 = 0
    num1 = 1
    hi = 0
    try:
        while True:
            num = num0 + num1 #set variable num to the sum of num0 and num1.
            if hi == 0:
                num0 = num
                hi = 1
            else: #every other time this loops it will run this instead of the previous block
                num1 = num # set num1 to num
                hi = 0 #next time it wont do this block it'll do the previous one
            print(num, end=", ", flush=True) #print the current number
            final.append(num)
            time.sleep(0.4)
    finally:
        return final
CalculateLoopedFibo = calculate_endless_fibonacci

if __name__ == "__main__":
    print("Press Control+C to stop.")
    try:
        CalculateLoopedFibo()
    except KeyboardInterrupt:
        print("Thanks for using Mathmod's fibonacci function!")
    except Exception:
        print("An error occured. Raising backtrace...")
        raise
