# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
carModel=str.Model("Car 2 levels")
#create nodes
goal_node=str.Node("GoalNode",0)

prestige=str.Node("1Prestige",1)
price=str.Node("2Price",2)
mpg=str.Node("3MPG",3)
comf=str.Node("4Comfort",4)

alt1=str.Node("1Acura TL",7)
alt2=str.Node("2Toyota Camry",8)
alt3=str.Node("3Honda Civic",9)

#create clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("3Alternatives",2)

#add nodes to clusters
#when add one node to a cluster, use addNode2Cluster command
cluster0.addNode2Cluster(goal_node) 
#when add more than one node to a cluster, use addMultipleNode2Cluster command
cluster1.addMultipleNodes2Cluster(prestige,price,mpg,comf)
cluster2.addMultipleNodes2Cluster(alt1,alt2,alt3)

#add clusters to model 
#when add more than one cluster to the model, use addMultipleClusters2Model command
carModel.addMultipleClusters2Model(cluster0,cluster1,cluster2)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model
carModel.printStruct()

# Excel
#export to Excel all pairwise comparison matrices - to be filled in and imported back
#no need to enter all the values
#verbal true will print out info about the values being exported 
input.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx",True)

# Show nodes and connections
carModel.drawGraphNodes()

# Excel
#the third parameter we set as True so the estimated results will be included in the exported Excel questionnaire
input.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx",True)

inputFilePath="carModel_Excel_filledIn.xlsx"
outputFilepath = "carModel_Excel_Results.xlsx"
 
#calculate results and export the results to the outputFile.
#we set the fourth parameter as True, so the inpuFile will be used in calculating
#we set the fifth parameter as False, then the normal bar will be displayed in the exported Excel result
#we set the sixth parameter as True, then the ideal bar will be displayed in the exported Excel result
calc.calcAHPMatricesSave2File(carModel,inputFilePath,outputFilepath,True,False,True,False)

#sensitivity analysis: we analyze when priority of "1Prestige","2Price","3MPG","4Comfort" changes respectively, how the priorities of all nodes in 3Alternatives will change
#so we set the second parameter as 3Alternatives cluster and the last parameters as criteria node names
#the sensitivity analysis graphs will be exported to the outputFile. It can be the same file with AHP results and sensitivity analysis results will be appended as separate worksheets 
calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFilepath,False,"1Prestige","2Price","3MPG","4Comfort")
