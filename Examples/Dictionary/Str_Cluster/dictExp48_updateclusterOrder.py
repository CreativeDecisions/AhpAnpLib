from AhpAnpLib import structs_AHPLib as str

myCluster=str.Cluster("my cluster",3) 
print('Before updating: ',myCluster)

myCluster.updateC_DisplayOrder(2)
print('After updating: ',myCluster)