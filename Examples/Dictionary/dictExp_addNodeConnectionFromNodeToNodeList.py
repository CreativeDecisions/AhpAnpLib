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
oneCluster.addMultipleNodes2Cluster(SecondNode,ThirdNode,FourthNode) 

myModel.addNodeConnectionFromNodeToNodeList("Node X","Node Y","Node Z")

myModel.printStruct()