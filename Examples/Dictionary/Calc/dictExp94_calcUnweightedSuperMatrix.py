# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
expModel=str.Model("Example Model")
#create nodes
lv1Node1=str.Node("X",1)
lv1Node2=str.Node("Y",2)
lv1Node3=str.Node("Z",3)

aNode1=str.Node("A1",1)
aNode2=str.Node("A2",2)
aNode3=str.Node("A3",3)

#create clusters
cluster1=str.Cluster("C1",1)
cluster2=str.Cluster("C2",2)

#add nodes to clusters
cluster1.addMultipleNodes2Cluster(lv1Node1,lv1Node2,lv1Node3)
cluster2.addMultipleNodes2Cluster(aNode1,aNode2,aNode3)

#add clusters to model 
expModel.addMultipleClusters2Model(cluster1,cluster2)

expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("C1","C2")
expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("C2","C1")
expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("C2","C2")
#export to Excel all pairwise comparison matrices - to be filled in and imported back
input.export4ExcelQuestFull(expModel,"Exp94_Excel_empty.xlsx",False)
#Import Excel of all pairwise comparison matrices
input.importFromExcel(expModel,"Exp94_Excel_pwFilledin.xlsx","pairwise_comp")

unweighted = calc.calcUnweightedSuperMatrix(expModel,True)