from AhpAnpLib import calcs_AHPLib as calc

vectorValues = [30,60,80,20,40,20]
transformedM = calc.vector2matrix(vectorValues,4)

print(transformedM)