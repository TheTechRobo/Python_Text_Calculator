symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

max_base = len(symbol)

def numeral_to_number(number, old_base):
    """
    Convert str number in old_base to an int value.
    """
    result = 0
    for elem in number.lower():
        if elem not in symbol:
            raise Exception('Invalid number.')
        i = symbol.index(elem)
        if i >= old_base:
            raise Exception('Invalid number.')
        result = result * old_base + i
    return result

def number_to_numeral(number, new_base):
    """
    Convert int number to str in new_base.
    """
    result = ''
    while number > 0:
        remainder = number % new_base
        result = symbol[remainder] + result
        number = number // new_base
    return result

def cast(number, old_base, new_base):
    if new_base < 2 or new_base > max_base:
        raise Exception('Not a valid base.')

    if isinstance(number, str):
        if old_base < 2 or old_base > max_base:
            raise Exception('Not a valid base.')
        number = numeral_to_number(number, old_base)
    elif isinstance(number, int):
        if old_base is not None:
            raise Exception('Second argument should be None.')
    else:
        raise Exception("Invalid number.")

    return number_to_numeral(number, new_base)


class Converter:
    def __init__(self, old_base, new_base):
        self.old_base = old_base
        self.new_base = new_base
    def convert(self, number):
        return cast(number, self.old_base, self.new_base)
