from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
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
#add nodes to clusters
Cluster1.addNode2Cluster(ANode) 
Cluster1.addNode2Cluster(BNode)

Cluster2.addMultipleNodes2Cluster(CNode,DNode,XNode,YNode,ZNode) 
#add clusters to the model 
myModel.addCluster2Model(Cluster1)
myModel.addCluster2Model(Cluster2)

max=Cluster2.getMaxNodeOrderOfCluster()

print(f"The maximum node display order in Cluster2 is {max}")