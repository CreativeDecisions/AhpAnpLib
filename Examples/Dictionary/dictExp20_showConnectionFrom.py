
from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
# create nodes
ANode=str.Node("A",0)
BNode=str.Node("B",1)
CNode=str.Node("C",2)
XNode=str.Node("X",3)
YNode=str.Node("Y",4)
ZNode=str.Node("Z",5)
# create clusters
Cluster1=str.Cluster("One",0)
Cluster2=str.Cluster("Two",1)
#add nodes to clusters
Cluster1.addNode2Cluster(ANode) 
Cluster1.addNode2Cluster(BNode)
Cluster1.addNode2Cluster(CNode) 
Cluster2.addNode2Cluster(XNode)
Cluster2.addNode2Cluster(YNode)
Cluster2.addNode2Cluster(ZNode)
#add clusters to the model 
myModel.addCluster2Model(Cluster1)
myModel.addCluster2Model(Cluster2)
#add connections
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")

myModel.showAllNodeConnectionsFrom("B")