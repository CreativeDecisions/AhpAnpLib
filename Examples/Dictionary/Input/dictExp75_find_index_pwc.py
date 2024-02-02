from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str

myModel = str.Model('my Model')
node1 = str.Node("A",1)
node2 = str.Node("B",2)
node3 = str.Node("C",3)
cluster1 = str.Cluster("Styles",1)
cluster1.addMultipleNodes2Cluster(node1,node2,node3)
cluster2 = str.Cluster("Quality",2)
node4 = str.Node("X",1)
node5 = str.Node("Y",2)
cluster2.addMultipleNodes2Cluster(node4,node5)

myModel.addMultipleClusters2Model(cluster1,cluster2)
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster(cluster1.name,cluster2.name)
list_connect = [[cluster1, node3,cluster2],[cluster1,node1,cluster2],[cluster1,node2,cluster2]]
print(input.find_index_pwc (list_connect,cluster1,node2,cluster2))