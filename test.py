import sys, mathmod, mathmod.area, mathmod.volume, mathmod.temperature, mathmod.fibonacci
v = mathmod.volume
t = mathmod.temperature
from cprint import cprint

class Testing:
    def __init__(self):
        self.tests = []
        self.finished_tests = []
        self.successful_tests = 0
        self.failed_tests = 0
    def add_test(self, name, expected, function):
        self.tests.append(
                {
                    "name": name,
                    "expected": expected,
                    "function": function,
                }
        )
    def run(self):
        for test in self.tests:
            cprint.warn(f"Testing {test['name']}...", end=" ", flush=True)
            try:
                assert test['function']() == test['expected']
            except AssertionError:
                cprint.err("FAIL")
                self.failed_tests += 1
                self.finished_tests.append(
                        {
                            "name": test['name'],
                            "status": False,
                            "expected": test['expected'],
                            "got": test['function']()
                        }
                )
            else:
                self.successful_tests += 1
                cprint.info("PASS")
                self.finished_tests.append(
                        {
                            "name": test['name'],
                            "status": True
                        }
                )
        print("\n\tSUMMARY\n\t=======")
        for test in self.finished_tests:
            cprint.ok(f"{test['name']}:", end=" ", flush=True)
            if not test['status']:
                cprint.err(f"FAIL (expected {test['expected']}, got {test['got']})")
            else:
                cprint.info("PASS")
        print(f"\n\t{self.successful_tests} passed; {self.failed_tests} failed; {self.failed_tests + self.successful_tests} total")
        sys.exit(self.failed_tests)

def test_area_square():
    return mathmod.area.area_square(5)
def test_volume_cube():
    return v.volume_cube(4)
def fail():
    return False
test_temperature_cf = lambda : t.calculate_temperature(3, t.Temperatures.CELSIUS, t.Temperatures.FAHRENHEIT)
test_temperature_fc = lambda : round(t.calculate_temperature(37.4, t.Temperatures.FAHRENHEIT, t.Temperatures.CELSIUS), 2) #fcc


def mathmod_tests():
    tests = Testing()
    #tests.add_test("fail_always", True, fail)
    tests.add_test("mathmod::area::square", 25.0, test_area_square)
    tests.add_test("mathmod::area::triangle", 2.5, lambda : mathmod.area.area_triangle(1, 5))
    tests.add_test("mathmod::area::rectangle", 32.0, lambda:mathmod.area.area_rectangle( 8, 4))
    tests.add_test("mathmod::area::parallelogram", 64.0, lambda:mathmod.area.area_parallelogram(8,8))
    tests.add_test("mathmod::area::trapezium", 2.0, lambda:mathmod.area.area_trapezium(2,1,1))
    tests.add_test("mathmod::area::circle", 12.566370614359172, lambda:mathmod.area.area_circle(2))
    tests.add_test("mathmod::area::semicircle", 6.283185307179586, lambda:mathmod.area.area_semicircle(2))
    tests.add_test("mathmod::area::ellipse", 91043.35510103221, lambda:mathmod.area.area_ellipse(69, 420))
    tests.add_test("mathmod::area::sector", 6085800.0, lambda:mathmod.area.area_sector(69, 420))
    tests.add_test("mathmod::area::rhombus", 28980.0, lambda :mathmod.area.area_rhombus(69, 420))
    tests.add_test("mathmod::area::ring", 539219.8214694984, lambda:mathmod.area.area_ring(69,420))
    tests.add_test("mathmod::volume::cube", 64.0, test_volume_cube)
    tests.add_test("mathmod::temperature::cf", 37.4, test_temperature_cf)
    tests.add_test("mathmod::temperature::fcc", 3.0, test_temperature_fc)
    tests.add_test("mathmod::fibonacci", [0, 1, 1, 2, 3], lambda : mathmod.fibonacci.calculate_fixed_fibonacci(5))
    tests.run()

cprint.warn(":WARN: TEST SUITE UNFINISHED !")

if __name__ == "__main__":
    mathmod_tests()
