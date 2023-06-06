from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",0)
clusterY=str.Cluster("cluster y",0)

myModel.addCluster2Model(clusterX)
myModel.addCluster2Model(clusterY)
clusterYID=myModel.getClusterIDByName("cluster y")

print(clusterYID)
