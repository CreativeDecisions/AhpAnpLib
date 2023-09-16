# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

import pandas as pd

#Create model
Reservoir = str.Model("Water Reservoir")

#Create two cluster
Purposes = str.Cluster("1Purposes",1)
Alternatives = str.Cluster("2Alternative Water Levels",2)

#Create nodes in Purposes
FloodControl = str.Node("1FloodControl",1)
Recreation = str.Node("2Recreation",2)
Hydroelectric = str.Node("3Hydroelectric Power",3)

Purposes.addMultipleNodes2Cluster(FloodControl,Recreation,Hydroelectric)

#Create water levels
Lo = str.Node("1Lo",1)
Med = str.Node("2Med",2)
Hi = str.Node("3Hi",3)

Alternatives.addMultipleNodes2Cluster(Lo,Med,Hi)

#Include clusters in the model
Reservoir.addMultipleClusters2Model(Purposes,Alternatives)

#Add connections from all nodes to all nodes
Reservoir.addNodeConnectionFromAllNodesToAllNodesOfCluster("1Purposes","2Alternative Water Levels")
Reservoir.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Alternative Water Levels","1Purposes")

#Export Questionnaires
input.export4ExcelQuestFull(Reservoir,"WaterReservior_Full_empty.xlsx")

input.importFromExcel(Reservoir,"WaterReservior_Full_filledIn.xlsx",0)

#Matrix
listTitles=calc.nodeNameList(Reservoir)

unWighted=calc.calcUnweightedSuperMatrix(Reservoir)

df = pd.DataFrame(unWighted,index=listTitles,columns=listTitles)
filepath = "WaterReservior_results_unWeighted.xlsx"
df.to_excel(filepath)
weighted = calc.calcWeightedSupermatrix(Reservoir)
df3 = pd.DataFrame(weighted,index=listTitles,columns=listTitles)
filepath = "WaterReservior_results_Weighted.xlsx"
df3.to_excel(filepath)

limit = calc.calcLimitANP(weighted,Reservoir)

df2 = pd.DataFrame (limit,index=listTitles)
filepath = "WaterReservior_results_Limit.xlsx"
df2.to_excel(filepath)

#plot
Reservoir.drawGraphModel()
Reservoir.drawGraphClusters()