from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("Model’s name")
# create nodes
XNode=str.Node("Node Name X",0)
YNode=str.Node("Node Name Y",1)
ZNode=str.Node("Node Name Z",2)
# create cluster
myCluster=str.Cluster("My Cluster",0)
#add the nodes to the cluster
myCluster.addNode2Cluster(XNode) 
myCluster.addNode2Cluster(YNode)
myCluster.addNode2Cluster(ZNode)
#add the cluster to the model 
myModel.addCluster2Model(myCluster)

nodeZIndex=myModel.getNodeIndexInClusterModelByName("Node Name Z")

print(f"node X index in Cluster My Cluster is {nodeZIndex}")
