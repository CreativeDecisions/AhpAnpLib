from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",0)

myModel.addCluster2Model(clusterX)
myObjCluster= myModel.getClusterObjByName("cluster x")

print(myObjCluster.name)
print(myObjCluster.order)
