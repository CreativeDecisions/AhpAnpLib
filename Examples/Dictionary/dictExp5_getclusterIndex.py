from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my model name") 
clusterX=str.Cluster("cluster x",1)
clusterY=str.Cluster("cluster y",2)
clusterZ=str.Cluster("cluster z",3)


myModel.addCluster2Model(clusterX)
myModel.addCluster2Model(clusterY)
myModel.addCluster2Model(clusterZ)

clusterIndex2 = myModel.getClusterIndexByName("cluster y") 

print(f"These are all  my clusters: {myModel.clusters}")
print(f"Index of cluster y in the model’s cluster list: {clusterIndex2}")
