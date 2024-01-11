# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create the model
carModel=str.Model("Car 3 Levels")
#create all nodes
goal_node=str.Node("GoalNode",0)

prestige=str.Node("1Prestige",1)
price=str.Node("2Price",2)
mpg=str.Node("3MPG",3)
comf=str.Node("4Comfort",4)

sub1=str.Node("2.1InitialCost",5)
sub2=str.Node("2.2Maintenance",6)

alt1=str.Node("1Acura TL",7)
alt2=str.Node("2Toyota Camry",8)
alt3=str.Node("3Honda Civic",9)

#create all clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("PriceSubCriteria",2)
cluster3=str.Cluster("3Alternatives",3)

#add nodes to clusters
#when add one node to a cluster, use addNode2Cluster command
cluster0.addNode2Cluster(goal_node) 
#when add more than one node to a cluster, use addMultipleNode2Cluster command
cluster1.addMultipleNodes2Cluster(prestige,price,mpg,comf)

cluster2.addNode2Cluster(sub1)
cluster2.addNode2Cluster(sub2)

cluster3.addMultipleNodes2Cluster(alt1,alt2,alt3)

#add clusters to model 
#when add more than one cluster to the model, use addMultipleClusters2Model command
carModel.addMultipleClusters2Model(cluster0,cluster1,cluster2,cluster3)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

#2Price has subcriteria so we don't need to connect 2Price to alternatives
#use remNodeConnectionFromTo to remove connections from 2Price to alternatives one by one
carModel.remNodeConnectionFromTo("2Price","1Acura TL")
carModel.remNodeConnectionFromTo("2Price","2Toyota Camry")
carModel.remNodeConnectionFromTo("2Price","3Honda Civic")

#connect 2Price to all of its Subcriteria
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("2Price","PriceSubCriteria")

#connect all nodes of PriceSubCriteria cluster to all alternatives nodes of 2Alternatives cluster
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("PriceSubCriteria","3Alternatives")

#print out model to help us to do sanity check
carModel.printStruct()

#show nodes and connections to help us to check connections
carModel.drawGraphNodes()

#export Excel questionnaire
#the third parameter we set as True so the estimated results will be included in the exported Excel questionnaire
input.export4ExcelQuestFull(carModel,"carModel_3Lvl_Excel_empty.xlsx",True)

#set up the file path and name of the filledin Excel questionnaires and the final results Excel file
inputFile="carModel_3Lvl_Excel_filledIn.xlsx"
outputFile = "carModel_3Lvl_Excel_Results.xlsx"

#calculate results and export the results to the outputFile.
#we set the fourth parameter as True, so the inpuFile will be used in calculating
#we set the fifth parameter as False, then the normal bar will be displayed in the exported Excel result
#we set the sixth parameter as True, then the ideal bar will be displayed in the exported Excel result
calc.calcAHPMatricesSave2File(carModel,inputFile,outputFile,True,False,True,False)

#sensitivity analysis: we analyze when priority of "1Prestige","2Price","3MPG","4Comfort" changes respectively, how the priorities of all nodes in 3Alternatives will change
#so we set the second parameter as 3Alternatives cluster and the last parameters as criteria node names
#the sensitivity analysis graphs will be exported to the outputFile. It can be the same file with AHP results and sensitivity analysis results will be appended as separate worksheets 
calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFile,False,"1Prestige","2Price","3MPG","4Comfort")