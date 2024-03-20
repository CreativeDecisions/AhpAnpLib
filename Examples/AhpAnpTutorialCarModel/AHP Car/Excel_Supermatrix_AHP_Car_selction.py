from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import calcs_AHPLib as calc

#create model
carModel=str.Model("From Supermatrix Car Model")
#read supermatrix from Excel
input.readSupermatrixFromExcel(carModel,"Excel_Supermatrix_AHP_Car_selection.xlsx","Supermatrix", False)

carModel.printStruct()

carModel.drawGraphModel()

#calculate and export the Excel results of the model read from the Excel
calc.calcAHPMatricesSave2File(carModel,"","Excel_Supermatrix_AHP_Car_selection_results.xlsx",False,False,True,False)