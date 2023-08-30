from AhpAnpLib import structs_AHPLib as str

myCluster=str.Cluster("my cluster",3) 
print('my cluster before updating: ',myCluster)

myCluster.updateC_DisplayOrder(2)
print('my cluster after updating: ',myCluster)