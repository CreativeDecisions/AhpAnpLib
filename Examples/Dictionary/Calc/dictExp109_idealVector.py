from AhpAnpLib import calcs_AHPLib as calc

vectorValues = [0.05,0.35,0.25,0.05,0.3]
idealVector = calc.idealVector(vectorValues)

print(idealVector)