import mathmod, mathmod.area, mathmod.volume
v = mathmod.volume

def mathmod_tests():
    assert mathmod.area.area_square(5) == 25.0
    
    assert v.cube(4) == 64.0

print(":WARN: TEST SUITE UNFINISHED !")

if __name__ == "__main__": mathmod_tests()
