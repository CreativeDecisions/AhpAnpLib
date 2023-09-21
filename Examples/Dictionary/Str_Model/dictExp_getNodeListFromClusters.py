from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my first model") 
myCA=str.Cluster("Cluster A",0)
myCB=str.Cluster("Cluster B",1)

myNa1=str.Node("a1",0)
myNa2=str.Node("a2",1)
myNa3=str.Node("a3",2)

myNb1=str.Node("b1",0)
myNb2=str.Node("b2",1)

myCA.addNode2Cluster(myNa1)
myCA.addNode2Cluster(myNa2)
myCA.addNode2Cluster(myNa3)
myCB.addNode2Cluster(myNb1)
myCB.addNode2Cluster(myNb2)

myModel.addCluster2Model(myCA)
myModel.addCluster2Model(myCB)
orderednodes=myModel.getNodeListFromClusters()
print(orderednodes)