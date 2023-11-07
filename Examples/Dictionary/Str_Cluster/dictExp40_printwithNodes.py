from AhpAnpLib import structs_AHPLib as str

myCluster=str.Cluster("my cluster",0) 
nodeA=str.Node("A",0)
nodeB=str.Node("B",1)
nodeC=str.Node("C",2)

myCluster.addMultipleNodes2Cluster(nodeA,nodeB,nodeC)

myCluster.printWithNodes()