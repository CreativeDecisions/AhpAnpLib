from AhpAnpLib import inputs_AHPLib as cdf_inp
from AhpAnpLib import structs_AHPLib as cdf_str
from AhpAnpLib import calcs_AHPLib as cdf_calc

#create model
lunchModel=cdf_str.Model("Lunch")
print(lunchModel)

#create nodes
goal_node=cdf_str.Node("GoalNode",0)

quality=cdf_str.Node("1Quality",1)
price=cdf_str.Node("2Price",2)
menu=cdf_str.Node("3Menu",3)
speed=cdf_str.Node("4Speed",4)

alt1=cdf_str.Node("1Primanti",5)
alt2=cdf_str.Node("2Panera",6)
alt3=cdf_str.Node("3Piada",7)

#create clusters
cluster0=cdf_str.Cluster("1Goal",0)
cluster1=cdf_str.Cluster("2Criteria",1)
cluster2=cdf_str.Cluster("3Alternatives",2)

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

cdf_inp.export4ExcelQuestFull(lunchModel,"lunchModel_Excel_empty.xlsx",True)

inputFilePath="lunchModel_Excel_filledIn.xlsx"
outputFilePath="lunchModel_Results.xlsx"

#cdf_inp.importFromExcel(lunchModel,inputFilePath,0)
cdf_calc.calcAHPMatricesSave2File(lunchModel,inputFilePath,outputFilePath,True,True,True,False)
cdf_calc.sensitivityCellSupermatrixPlot(lunchModel,"3Alternatives",outputFilePath,False,"1Quality","2Price","3Menu","4Speed")
