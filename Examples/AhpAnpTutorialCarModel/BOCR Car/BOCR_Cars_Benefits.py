from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create Benefits sub model
Benefits_Cars=str.Model("Hertz EV vs ICE Benefits")
#import structure and connections from Excel
input.readStructFromExcel(Benefits_Cars,"BOCR_Cars.xlsx","Benefits",False)
input.readConnectionsFromExcel(Benefits_Cars,"BOCR_Cars.xlsx","BenefitsConnections",False)
Benefits_Cars.printStruct()
Benefits_Cars.drawGraphModel()

input.export4ExcelQuestFull(Benefits_Cars,"BOCR_Cars_Benefits_empty.xlsx",True)
calc.calcAHPMatricesSave2File(Benefits_Cars,"BOCR_Cars_Benefits_filledin.xlsx","BOCR_Cars_Benefits_results.xlsx")
