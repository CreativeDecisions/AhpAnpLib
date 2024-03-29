from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

#create model
mymodel=str.Model("My Model")

input.readStructFromExcel(mymodel,'ExpN_readconnectionsstruct_Excel.xlsx',"Structure", False)
input.readConnectionsFromExcel(mymodel,'ExpN_readconnectionsstruct_Excel.xlsx',"Connections", True)

mymodel.printStruct()