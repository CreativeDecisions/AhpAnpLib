from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Costs sub model
Costs_Cars=str.Model("Hertz EV vs ICE Costs")
#import structure and connections from Excel
input.readStructFromExcel(Costs_Cars,"BOCR_Cars.xlsx","Costs",False)
input.readConnectionsFromExcel(Costs_Cars,"BOCR_Cars.xlsx","CostsConnections",False)
Costs_Cars.printStruct()
Costs_Cars.drawGraphModel()

input.export4ExcelQuestFull(Costs_Cars,"BOCR_Cars_Costs_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Costs_Cars,"BOCR_Cars_Costs_filledin.xlsx","BOCR_Cars_Costs_results.xlsx")
