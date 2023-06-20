from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my first model") 
myCA=str.Cluster("Cluster A",0)
myCB=str.Cluster("Cluster B",1)

myNa1=str.Node("a1",0)
myNa2=str.Node("a2",1)
myNa3=str.Node("a3",2)

myNb1=str.Node("b1",3)
myNb2=str.Node("b2",4)
myNb3=str.Node("b3",5)

myCA.addNode2Cluster(myNa1)
myCA.addNode2Cluster(myNa2)
myCA.addNode2Cluster(myNa3)
myCB.addNode2Cluster(myNb1)
myCB.addNode2Cluster(myNb2)
myCB.addNode2Cluster(myNb3)

myModel.addCluster2Model(myCA)
myModel.addCluster2Model(myCB)

myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Cluster A","Cluster B")
myModel.printStruct()
myModel.remClusterByNameFromModel("Cluster A")
myModel.printStruct()
