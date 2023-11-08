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
hierarchy=calc.calcHierarchy(superMatrix)
print(hierarchy)

superMatrix2 = reqLib.np.array([
    [0, 0, 0, 0.637, 0.2, 0.06],
    [0, 0, 0, 0.258, 0.6, 0.231],
    [0, 0, 0, 0.105, 0.2, 0.709],
    [0.722, 0.072, 0.058, 0, 0, 0],
    [0.205, 0.649, 0.207, 0, 0, 0],
    [0.073, 0.279, 0.735, 0, 0, 0]
])
limitMatrix=calc.calcHierarchy(superMatrix2)