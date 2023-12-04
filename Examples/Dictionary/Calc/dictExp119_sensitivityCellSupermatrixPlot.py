# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
expModel=str.Model("Example Model")
#create nodes
lv0Node1=str.Node("G",1)
lv1Node1=str.Node("X",1)
lv1Node2=str.Node("Y",2)
lv1Node3=str.Node("Z",3)

aNode1=str.Node("A1",1)
aNode2=str.Node("A2",2)
aNode3=str.Node("A3",3)

#create clusters
cluster0=str.Cluster("Goal",1)
cluster1=str.Cluster("C",1)
cluster2=str.Cluster("A",2)

#add nodes to clusters
cluster0.addNode2Cluster(lv0Node1)
cluster1.addMultipleNodes2Cluster(lv1Node1,lv1Node2,lv1Node3)
cluster2.addMultipleNodes2Cluster(aNode1,aNode2,aNode3)

#add clusters to model 
expModel.addMultipleClusters2Model(cluster0,cluster1,cluster2)

expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Goal","C")
expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("C","A")
#export to Excel all pairwise comparison matrices - to be filled in and imported back
input.export4ExcelQuestFull(expModel,"Exp119_Excel_empty.xlsx",False)

calc.calcMatrices(expModel,"Exp119_Excel_pwfilledin.xlsx",True,False)
# how would nodes priorities in cluster "A" change when "X" changes
calc.sensitivityCellSupermatrixPlot(expModel,"A","show",True,"X")
calc.sensitivityCellSupermatrixPlot(expModel,"A","Exp119_Excel_sensitivity.xlsx",True,"Y","Z")