# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model with a model name as "Select a Car"
carModel=str.Model("Select a Car")

#create nodes

# goal node
goal_node=str.Node("GoalNode",0)

# criteria nodes
prestige=str.Node("1Prestige",1)
price=str.Node("2Price",2)
mpg=str.Node("3MPG",3)
comf=str.Node("4Comfort",4)

# alternative nodes
alt1=str.Node("1Acura TL",5)
alt2=str.Node("2Toyota Camry",6)
alt3=str.Node("3Honda Civic",7)

#create clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("3Alternatives",2)

#add nodes to clusters
cluster0.addNode2Cluster(goal_node) 

# you can add node one at a time using addNode2Cluster command 
# or add multiple nodes to the same cluster in one command addMultipleNodes2Cluster

# add nodes to the cluster one at a time:
cluster1.addNode2Cluster(prestige)
cluster1.addNode2Cluster(price)
cluster1.addNode2Cluster(mpg)
cluster1.addNode2Cluster(comf)

# add multiple nodes to the cluster once:
cluster2.addMultipleNodes2Cluster(alt1,alt2,alt3)

# you can add one cluster to the model at a time using addCluster2Model
# or you use add multiple clusters one a model using one command: addMultipleClusters2Model
# add clusters to the model 
carModel.addCluster2Model(cluster0)
carModel.addMultipleClusters2Model(cluster1,cluster2)


#set up node connections from Goal Node to all the nodes in the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes in the 2Criteria cluster to all the nodes in the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model structure
carModel.printStruct()

#Generate Excel questionnaires 
#export to Excel all pairwise comparison matrices - to be filled in and imported back
# when only file name is specified, the file will be exported to the current working folder
# you can also define path in the export file then the file will be exported to the specific folder
# verbal true will print out info about the values being exported 
input.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx",True)

# import back the excel that has filed in judgments
inputFile="carModel_Excel_filledInJudgments.xlsx"
outputFile = "carModel_Results.xlsx"
calc.calcAHPMatricesSave2File(carModel,inputFile,outputFile,True,False,True,True)

#the bove command will:
#calculate supermatrix, weighted, limiting and global priorities
#will save results to filepath of set as outputFile above
#4th parameter: if an input file use is True then it will read the inputfile to generate the latest paiwise comp matrices otherwise from memory
#5th parameter: if normal bar true then will show bars for normal eigen
#6th parameter: if ideal bar true then will show bars for ideal eigen
#7th parameter: if verbal true will print out the intermediate results

# sensitivity analysis
#set output file the same as results file above will append sensitivity graphs to the Excel 
#you can change the cirteria names in the commands parameters to set the criteria that you'd like to do the sensitivity analysis
calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFile,"1Prestige","2Price","3MPG","4Comfort")

# export model graph
carModel.drawGraphModel()
