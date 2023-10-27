from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("my model")
# create nodes
NodeA = str.Node("Node A",0)
NodeX=str.Node("Node X",1)
NodeY=str.Node("Node Y",2)
NodeZ=str.Node("Node Z",3)
NodeR=str.Node("Node R",4)
NodeS=str.Node("Node S",5)
# create clusters
ClusterG=str.Cluster("Cluster G",0)
ClusterA=str.Cluster("Cluster A",0)
ClusterB=str.Cluster("Cluster B",1)
#add nodes to clusters
ClusterG.addNode2Cluster(NodeA)
ClusterA.addMultipleNodes2Cluster(NodeX,NodeY,NodeZ) 
ClusterB.addNode2Cluster(NodeR)
ClusterB.addNode2Cluster(NodeS)
#add clusters to the model 
myModel.addCluster2Model(ClusterG)
myModel.addCluster2Model(ClusterA)
myModel.addCluster2Model(ClusterB)
#add connections from Node X to Node Z
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Cluster G","Cluster A")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Cluster A","Cluster B")
myModel.drawGraphClusters()