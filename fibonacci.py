#FIBONACCI
import time
import logging
num0 = 0
num1 = 1
hi = 0
def main(Comandeer):
    global _
    _ = Comandeer

print(_("Press Control-C to stop."))
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
        time.sleep(0.5)
except KeyboardInterrupt: #if ctrl-c
    print(_("Thanks for using Palc's FIBONACCI function!"))
except Exception as e: #if an error occurs
    print(_("An error occured."))
    logging.err("Exception %s" % e)
