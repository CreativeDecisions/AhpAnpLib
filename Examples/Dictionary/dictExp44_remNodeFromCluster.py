from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model")

myCluster=str.Cluster("my cluster",0) 

nodeA=str.Node("A",0)
nodeB=str.Node("B",1)
nodeC=str.Node("C",2)

myCluster.addNode2Cluster(nodeA)
myCluster.addNode2Cluster(nodeB)
#myModel.addCluster2Model(myCluster)

myCluster.remNodeFromCluster(nodeA)
print(myCluster.nodes)
