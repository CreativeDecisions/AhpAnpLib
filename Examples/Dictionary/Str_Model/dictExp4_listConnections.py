from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("My model")
# create nodes
myNode=str.Node("Node Name Z",0)
myOtherNode=str.Node("Node Name X",1)
myNewNode=str.Node("Node Name Y",2)
# create clusters
oneCluster=str.Cluster("Cluster A",0)
otherCluster=str.Cluster("Cluster B",1)
#add nodes to clusters
oneCluster.addNode2Cluster(myNode) 
otherCluster.addNode2Cluster(myOtherNode)
otherCluster.addNode2Cluster(myNewNode)
#add clusters to the model 
myModel.addCluster2Model(oneCluster)
myModel.addCluster2Model(otherCluster)
#add connections from myNode to two nodes in the otherCluster: myOtherNode and myNewNode
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("Node Name Z","Cluster B")

allNodesconnectionsList=myModel.defineAllNodeConnections()

print(allNodesconnectionsList)
