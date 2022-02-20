from enum import Enum

class Temperatures(Enum):
    FAHRENHEIT = "f"
    CELSIUS    = "c"
    RANKINE    = "r"
    KELVIN     = "k"

def _handle_error(d):
    try:
        d.value
    except AttributeError as e:
        raise TypeError("You need to use the Temperatures enum. (%s)" % e)

def _select_temperature(source, destination):
    _handle_error(source)
    _handle_error(destination)
    return str(source.value).upper() + str(destination.value).upper()

f_to_c = lambda a : (a - 32) * 5/9
c_to_f = lambda a : (a * 9/5) + 32

c_to_k = lambda a : a + 273.15
k_to_c = lambda a : a - 273.15

f_to_k = lambda a : c_to_k(f_to_c(a))
k_to_f = lambda a : c_to_f(k_to_c(a))

r_to_f = lambda a : a - 459.67
f_to_r = lambda a : a + 459.67

r_to_c = lambda a : (a - 491.69) * 5/9
c_to_r = lambda a : a * 9/5 + 491.67

r_to_k = lambda a : a * 5/9
k_to_r = lambda a : a * 1.8

switch_statement = {
        "FC": f_to_c,
        "CF": c_to_f,
        "CK": c_to_k,
        "KC": k_to_c, #Previously on Matt kay see
        "FK": f_to_k,
        "KF": k_to_f,
        "RF": r_to_f, #interference
        "FR": f_to_r, #for real?!
        # also oui oui baguette
        "RC": r_to_c, #release-candidate
        "CR": c_to_r, #Clash Royale
        "RK": r_to_k, #publishing
        "KR": k_to_r, #dammit why cant the last one have a funny one D:
}

def calculate_temperature(number: float, source: Temperatures, destination: Temperatures) -> float:
    number = float(number)
    formula = switch_statement[_select_temperature(source, destination)]
    return formula(number)
