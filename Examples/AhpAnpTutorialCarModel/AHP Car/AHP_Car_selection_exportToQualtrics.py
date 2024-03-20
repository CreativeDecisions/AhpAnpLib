# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create the model
carModel=str.Model("AHP Car Selection")

#create goal cluster
cluster0=str.Cluster("1Goal",0)
#create goal node
goal_node=str.Node("GoalNode",0)
#add the goal to the goal cluster
cluster0.addNode2Cluster(goal_node) 
#add the goal cluster to the model 
carModel.addCluster2Model(cluster0)

#create criteria nodes
cost=str.Node("1Cost",1)
reliability=str.Node("2Reliability",2)
performance=str.Node("3Performance",3)
comf=str.Node("4Comfort and Style",4)
#criteria cluster
cluster1=str.Cluster("2Criteria",1)
#add the nodes to the criteria cluster
cluster1.addMultipleNodes2Cluster(cost,reliability,performance,comf)
#add the cluster to the model
carModel.addCluster2Model(cluster1)

#Cost subcriteria cluster and nodes
cluster2=str.Cluster("CostSubCriteria",2)
subCost1=str.Node("1.1Initial Cost",5)
subCost2=str.Node("1.2Monthly Payment",6)
subCost3=str.Node("1.3Resale Value",7)
cluster2.addMultipleNodes2Cluster(subCost1,subCost2,subCost3)
carModel.addCluster2Model(cluster2)

#alternatives
car1=str.Node("1Toyota Highlander",1)
car2=str.Node("2Honda Odyssey",2)
car3=str.Node("3Subaru Outback",3)
cluster3=str.Cluster("3Alternatives",3)
cluster3.addMultipleNodes2Cluster(car1,car2,car3)
carModel.addCluster2Model(cluster3)

#alternatively you can add all clusters to the model all in once
#carModel.addMultipleClusters2Model(cluster0,cluster1,cluster2,cluster3)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

#1Cost has subcriteria so we don't need to connect 1Cost to alternatives
#use remNodeConnectionFromTo to remove connections from 1Cost to alternatives one by one
carModel.remNodeConnectionFromTo("1Cost","1Toyota Highlander")
carModel.remNodeConnectionFromTo("1Cost","2Honda Odyssey")
carModel.remNodeConnectionFromTo("1Cost","3Subaru Outback")

#connect 1Cost to all of its Subcriteria
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("1Cost","CostSubCriteria")
#and connect all nodes of CostSubCriteria cluster to all alternatives nodes of 2Alternatives cluster
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("CostSubCriteria","3Alternatives")

#print out model to help us to do sanity check
carModel.printStruct()

#export questionnaire for qualtrics
input.genexport4QualtricsQuestFull("AHP_Car_selection_Qualtrics_questionnaire_full.txt",carModel,"preferred", True)


#alternatively, we can export questionnaire with only first line questions or first line and above diagonal questions
input.genexport4QualtricsFirstLineQuest("AHP_Car_selection_Qualtrics_questionnaire_firstline.txt",carModel,"preferred", True)



input.genexport4GoogleFirstLineAboveDiagQuest("AHP_Car_selection_Qualtrics_questionnaire_firstandabove.txt",carModel,"preferred", True)