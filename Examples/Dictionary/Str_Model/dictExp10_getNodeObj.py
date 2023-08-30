from AhpAnpLib import structs_AHPLib as str

myModel=str.Model("Model’s name")
# create node
XNode=str.Node("Node Name X",0)
YNode=str.Node("Node Name Y",1)
# create cluster
myCluster=str.Cluster("My Cluster",0)
#add the node to the cluster
myCluster.addNode2Cluster(XNode) 
myCluster.addNode2Cluster(YNode) 
#add the cluster to the model 
myModel.addCluster2Model(myCluster)

refNodeObj=myModel.getNodeInClusterModelByName("Node Name Y")

nodeYOder=refNodeObj.order
nodeYname=refNodeObj.name
print(f"Display order of node {nodeYname} is {nodeYOder}")


