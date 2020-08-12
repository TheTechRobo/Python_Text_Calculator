symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def to_base_10(number, old_base):
    result = 0
    figures = str(number).lower()[::-1]
    for index, elem in enumerate(figures):
        if elem not in symbol:
            raise Exception('Invalid number')
        i = symbol.index(elem)
        if i >= old_base:
            raise Exception('Invalid number')
        result += i * old_base**index
    return str(result)

def from_base_10(number, new_base):
    result = ''
    try:
        number = int(number)
    except:
        raise Exception('Invalid number')
    while number > 0:
        remainder = number % new_base
        result = symbol[remainder] + result
        number = number/new_base
    return result

def cast(number, old_base, new_base):
    if old_base==1 or new_base==1:
        raise Exception('Invalid base')
    if old_base != 10:
        number = to_base_10(number, old_base)
    if new_base != 10:
        number = from_base_10(number, new_base)
    return number
