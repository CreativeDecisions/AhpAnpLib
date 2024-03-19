from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Opportunities sub model
Opportunities_Cars=str.Model("Hertz EV vs ICE Opportunities")
#import structure and connections from Excel
input.readStructFromExcel(Opportunities_Cars,"BOCR_Cars.xlsx","Opportunities",False)
input.readConnectionsFromExcel(Opportunities_Cars,"BOCR_Cars.xlsx","OpportunitiesConnections",False)
Opportunities_Cars.printStruct()
Opportunities_Cars.drawGraphModel()

input.export4ExcelQuestFull(Opportunities_Cars,"BOCR_Cars_Opportunities_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Opportunities_Cars,"BOCR_Cars_Opportunities_filledin.xlsx","BOCR_Cars_Opportunities_results.xlsx")
