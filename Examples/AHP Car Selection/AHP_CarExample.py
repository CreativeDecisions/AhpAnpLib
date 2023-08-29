# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as cdf_inp
from AhpAnpLib import structs_AHPLib as cdf_str
from AhpAnpLib import calcs_AHPLib as cdf_calc

#create model
carModel=cdf_str.Model("Car 2 levels")
#create nodes
goal_node=cdf_str.Node("GoalNode",0)


prestige=cdf_str.Node("1Prestige",1)
price=cdf_str.Node("2Price",2)
mpg=cdf_str.Node("3MPG",3)
comf=cdf_str.Node("4Comfort",4)


alt1=cdf_str.Node("1Acura TL",7)
alt2=cdf_str.Node("2Toyota Camry",8)
alt3=cdf_str.Node("3Honda Civic",9)

#create clusters
cluster0=cdf_str.Cluster("1Goal",0)
cluster1=cdf_str.Cluster("2Criteria",1)
cluster2=cdf_str.Cluster("3Alternatives",2)

#add nodes to clusters
cluster0.addNode2Cluster(goal_node) 

cluster1.addMultipleNodes2Cluster(prestige,price,mpg,comf)

cluster2.addMultipleNodes2Cluster(alt1,alt2,alt3)

#add clusters to model 
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
cdf_inp.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx",True)

# Show nodes and connections
carModel.drawGraphNodes()

# Excel
cdf_inp.export4ExcelQuestFull(carModel,"carModel_Excel_empty.xlsx",True)

inputFilePath="carModel_Excel_filledIn.xlsx"
outputFilepath = "carModel_Excel_Results.xlsx"
 

cdf_calc.calcAHPMatricesSave2File(carModel,inputFilePath,outputFilepath,True,False,True,False)


cdf_calc.sensitivityCellSupermatrixPlot(carModel,"3Alternatives",outputFilepath,False,"1Prestige","2Price","3MPG","4Comfort")
