from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import calcs_AHPLib as calc

#create model
carModel=str.Model("From Excel Car Model")

#read model structure from the excel file
input.readStructFromExcel(carModel,'Excel_AHP_Car_selection.xlsx',"Structure", False)
#read model connections from the excel file
input.readConnectionsFromExcel(carModel,'Excel_AHP_Car_selection.xlsx',"Connections", False)

#print the model structure to validate the structure
carModel.printStruct()

#export empty questionnaire
input.export4ExcelQuestFull(carModel,"AHP_Car_selection_Excel_questionnaire_empty.xlsx",True)


#import group decision, calculate results and export group decision results
calc.calcAHPMatricesSave2File(carModel,"AHP_Car_selection_Excel_questionnaire_filledin_group.xlsx","Excel_AHP_Car_selection_Group_results.xlsx",True,False,True,False)
