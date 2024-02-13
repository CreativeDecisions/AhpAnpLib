# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc


#Create model
Reservoir = str.Model("Water Reservoir")

#Create two clusters
Purposes = str.Cluster("1Purposes",1)
Alternatives = str.Cluster("2Alternative Water Levels",2)

#Create nodes in Purposes clusters and add them to the cluster
FloodControl = str.Node("1FloodControl",1)
Recreation = str.Node("2Recreation",2)
Hydroelectric = str.Node("3Hydroelectric Power",3)

Purposes.addMultipleNodes2Cluster(FloodControl,Recreation,Hydroelectric)

#Create water levels
Lo = str.Node("1Lo",1)
Med = str.Node("2Med",2)
Hi = str.Node("3Hi",3)

Alternatives.addMultipleNodes2Cluster(Lo,Med,Hi)

#Add clusters to the model
Reservoir.addMultipleClusters2Model(Purposes,Alternatives)

#Add connections from all nodes to all nodes
Reservoir.addNodeConnectionFromAllNodesToAllNodesOfCluster("1Purposes","2Alternative Water Levels")
Reservoir.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Alternative Water Levels","1Purposes")

#Export Questionnaires
input.export4ExcelQuestFull(Reservoir,"WaterReservior_Full_empty.xlsx")

#Import filledin questionnaire to calculate results and export results to Excel file
calc.calcAHPMatricesSave2File(Reservoir,"WaterReservior_Full_filledIn.xlsx","WaterReservior_Full_results.xlsx",True,False,True,True)
