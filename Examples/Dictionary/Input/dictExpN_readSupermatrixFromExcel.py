from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

#create model
mymodel=str.Model("My Model")

input.readSupermatrixFromExcel(mymodel,'ExpN_readSupermatrix.xlsx',"Sheet1", False)

input.export4ExcelQuestFull(mymodel,"ExpN_readSupermatrix_pw_empty.xlsx")

calc.calcAHPMatricesSave2File(mymodel,"ExpN_readSupermatrix_pw_empty.xlsx","ExpN_readSupermatrix_pw_export.xlsx",False,False,True,True)