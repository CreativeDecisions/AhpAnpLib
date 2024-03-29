from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import functions_AHPLib as reqLib

new_model=str.Model("From SuperDecisions Car Model")

cl0=str.Cluster("1Goal",0)
nd0=str.Node("Goal Node",0)
cl0.addNode2Cluster(nd0)
new_model.addCluster2Model(cl0)

cl1=str.Cluster("2Criteria",1)
nd1=str.Node("1Cost",1)
cl1.addNode2Cluster(nd1)
nd1=str.Node("2Reliability",2)
cl1.addNode2Cluster(nd1)
nd1=str.Node("3Performance",3)
cl1.addNode2Cluster(nd1)
nd1=str.Node("4Comfort and Style",4)
cl1.addNode2Cluster(nd1)
new_model.addCluster2Model(cl1)

cl2=str.Cluster("3Alternatives",2)
nd2=str.Node("1Toyota Highlander",5)
cl2.addNode2Cluster(nd2)
nd2=str.Node("2Honda Odyssey",6)
cl2.addNode2Cluster(nd2)
nd2=str.Node("3Subaru Outback",7)
cl2.addNode2Cluster(nd2)
new_model.addCluster2Model(cl2)

cl3=str.Cluster("CostSubCriteria",3)
nd3=str.Node("1.1Initial Cost",8)
cl3.addNode2Cluster(nd3)
nd3=str.Node("1.2Monthly Payment",9)
cl3.addNode2Cluster(nd3)
nd3=str.Node("1.3Resale Value",10)
cl3.addNode2Cluster(nd3)
new_model.addCluster2Model(cl3)

new_model.addNodeConnectionFromTo("Goal Node","4Comfort and Style",False)
new_model.addNodeConnectionFromTo("Goal Node","1Cost",False)
new_model.addNodeConnectionFromTo("Goal Node","2Reliability",False)
new_model.addNodeConnectionFromTo("Goal Node","3Performance",False)
new_model.addNodeConnectionFromTo("2Reliability","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("2Reliability","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("2Reliability","3Subaru Outback",False)
new_model.addNodeConnectionFromTo("3Performance","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("3Performance","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("3Performance","3Subaru Outback",False)
new_model.addNodeConnectionFromTo("4Comfort and Style","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("4Comfort and Style","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("4Comfort and Style","3Subaru Outback",False)
new_model.addNodeConnectionFromTo("1Cost","1.1Initial Cost",False)
new_model.addNodeConnectionFromTo("1Cost","1.2Monthly Payment",False)
new_model.addNodeConnectionFromTo("1Cost","1.3Resale Value",False)
new_model.addNodeConnectionFromTo("1.1Initial Cost","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("1.1Initial Cost","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("1.1Initial Cost","3Subaru Outback",False)
new_model.addNodeConnectionFromTo("1.2Monthly Payment","3Subaru Outback",False)
new_model.addNodeConnectionFromTo("1.2Monthly Payment","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("1.2Monthly Payment","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("1.3Resale Value","1Toyota Highlander",False)
new_model.addNodeConnectionFromTo("1.3Resale Value","2Honda Odyssey",False)
new_model.addNodeConnectionFromTo("1.3Resale Value","3Subaru Outback",False)
new_model.printStruct()
input.export4ExcelQuestFull(new_model,"py_file_From SuperDecisions Car Model_empty.xlsx",verb=False)
calc.calcAHPMatricesSave2File(new_model,"From SuperDecisions Car Model_filledIn.xlsx","py_file_From SuperDecisions Car Model_results.xlsx",inputFileUse=True,normalbar=False,idealbar=True,verbal=False)
calc.copyExcelSheet("py_file_From SuperDecisions Car Model_results.xlsx","py_file_From SuperDecisions Car Model_filledIn.xlsx", "pairwise_comp",False)