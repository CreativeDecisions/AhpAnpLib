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
Cluster3=str.Cluster("Three",2)
#add nodes to clusters
Cluster1.addNode2Cluster(ANode) 
Cluster2.addNode2Cluster(BNode)
Cluster2.addNode2Cluster(CNode) 
Cluster2.addNode2Cluster(DNode) 
Cluster3.addNode2Cluster(XNode)
Cluster3.addNode2Cluster(YNode)
Cluster3.addNode2Cluster(ZNode)
#add clusters to the model 
myModel.addCluster2Model(Cluster1)
myModel.addCluster2Model(Cluster2)
myModel.addCluster2Model(Cluster3)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("A","Two")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Two","Three")
#generate a full questionnaire of the model to .txt file that can be imported in Qualtrics survey
FullQuestionnaire= input.genexport4QualtricsQuestFull("Exp53_QualtricsFull.txt",myModel,"important",True)
FullQuestionnaire= input.genexport4QualtricsQuestFull("Exp53_QualtricsSection1.txt",myModel,"dominate",False)