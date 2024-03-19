from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Risks sub model
Risks_Cars=str.Model("Hertz EV vs ICE Risks")
#import structure and connections from Excel
input.readStructFromExcel(Risks_Cars,"BOCR_Cars.xlsx","Risks",False)
input.readConnectionsFromExcel(Risks_Cars,"BOCR_Cars.xlsx","RisksConnections",False)
Risks_Cars.printStruct()
Risks_Cars.drawGraphModel()

input.export4ExcelQuestFull(Risks_Cars,"BOCR_Cars_Risks_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Risks_Cars,"BOCR_Cars_Risks_filledin.xlsx","BOCR_Cars_Risks_results.xlsx")