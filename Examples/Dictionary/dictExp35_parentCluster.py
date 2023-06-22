from AhpAnpLib import structs_AHPLib as str

myNode=str.Node("my node",0) 
mySecNode=str.Node("second node",1) 
XNode=str.Node("x",3) 

myCluster=str.Cluster("my cluster",0)

myCluster.addNode2Cluster(myNode)

print(f"Parent cluster of my node is: {myNode.parCluster}")
print(f"Parent cluster of second node is: {mySecNode.parCluster}")