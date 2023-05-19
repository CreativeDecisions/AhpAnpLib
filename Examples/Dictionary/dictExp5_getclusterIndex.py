from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",1)
clusterY=str.Cluster("cluster y",2)

myModel.addCluster2Model(clusterX)
myModel.addCluster2Model(clusterY)

clusterIndex1 = myModel.getClusterIndexByName("cluster x") 
clusterIndex2 = myModel.getClusterIndexByName("cluster y") 

print(clusterIndex1)
print(clusterIndex2)
