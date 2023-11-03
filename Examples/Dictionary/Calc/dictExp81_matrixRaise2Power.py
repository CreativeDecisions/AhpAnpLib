from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import functions_AHPLib as reqLib
pwMatrix = reqLib.np.array([[1,	0.25,	0.33,	0.50],
[4,	1,	3.00,	1.50],
[3,	0.333,	1,	0.33],
[2,	0.667,	3,	1]])
pwMatrixP2 = calc.matrixRaise2Power(pwMatrix,2)
pwMatrixP3 = calc.matrixRaise2Power(pwMatrix,3,False)
pwMatrixP2_Rescale = calc.matrixRaise2Power(pwMatrix,2,True)
pwMatrixP3_Rescale = calc.matrixRaise2Power(pwMatrix,3,True)
pwMatrixP4_Rescale = calc.matrixRaise2Power(pwMatrix,4,True)
print("Matrix when raising powers to 2: ",pwMatrixP2)
print("Matrix when raising powers to 3: ",pwMatrixP3)
print("Matrix when raising powers to 2 and rescaled: ",pwMatrixP2_Rescale)
print("Matrix when raising powers to 3 and rescaled: ",pwMatrixP3_Rescale)
print("Matrix when raising powers to 4 and rescaled: ",pwMatrixP4_Rescale)