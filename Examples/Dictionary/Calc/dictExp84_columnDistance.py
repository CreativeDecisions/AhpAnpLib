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
matrixP2=calc.matrixRaise2Power(superMatrix,1,rescale=True)
matrixP3=calc.matrixRaise2Power(superMatrix,3,rescale=True)
print("First matrix:", matrixP2)
print("Second matrix:", matrixP3)
distanceP23 = calc.columnDistance(matrixP2,matrixP3)
print(distanceP23)