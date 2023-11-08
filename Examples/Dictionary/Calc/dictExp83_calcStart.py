from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import functions_AHPLib as reqLib
superMatrix = reqLib.np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0.099, 0, 0, 0, 0, 0, 0, 0],
    [0.425, 0, 0, 0, 0, 0, 0, 0],
    [0.169, 0, 0, 0, 0, 0, 0, 0],
    [0.308, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.707, 0.063, 0.182, 0.705, 0, 0, 0],
    [0, 0.07, 0.194, 0.273, 0.211, 0, 0, 0],
    [0, 0.223, 0.743, 0.545, 0.084, 0, 0, 0]
])
startPower = calc.calcStart(superMatrix)
print(startPower)