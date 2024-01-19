from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

#create model
superModel=str.Model("My Model")
input.readSupermatrixFromExcel(superModel,"ExpN_readSupermatrix.xlsx","Sheet1", False)
superModel.printStruct()
calc.calcAHPMatricesSave2File(superModel,"","ExpN_readSupermatrix_pw_results.xlsx",False,False,True,False)