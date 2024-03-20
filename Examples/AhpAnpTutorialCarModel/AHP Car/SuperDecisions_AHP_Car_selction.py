from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate


#create model
carModel=input.readSDMODfile("From SuperDecisions Car Model","SuperDecisions_AHP_Car_selection.sdmod",True,False)

carModel.printStruct()
calc.calcAHPMatricesSave2File(carModel,"","SuperDecisions_AHP_Car_selection_results.xlsx",False,False,True,False)