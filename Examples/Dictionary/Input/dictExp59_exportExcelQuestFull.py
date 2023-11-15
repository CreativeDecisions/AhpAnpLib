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
Cluster1=str.Cluster("One",0)
Cluster2=str.Cluster("Two",1)

#add nodes to clusters
Cluster0.addNode2Cluster(GNode)
Cluster1.addMultipleNodes2Cluster(ANode,BNode,CNode,DNode)  
Cluster2.addMultipleNodes2Cluster(XNode,YNode,ZNode)
#add clusters to the model 
myModel.addMultipleClusters2Model(Cluster0,Cluster1,Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","One")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")
#generate a full questionnaire of the model and export the pairwise comparison matrix to an Excel file
#we can set to show the estimated priorities in the excel using the third parameter show_estimates as True
#we can set the verb as True in the fourth parameter to see the process print out in the screen while export excel
input.export4ExcelQuestFull(myModel,"Example59_Excel_FullQuestionnaire_empty.xlsx",False,True)