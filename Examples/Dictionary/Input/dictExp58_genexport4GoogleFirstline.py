from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input

myModel=str.Model("my model")
# create nodes
GNode=str.Node("G",0)
ANode=str.Node("A",0)
BNode=str.Node("B",1)
CNode=str.Node("C",2)
DNode=str.Node("D",3)
XNode=str.Node("X",4)
YNode=str.Node("Y",5)
ZNode=str.Node("Z",6)
# create clusters
Cluster0=str.Cluster("Goal",0)
Cluster1=str.Cluster("One",1)
Cluster2=str.Cluster("Two",2)
#add nodes to clusters
Cluster0.addNode2Cluster(GNode)
Cluster1.addNode2Cluster(ANode,BNode,CNode,DNode) 
Cluster2.addNode2Cluster(XNode)
Cluster2.addNode2Cluster(YNode)
Cluster2.addNode2Cluster(ZNode)
#add clusters to the model 
myModel.addMultipleClusters2Model(Cluster0,Cluster1,Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","One")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")
#generate a questionnaire of the model to .csv file that can be imported in Google Forms
Questionnaire= input.genexport4GoogleFirstLineQuest("Exp58_GoogleFistline.csv",myModel,"important",True)