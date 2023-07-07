from AhpAnpLib import structs_AHPLib as str

ACluster=str.Cluster("A",0) 
BCluster=str.Cluster("B",0) 

nodeA=str.Node("A",0)
nodeB=str.Node("B",1)
nodeC=str.Node("C",2)

ACluster.addNode2Cluster(nodeA)
ACluster.addNode2Cluster(nodeB)
BCluster.addNode2Cluster(nodeC)

BCluster.forceAddNode2Cluster(nodeB)
print(f"Acluster has nodes: {ACluster.nodes}")
print(f"Bcluster has nodes: {BCluster.nodes}")