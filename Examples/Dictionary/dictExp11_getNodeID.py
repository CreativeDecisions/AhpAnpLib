from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("Model’s name")
# create node
XNode=str.Node("Node Name X",0)
# create cluster
myCluster=str.Cluster("My Cluster",0)
#add the node to the cluster
myCluster.addNode2Cluster(XNode) 
#add the cluster to the model 
myModel.addCluster2Model(myCluster)

XnodeID=myModel.getNodeIDByName("Node Name X")

print(XnodeID)
