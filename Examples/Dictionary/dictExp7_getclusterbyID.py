from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",0)

myModel.addCluster2Model(clusterX)
clusterXID=myModel.getClusterIDByName("cluster x")

print(myModel.getClusterObjByID(clusterXID))
