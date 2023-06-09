from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
# create nodes
FirstNode=str.Node("Node X",0)
SecondNode=str.Node("Node Y",1)
ThirdNode=str.Node("Node Z",2)
FourthNode=str.Node("Node R",4)
# create clusters
oneCluster=str.Cluster("Cluster A",0)
twoCluster=str.Cluster("Cluster B",1)
#add nodes to clusters
oneCluster.addNode2Cluster(FirstNode) 
oneCluster.addNode2Cluster(SecondNode)

twoCluster.addNode2Cluster(ThirdNode)
twoCluster.addNode2Cluster(FourthNode)
#add clusters to the model 
myModel.addCluster2Model(oneCluster)
myModel.addCluster2Model(twoCluster)
#add connections from Node X to Node Z
myModel.addNodeConnectionFromTo("Node X","Node Z",True)
myModel.addNodeConnectionFromTo("Node Y","Node Z",False)
myModel.addNodeConnectionFromTo("Node Y","Node R")