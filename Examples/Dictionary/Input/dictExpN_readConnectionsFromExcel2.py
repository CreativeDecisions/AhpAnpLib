from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

#create model
mymodel=str.Model("My Model")
#Create nodes
Gnode = str.Node("GNode",0)
N1 = str.Node("N1",1)
N2 = str.Node("N2",2)
N3 = str.Node("N3",3)
N4 = str.Node("N4",4)
N5 = str.Node("N5",5)
N6 = str.Node("N6",6)

A1 = str.Node("A1",7)
A2 = str.Node("A2",8)
A3 = str.Node("A3",9)

#create clusters and add nodes to clusters
GoalC = str.Cluster("Goal",0)
Cl1 = str.Cluster("Cluster1",1)
Cl2 = str.Cluster("Cluster2",2)
GoalC.addNode2Cluster(Gnode)
Cl1.addMultipleNodes2Cluster(N1,N2,N3,N4,N5,N6)
Cl2.addMultipleNodes2Cluster(A1,A2,A3)
mymodel.addMultipleClusters2Model(GoalC,Cl1,Cl2)

input.readConnectionsFromExcel(mymodel,'ExpN_readconnectionsstruct_Excel.xlsx',"Connections", True)

mymodel.printStruct()