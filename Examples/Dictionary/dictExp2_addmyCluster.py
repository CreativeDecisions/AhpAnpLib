from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my first model") 
myCluster=str.Cluster("Cluster A",0)

myModel.addCluster2Model(myCluster)

print(myModel)
