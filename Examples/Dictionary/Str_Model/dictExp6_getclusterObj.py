from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",1)
clusterY=str.Cluster("cluster y",2)
clusterZ=str.Cluster("cluster z",3)

nodeA=str.Node("node A", 0)
clusterX.addNode2Cluster(nodeA)
nodeB=str.Node("node B", 1)
nodeC=str.Node("node C", 2)
clusterY.addNode2Cluster(nodeB)
clusterY.addNode2Cluster(nodeC)
nodeD=str.Node("node D", 3)
nodeE=str.Node("node E", 4)
clusterZ.addNode2Cluster(nodeD)
clusterZ.addNode2Cluster(nodeE)

myModel.addCluster2Model(clusterX)
myModel.addCluster2Model(clusterY)
myModel.addCluster2Model(clusterZ)

myObjCluster = myModel.getClusterObjByName("cluster y") 

print(f"These are all  my clusters: {myModel.clusters}")
print(f"These are the nodes of cluster y in the model’s cluster list: {myObjCluster.nodes}")
