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
myModel.addNodeConnectionFromNodeToNodeList(node4.name,node1.name,node2.name)
list_connect = [[cluster2, node4, cluster1],[cluster1, node3,cluster2],[cluster1,node1,cluster2],[cluster1,node2,cluster2]]
temp_all_pc_matrices =[[1,0.25,
                        [4,1]],
                        [[1,2],
                        [0.5,1]],
                        [[1,3],
                         [0.33333,1]],
                         [[1,5],
                          [0.2,1]]]
print(input.reorder_pwc_np (myModel,temp_all_pc_matrices,list_connect))