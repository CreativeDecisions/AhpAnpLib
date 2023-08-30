from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
# create nodes
ANode = str.Node("Node A",0)
FirstNode=str.Node("Node X",1)
SecondNode=str.Node("Node Y",2)
ThirdNode=str.Node("Node Z",3)
FourthNode=str.Node("Node R",4)
FifthNode=str.Node("Node S",5)
# create clusters
GCluster=str.Cluster("Cluster G",0)
oneCluster=str.Cluster("Cluster A",0)
twoCluster=str.Cluster("Cluster B",1)
#add nodes to clusters
GCluster.addNode2Cluster(ANode)
oneCluster.addNode2Cluster(FirstNode) 
oneCluster.addNode2Cluster(SecondNode)
oneCluster.addNode2Cluster(ThirdNode)

twoCluster.addNode2Cluster(FourthNode)
twoCluster.addNode2Cluster(FifthNode)
#add clusters to the model 
myModel.addCluster2Model(GCluster)
myModel.addCluster2Model(oneCluster)
myModel.addCluster2Model(twoCluster)
#add connections from Node X to Node Z
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Cluster G","Cluster A")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Cluster A","Cluster B")

myModel.drawGraphModel(False)