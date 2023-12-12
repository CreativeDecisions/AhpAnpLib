from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

myModel=str.Model("my model")
# create nodes
GNode=str.Node("G",0)
ACri=str.Node("A",0)
BCri=str.Node("B",1)
XsubCri=str.Node("X subCri",4)
YsubCri=str.Node("Y subCri",5)
ZsubCri=str.Node("Z subCri",6)
# create clusters
Cluster0=str.Cluster("Goal",0)
Cluster1=str.Cluster("One",1)
Cluster2=str.Cluster("Two",2)
#add nodes to clusters
Cluster0.addNode2Cluster(GNode)
Cluster1.addMultipleNodes2Cluster(ACri,BCri)  
Cluster2.addMultipleNodes2Cluster(XsubCri,YsubCri,ZsubCri)
#add clusters to the model 
myModel.addMultipleClusters2Model(Cluster0,Cluster1,Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","One")
myModel.addNodeConnectionFromNodeToNodeList("A","X subCri","Y subCri")
myModel.addNodeConnectionFromTo("B","Z subCri")

#set up rating model
myModel.setModelTypeRatings()
#add criteria for ratings
myModel.rateModel.addCriteriaByVar(XsubCri)
myModel.rateModel.addCriteriaByName("Y subCri","Z subCri")

print(myModel.rateModel)