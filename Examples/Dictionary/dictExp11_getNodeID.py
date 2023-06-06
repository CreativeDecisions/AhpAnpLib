from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("Model’s name")
# create node
XNode=str.Node("Node X",0)
YNode=str.Node("Node Y",1)
# create cluster
myCluster=str.Cluster("My Cluster",0)
#add the node to the cluster
myCluster.addNode2Cluster(XNode) 
myCluster.addNode2Cluster(YNode) 
#add the cluster to the model 
myModel.addCluster2Model(myCluster)

YnodeID=myModel.getNodeIDByName("Node Y")

print(f"ID of Node Y is {YnodeID}")
