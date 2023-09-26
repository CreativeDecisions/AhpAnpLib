from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input

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
Cluster2.addNode2Cluster(BNode)
Cluster2.addNode2Cluster(CNode) 
Cluster2.addNode2Cluster(DNode) 
Cluster2.addNode2Cluster(XNode)
Cluster2.addNode2Cluster(YNode)
Cluster2.addNode2Cluster(ZNode)
#add clusters to the model 
myModel.addCluster2Model(Cluster1)
myModel.addCluster2Model(Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("A","Two")
#generate a reduced questionnaire of the model to screen/text, it will only print out when the third parameter is True
Questionnaire= input.genFirstLineQuest(myModel,"important",True)