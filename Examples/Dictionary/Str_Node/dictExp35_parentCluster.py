from AhpAnpLib import structs_AHPLib as str

Node1=str.Node("X",0) 
ANode=str.Node("Node A",3) 

myCluster=str.Cluster("my cluster",0)

myCluster.addNode2Cluster(Node1)

print(f"Parent cluster of Node1 is: {Node1.myParentCluster()}")
print(f"Parent cluster of ANode is: {ANode.myParentCluster()}")