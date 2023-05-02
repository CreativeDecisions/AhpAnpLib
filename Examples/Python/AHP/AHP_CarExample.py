# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import functions_AHPLib as reqLib

#You don't need this
# #set here the number of decimals that you want to be displayed
# reqLib.np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

#create model
carModel=str.Model("Select a Car")
#create nodes
goal_node=str.Node("GoalNode",0)

prestige=str.Node("1Prestige",1)
price=str.Node("2Price",2)
mpg=str.Node("3MPG",3)
comf=str.Node("4Comfort",4)

alt1=str.Node("1Acura TL",5)
alt2=str.Node("2Toyota Camry",6)
alt3=str.Node("3Honda Civic",7)

#create clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)
cluster2=str.Cluster("3Alternatives",2)

#add nodes to clusters
cluster0.addNode2Cluster(goal_node) #on purpose wrong assignment

cluster1.addNode2Cluster(prestige)
cluster1.remNodeFromCluster(prestige)
cluster1.addNode2Cluster(price)
cluster1.addNode2Cluster(mpg)
cluster1.addNode2Cluster(comf)

cluster2.addNode2Cluster(alt1)
cluster2.addNode2Cluster(alt2)
cluster2.addNode2Cluster(alt3)


#add clusters to model 
carModel.addCluster2Model(cluster0)
carModel.addCluster2Model(cluster1)
carModel.addCluster2Model(cluster2)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
carModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#set up node connections from all the nodes of the 2Criteria cluster to all the nodes of the cluster 3Alternatives
carModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Criteria","3Alternatives")

# Print out model
carModel.printStruct()

#Generate questionnaires - genFullQuest: all questions -genFirstLineAboveDiagQuest: questions to gather data for the first and the above the diagonal - genFirstLineQuest: gather data just for the first line
#set true to print on screen and save in model object, set false to avoid the terminal printout
print("-----------------------------Questionnaire--------------------------------------\n")
input.genFullQuest(carModel,"important",False)
# print("---------------------------------------------------------------------------\n")

input.genFirstLineQuest(carModel,"important",False)
# print("---------------------------------------------------------------------------\n")

input.genFirstLineAboveDiagQuest(carModel,"important",True)


#Qualtrics questionnaires
#the path is for mac users
input.genexport4QualtricsQuestFull("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Qualtrics_Full.txt",carModel,"important",False)
input.genexport4QualtricsFirstLineQuest("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Qualtrics_FirstLine.txt",carModel,"important",False)
input.genexport4QualtricsFirstLineAboveDiagQuest("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Qualtrics_FirstAndAbove.txt",carModel,"important",False)

# #Google qunestionnaires
#the path is for mac users
input.genexport4GoogleQuestFull("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Google_Full.csv",carModel,"important",False)
input.genexport4GoogleFirstLineQuest("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Google_FirstLine.csv",carModel,"important",False)
input.genexport4GoogleFirstLineAboveDiagQuest("/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/CarModel_Google_FirstAndAbove.csv",carModel,"important",False)

# Excel
#export to Excel all pairwise comparison matrices - to be filled in and imported back
#verbal true will print out info about the values being exported 
input.export4ExcelQuestFull(carModel,"/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/carModel_Excel_empty.xlsx",True)

# the path is for mac users
inputFilePath="/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/carModel_Excel_filledInJudgments.xlsx"
outputFilepath = "/Users/Shared/GITHUB/AhpAnpLib/Examples/IO Files/carModel_Results.xlsx"
 
#------------------------------
#calculate, supermatrix, weighted, limiting and global priorities
#will save results to filepath
#if an input file use is True then it will read the file to generate the latest paiwise comp matrices otherwise from memory
#if normal bar true then will show bars for normal eigen
#if ideal bar true then will show bars for ideal eigen
#if verbal will print out the intermediate results
calc.calcAHPMatricesSave2File(carModel,inputFilePath,outputFilepath,True,False,True,True)

# sensitivity analysis
#set output file path to append to excel or "show" to display on screen
calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFilepath,"1Prestige","2Price","3MPG","4Comfort")

