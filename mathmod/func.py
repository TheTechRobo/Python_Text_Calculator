import logging
from modules.cprint import cprint

def main(Comandeer):
    globals()['_'] = Commandeer

if __name__ == "__main__":
    print("Please do not run any of these files directly. They don't do anything useful on their own.")

"""def calculateInterest_RenameLater(origin, rate, units):
    '''
    units: if the rate is per month, and you want to calculate 3 months, you'd type 3 for this. If the rate is per year, and you want 2 years, you'd type 2 for this. And so on.
    rate: How much money per unit of time. So if you want to do 5% per unit of time, you'd type 5. 15%? Type 15.
    origin: Original number.
    '''
    inRealNumbers = percentage(whole=origin, percent=rate)
"""
