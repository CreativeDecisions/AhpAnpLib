# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
lunchModel=str.Model("Where to order lunch")
print(lunchModel)

#create nodes
goal_node=str.Node("GoalNode",0)

quality=str.Node("1Quality",1)
price=str.Node("2Price",2)
menu=str.Node("3Menu",3)
speed=str.Node("4Speed",4)

alt1=str.Node("1Primanti",5)
alt2=str.Node("2Panera",6)
alt3=str.Node("3Piada",7)

#create clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("3Alternatives",2)

#add nodes to clusters
cluster0.addNode2Cluster(goal_node) 

cluster1.addNode2Cluster(menu)
cluster1.addNode2Cluster(price)
cluster1.addNode2Cluster(quality)
cluster1.addNode2Cluster(speed)

cluster2.addNode2Cluster(alt1)
cluster2.addNode2Cluster(alt2)
cluster2.addNode2Cluster(alt3)

#print cluster contents to confirm that the assignment of nodes was the desired
cluster0.printWithNodes()
cluster1.printWithNodes()
cluster2.printWithNodes()

#add clusters to model 
lunchModel.addCluster2Model(cluster0)
lunchModel.addCluster2Model(cluster1)
lunchModel.addCluster2Model(cluster2)

#print
print(lunchModel)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
lunchModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
lunchModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model
lunchModel.printStruct()

#Generate questionnaires
input.genFullQuest(lunchModel,"important",False)
input.genFirstLineQuest(lunchModel,"important",False)
input.genFirstLineAboveDiagQuest(lunchModel,"important",True)

#Excel questionnaire
# path for mac users
input.export4ExcelQuestFull(lunchModel,"/Users/Shared/PythonAHP/Examples/IO Files/lunchModel_Excel_empty.xlsx",True)
inputFilePath="/Users/Shared/PythonAHP/Examples/IO Files/lunchModel_Excel_filledIn.xlsx"
outputFilePath="/Users/Shared/PythonAHP/Examples/IO Files/lunchModel_Results.xlsx"
# path for windows users
#input.export4ExcelQuestFull(lunchModel,"C:/Users/Public/PythonAHP/Examples/IO Files/lunchModel_Excel_empty.xlsx",True)
#inputFilePath="C:/Users/Public/PythonAHP/Examples/IO Files/lunchModel_Excel_filledIn.xlsx"
#outputFilePath="C:/Users/Public/PythonAHP/Examples/IO Files/lunchModel_Results.xlsx"

#calculate results and save to results Excel file
calc.calcAHPMatricesSave2File(lunchModel,inputFilePath,outputFilePath,True,False,True,False)
calc.sensitivityCellSupermatrixPlot(lunchModel,"3Alternatives",outputFilePath,"1Quality","2Price","3Menu","4Speed")