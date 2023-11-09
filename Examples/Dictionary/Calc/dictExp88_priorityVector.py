from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import functions_AHPLib as reqLib
pwMatrix = reqLib.np.array(
[[1,	0.25,	0.33,	0],
[4,	1,	3.00,	1.50],
[3,	0.333,	1,	0.33],
[0,	0.667,	3,	1]])
priorities = calc.priorityVector(pwMatrix)
priorities2 = calc.priorityVector(pwMatrix,False)
print('With Hacker fix:',priorities)
print('Without Hacker fix:',priorities2)