import sys, mathmod, mathmod.area, mathmod.volume, mathmod.temperature, mathmod.fibonacci, time
v = mathmod.volume
t = mathmod.temperature
from cprint import cprint

class Testing:
    def __init__(self):
        self.tests = []
        self.finished_tests = []
        self.successful_tests = 0
        self.failed_tests = 0
    def add_test(self, name, expected, function, run_function=None):
        self.tests.append(
                {
                    "name": name,
                    "expected": expected,
                    "function": function,
                    "run_function": run_function,
                }
        )
    def run(self):
        for test in self.tests:
            cprint.warn(f"Testing {test['name']}...", end=" ", flush=True)
            time.sleep(0.1)
            is_function = False
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

class FunctionToRun:
    def __init__(self, func):
        self.func = func

def SpinnerCheck(s):
    time.sleep(3)
    assert "HELLO_WORLD" == s[0];

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
    tests.add_test("mathmod::volume::cuboid", 1.0, lambda:v.volume_cuboid(1,1,1))
    tests.add_test("mathmod::volume::cylinder", 12.566370614359172, lambda:v.volume_cylinder(2,2))
    tests.add_test("mathmod::volume::cylinder::hollow", 25.132741228718345, lambda:v.volume_hollow_cylinder(2,2,2))
    tests.add_test("mathmod::volume::prism", 4.0, lambda:v.volume_prism(2,2))
    tests.add_test("mathmod::volume::sphere", 113.09733552923254, lambda:v.volume_sphere(3))
    tests.add_test("mathmod::volume::sphere::hollow", 0.0, lambda:v.volume_hollow_sphere(3,3))
    tests.add_test("mathmod::volume::pyramid", 3, lambda:v.volume_pyramid(3,3))
    tests.add_test("mathmod::volume::right_circular_cone", 536.165146212658, lambda:v.volume_right_circular_cone(8, 8))#,8,8
    tests.add_test("mathmod::volume::ellipsoid", 25.132741228718345, lambda:v.volume_ellipsoid(1, 2, 3))
    tests.add_test("mathmod::volume::tetrahedron", 0.1178511301977579, lambda:v.volume_tetrahedron(1))

    tests.add_test("mathmod::temperature::cf", 37.4, test_temperature_cf)
    tests.add_test("mathmod::temperature::fcc", 3.0, test_temperature_fc)
    tests.add_test("mathmod::temperature::ck", 0.0, lambda:t.c_to_k(-273.15))
    tests.add_test("mathmod::temperature::kc", -273.15, lambda:t.k_to_c(0))
    tests.add_test("mathmod::temperature::fk", 293.7055555555555, lambda:t.f_to_k(69))
    tests.add_test("mathmod::temperautre::kf", 69, lambda:round(t.k_to_f(293.7055555555555), 10))
    tests.add_test("mathmod::temperature::rf", -39.670000000000016, lambda:t.r_to_f(420))
    tests.add_test("mathmod::temperature::fr", 420, lambda:t.f_to_r(-39.670000000000016))
    tests.add_test("mathmod::temperature::rc", -273.1611111111111, lambda:t.r_to_c(0))
    tests.add_test("mathmod::temperature::cr", -0.02, lambda:round(t.c_to_r(-273.1611111111111), 10))
    tests.add_test("mathmod::temperature::rk", 291.6666666666667, lambda:t.r_to_k(525))
    tests.add_test("mathmod::temperature::kr", 525, lambda:t.k_to_r(291.6666666666667))

    tests.add_test("mathmod::fibonacci", [0, 1, 1, 2, 3], lambda : mathmod.fibonacci.calculate_fixed_fibonacci(5))
    tests.add_test("mathmod::spinner",   ["HELLO_WORLD"] * 1_000_000, lambda:mathmod.spinner(["HELLO_WORLD"], 1_000_000))
    tests.add_test("mathmod::multiplication", 69.0, lambda:mathmod.multiplication(8.625, 2, 4))
    tests.add_test("mathmod::division", 840.0, lambda:mathmod.division(1680.0, 4, 0.5))
    tests.add_test("mathmod::subtraction", 3.0, lambda:mathmod.subtraction(56, 1, -1, 53))
    tests.add_test("mathmod::addition", 489.0, lambda:mathmod.addition(69, 420, 420, -420))
    tests.add_test("mathmod::factorial", 120, lambda:mathmod.factorial(5))
    tests.add_test("mathmod::root::any", 1.0914858393463176, lambda:mathmod.root_general(420, 69))
    tests.add_test("mathmod::exponent", 244140625.0, lambda:mathmod.exponent(5, 12))
    tests.add_test("mathmod::modulo", 1.0, lambda:mathmod.modulo(11, 2))
    tests.add_test("mathmod::tax", 113.0, lambda:mathmod.tax(100, 13))
    tests.add_test("mathmod::log::10", 1.6989700043360187, lambda:mathmod.log(50, mathmod.LogarithmModes.base10))
    tests.add_test("mathmod::log::e" , 2.302585092994046, lambda:mathmod.log(10, mathmod.LogarithmModes.e       ))
    tests.add_test("mathmod::percent::of", 26.0, lambda:mathmod.percent_of(13, 200))
    tests.add_test("mathmod::percentage::find", 13.0, lambda:mathmod.find_percentage(26, 200))
    tests.add_test("mathmod::interest", {"interest": 1, "total": 2}, lambda:mathmod.interest(2, 50, 1))
    tests.run()

if __name__ == "__main__":
    mathmod_tests()
