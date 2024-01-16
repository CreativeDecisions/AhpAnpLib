from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
lunchModel=str.Model("Lunch")
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
cluster1.addMultipleNodes2Cluster(menu,quality,price,speed)
cluster2.addMultipleNodes2Cluster(alt1,alt2,alt3)

#print cluster contents to confirm that the assignment of nodes was the desired
cluster0.printWithNodes()
cluster1.printWithNodes()
cluster2.printWithNodes()

#add clusters to model 
lunchModel.addMultipleClusters2Model(cluster0,cluster1,cluster2)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
lunchModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
lunchModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model
lunchModel.printStruct()

#export empty Excel questionnaire
input.export4ExcelQuestFull(lunchModel,"lunchModel_Excel_empty.xlsx",True)

#import filled-in Excel quesionnaire, calculate and export results
inputFilePath="lunchModel_Excel_filledIn.xlsx"
outputFilePath="lunchModel_Results.xlsx"

calc.calcAHPMatricesSave2File(lunchModel,inputFilePath,outputFilePath,True,True,True,False)
# conduct sensitivity analysis with respect to 1Quality, 2Price, 3Menu and 4Speed
calc.sensitivityCellSupermatrixPlot(lunchModel,"3Alternatives",outputFilePath,False,"1Quality","2Price","3Menu","4Speed")
