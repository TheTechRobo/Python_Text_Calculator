import mathmod, mathmod.area, mathmod.volume
v = mathmod.volume

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
            print(f"Testing {test['name']}...", end="")
            try:
                assert test['function']() == test['expected']
            except AssertionError:
                print("FAIL")
                self.failed_tests += 1
                self.finished_tests.append(
                        {
                            "name": test['name'],
                            "status": False
                        }
                )
            else:
                self.successful_tests += 1
                print("PASS")
                self.finished_tests.append(
                        {
                            "name": test['name'],
                            "status": True
                        }
                )
        print("\n\tSUMMARY\n\t=======")
        for test in self.finished_tests:
            print(f"{test['name']}:", end=" ")
            print("FAIL") if not test['status'] else print("PASS")
        print(f"\n\t{self.successful_tests} passed; {self.failed_tests} failed; {self.failed_tests + self.successful_tests} total")

def test_area_square():
    return mathmod.area.area_square(5)
def test_volume_cube():
    return v.volume_cube(4)

def mathmod_tests():
    tests = Testing()
    tests.add_test("mathmod::area::square", 25.0, test_area_square)
    tests.add_test("mathmod::volume::cube", 64.0, test_volume_cube)
    tests.run()

print(":WARN: TEST SUITE UNFINISHED !")

if __name__ == "__main__": mathmod_tests()
