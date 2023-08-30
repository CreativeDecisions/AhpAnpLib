from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
# create nodes
FirstNode=str.Node("Node X",0)
SecondNode=str.Node("Node Y",1)
ThirdNode=str.Node("Node Z",2)
FourthNode=str.Node("Node R",4)
# create clusters
oneCluster=str.Cluster("Cluster One",0)
twoCluster=str.Cluster("Cluster Two",1)
#add nodes to clusters
oneCluster.addNode2Cluster(FirstNode) 
twoCluster.addMultipleNodes2Cluster(SecondNode,ThirdNode,FourthNode) 

myModel.addCluster2Model(oneCluster)
myModel.addCluster2Model(twoCluster)

myModel.addNodeConnectionFromNodeToNodeList("Node X","Node Y","Node Z")

oneCluster.calcAllConnectionsFrom()

print(oneCluster.connectedTo)