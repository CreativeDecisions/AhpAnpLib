from AhpAnpLib import structs_AHPLib as str
myModel=str.Model("my first model") 
myClusterA=str.Cluster("Cluster A",0)
myClusterB=str.Cluster("Cluster B",1)
myClusterC=str.Cluster("Cluster C",2)
myClusterD=str.Cluster("Cluster D",3)

myModel.addMultipleClusters2Model(myClusterA,myClusterB,myClusterC,myClusterD)

print(myModel)