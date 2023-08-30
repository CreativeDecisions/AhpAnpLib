from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",1)
clusterY=str.Cluster("cluster y",2)

nodeA=str.Node("node A", 0)
clusterX.addNode2Cluster(nodeA)
nodeB=str.Node("node B", 1)
nodeC=str.Node("node C", 2)
clusterY.addNode2Cluster(nodeB)
clusterY.addNode2Cluster(nodeC)

myModel.addCluster2Model(clusterX)
myModel.addCluster2Model(clusterY)

clusterYID=myModel.getClusterIDByName("cluster y")

myObjCluster = myModel.getClusterObjByID(clusterYID) 

print(f"Nodes of cluster y in the model’s cluster list: {myObjCluster.nodes}")
