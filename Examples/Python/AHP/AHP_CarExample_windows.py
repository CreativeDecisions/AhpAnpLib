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
#you can add nodes one at a time or many nodes at once
cluster0.addNode2Cluster(goal_node) 

cluster1.addNode2Cluster(prestige)
cluster1.addNode2Cluster(price)
cluster1.addNode2Cluster(mpg)
cluster1.addNode2Cluster(comf)

cluster2.addNode2Cluster(alt1)
cluster2.addNode2Cluster(alt2)
cluster2.addNode2Cluster(alt3)


#add clusters to the model 

carModel.addCluster2Model(cluster0)
carModel.addCluster2Model(cluster1)
carModel.addCluster2Model(cluster2)
#you can add one cluster at a time or multiple cluster at once e.g. 
#

#set up node connections from Goal Node to all the nodes in the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes in the 2Criteria cluster to all the nodes in the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model structure
carModel.printStruct()

#Generate an Excel to enter judgments 
#export to Excel all pairwise comparison matrices - to be filled in and imported back
#in this example the command will generate files in the location that your command prompt shows, 
# which will be your current working folder
# you can define any destination file path and filename you want e.g.
input.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx")

# Note that you get the carModel_Excel_filledInJudgments.xlsx by starting from
# the carModel_Excel_empty.xlsx, filling in the judgments and then saving it as
# carModel_Excel_filledInJudgments.xlsx 
# while the carModel_Results.xlsx will hold all the calculations and associated results of the 
#AHP/ANP method
inputFilePath="C:\GitCODE\AhpAnpLib\Examples\IO Files\carModel_Excel_filledInJudgments.xlsx"
outputFilepath = "carModel_Results.xlsx"


#------------------------------
#calculate, supermatrix, weighted, limiting and global priorities
#will save results to filepath that is set in outputFulepath above
#if an input file use is True then it will read the file to generate the latest paiwise comp matrices otherwise from memory
#if normal bar true then will show bars for normal eigen
#if ideal bar true then will show bars for ideal eigen
#if verbal will print out the intermediate results
calc.calcAHPMatricesSave2File(carModel,inputFilePath,outputFilepath,True,False,True,False)

# sensitivity analysis
#set output file path to append to excel that set in the outputFilepath above
#you can change the criteria parameters in the command to the criteria that you'd like to conduct sensitivity on
calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFilepath,"1Prestige","2Price","3MPG","4Comfort")

