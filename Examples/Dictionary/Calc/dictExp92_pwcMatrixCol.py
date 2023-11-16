# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
expModel=str.Model("Example Model")
#create nodes
g_node=str.Node("G",0)

lv1Node1=str.Node("X",1)
lv1Node2=str.Node("Y",2)
lv1Node3=str.Node("Z",3)

aNode1=str.Node("A1",1)
aNode2=str.Node("A2",2)
aNode3=str.Node("A3",3)

#create clusters
cluster1=str.Cluster("C1",1)
cluster2=str.Cluster("C2",2)
cluster3=str.Cluster("C3",3)

#add nodes to clusters
cluster1.addNode2Cluster(g_node) 
cluster2.addMultipleNodes2Cluster(lv1Node1,lv1Node2,lv1Node3)
cluster3.addMultipleNodes2Cluster(aNode1,aNode2,aNode3)

#add clusters to model 
expModel.addMultipleClusters2Model(cluster1,cluster2,cluster3)

#set up node connections from G Node to all the nodes of cluster2
expModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","C2")
#set up node connections from all the nodes of cluster2 to all the nodes of the cluster3
expModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("C2","C3")

#export to Excel all pairwise comparison matrices - to be filled in and imported back
input.export4ExcelQuestFull(expModel,"Exp92_Excel_empty.xlsx",False)

#Import Excel of all pairwise comparison matrices
input.importFromExcel(expModel,"Exp92_Excel_pwFilledin.xlsx","pairwise_comp")

colPos = calc.pwcMatrixCol (expModel,g_node,g_node)
print('g_node column, g_node row:',colPos)
colPos = calc.pwcMatrixCol (expModel,g_node,lv1Node1)
print('g_node column, lv1Node1 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,g_node,lv1Node2)
print('g_node column, lv1Node2 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,g_node,lv1Node3)
print('g_node column, lv1Node3 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,g_node,aNode1)
print('g_node column, aNode1 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,lv1Node1,aNode1)
print('lvNode1 column, aNode1 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,lv1Node1,aNode2)
print('lvNode1 column, aNode2 row:',colPos)
colPos = calc.pwcMatrixCol (expModel,lv1Node1,aNode3)
print('lvNode1 column, aNode3 row:',colPos)