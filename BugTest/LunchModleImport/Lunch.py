from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import functions_AHPLib as reqLib

new_model=str.Model("Lunch")

cl0=str.Cluster("Criteria",0)
nd0=str.Node("1Quality",0)
cl0.addNode2Cluster(nd0)
nd0=str.Node("2Price",1)
cl0.addNode2Cluster(nd0)
nd0=str.Node("3Menu",2)
cl0.addNode2Cluster(nd0)
nd0=str.Node("4Speed",3)
cl0.addNode2Cluster(nd0)
new_model.addCluster2Model(cl0)

cl1=str.Cluster("Goal",1)
nd1=str.Node("Goal: where to have lunch",4)
cl1.addNode2Cluster(nd1)
new_model.addCluster2Model(cl1)

new_model.addNodeConnectionFromTo("Goal: where to have lunch","3Menu",False)
new_model.addNodeConnectionFromTo("Goal: where to have lunch","2Price",False)
new_model.addNodeConnectionFromTo("Goal: where to have lunch","1Quality",False)
new_model.addNodeConnectionFromTo("Goal: where to have lunch","4Speed",False)
new_model.printStruct()
input.export4ExcelQuestFull(new_model,"py_file_Lunch_empty.xlsx",verb=False)
calc.calcAHPMatricesSave2File(new_model,"Lunch_filledIn.xlsx","py_file_Lunch_results.xlsx",inputFileUse=True,normalbar=False,idealbar=True,verbal=False)
calc.copyExcelSheet("py_file_Lunch_results.xlsx","py_file_Lunch_filledIn.xlsx", "pairwise_comp",False)