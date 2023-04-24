# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#model
moveModel=str.Model()

print(moveModel)

#node
goal_node=str.Node("Goal",1)

print(goal_node)
distance_node=str.Node("Distance",2)
weather_node=str.Node("Weather",3)
jobavail_node=str.Node("Job Availability",4)
safety_node=str.Node("Safety",5)

print(distance_node,"\n",weather_node,"\n",jobavail_node,"\n",safety_node)

sunny_subcatnode=str.Node("Sunny",6)
seasons_subcatnode=str.Node("Seasons",7)

print(sunny_subcatnode,"\n",seasons_subcatnode)
disaster_subcatnode2=str.Node("Disaster",8)
crime_subcatnode2=str.Node("Crime",9)

print(disaster_subcatnode2,"\n",crime_subcatnode2)



alt1=str.Node("New York",10)
alt2=str.Node("San Diego",11)
alt3=str.Node("Austin",12)

print(alt1,"\n",alt2,"\n",alt3)

#clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("3SubCriteria",2)
cluster3=str.Cluster("4SubCriteria2",3)
cluster4=str.Cluster("5Alternatives",3)

print(cluster0,"\n",cluster1,"\n",cluster2,"\n",cluster3,"\n",cluster4)

cluster0.addNode2Cluster(goal_node)

cluster1.addNode2Cluster(distance_node)
cluster1.addNode2Cluster(weather_node)
cluster1.addNode2Cluster(jobavail_node)
cluster1.addNode2Cluster(safety_node)


cluster2.addNode2Cluster(sunny_subcatnode)
cluster2.addNode2Cluster(seasons_subcatnode)
cluster3.addNode2Cluster(disaster_subcatnode2)
cluster3.addNode2Cluster(crime_subcatnode2)

cluster4.addNode2Cluster(alt1)
cluster4.addNode2Cluster(alt2)
cluster4.addNode2Cluster(alt3)

cluster0.printWithNodes()
cluster1.printWithNodes()
cluster2.printWithNodes()
cluster3.printWithNodes()
cluster4.printWithNodes()

#add clusters to the model
moveModel.addCluster2Model(cluster0)
moveModel.addCluster2Model(cluster1)
moveModel.addCluster2Model(cluster2)
moveModel.addCluster2Model(cluster3)
moveModel.addCluster2Model(cluster4)

print(moveModel)

#connections

moveModel.addNodeConnectionFromNodeToAllNodesOfCluster("Goal","2Criteria")
moveModel.addNodeConnectionFromNodeToAllNodesOfCluster("Weather","3SubCriteria")
moveModel.addNodeConnectionFromNodeToAllNodesOfCluster("Safety","4SubCriteria2")
moveModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3SubCriteria","5Alternatives")
moveModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4SubCriteria2","5Alternatives")
moveModel.addNodeConnectionFromNodeToAllNodesOfCluster("Distance","5Alternatives")
moveModel.addNodeConnectionFromNodeToAllNodesOfCluster("Job Availability","5Alternatives")

print(moveModel)

moveModel.showAllClusterConnections()

moveModel.showAllNodeConnections()

q1=input.genFullQuest(moveModel,"dominant")

print(q1)
inputFilPath="../../IO Files/moveModel_Excel_Filledin.xlsx"
outputFilepath="../../IO Files/moveModel_Results.xlsx"
calc.calcAHPMatricesSave2File(moveModel,inputFilPath,outputFilepath,False,True,True)
calc.sensitivityCellSupermatrixPlot(moveModel,"5Alternatives",outputFilepath,"Distance","Weather","Job Availability","Safety")


