
from AhpAnpLib import structs_AHPLib as str

myModel=str.Model()
# create nodes
ANode=str.Node("A",0)
BNode=str.Node("B",1)
CNode=str.Node("C",2)
DNode=str.Node("D",3)
XNode=str.Node("X",4)
YNode=str.Node("Y",5)
ZNode=str.Node("Z",6)
# create clusters
Cluster1=str.Cluster("One",0)
Cluster2=str.Cluster("Two",1)
Cluster3=str.Cluster("Three",2)
#add nodes to clusters
Cluster1.addMultipleNodes2Cluster(Cluster2,BNode)

Cluster2.addMultipleNodes2Cluster(CNode,DNode) 
Cluster3.addMultipleNodes2Cluster(XNode,YNode,ZNode)
#add clusters to the model 
myModel.addMultipleClusters2Model(CNode,Cluster2,Cluster3)

#add connections
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Three")

listA=myModel.retAllClusterConnectionsFromNode("A",False)
listB=myModel.retAllClusterConnectionsFromNode("B",True)
listC=myModel.retAllClusterConnectionsFromNode("C")

print("\nConnections from node A:",listA,"\nConnections from node B:",listB,"\nConnections from node C:",listC)
myModel.printStruct()