# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc


shoesModel=str.Model()

# check
print(shoesModel)

# making a goal node
goal_node=str.Node("GoalNode", 1) # IDはあまり重要じゃないみたい？
print(goal_node)

# making criteria
quality=str.Node("Quality", 2)
style=str.Node("Style", 3)
weight=str.Node("Weight", 4)
price=str.Node("Price", 5)

# check
print(quality, "\n", style, "\n", weight, "\n", price)

# making sub-criteria
easy_of_putting_on=str.Node("EasyOfPuttingOn", 6)
slip_resistance=str.Node("SlipResistance", 7)
design=str.Node("Design", 8)
color=str.Node("Color", 9)
easy_of_running=str.Node("EasyOfRunning", 10)
material=str.Node("Material", 11)

# check
print(easy_of_putting_on, "\n", slip_resistance, "\n", design, "\n", color, "\n", easy_of_running, "\n", material)

# making alternatives
alt1=str.Node("Nike", 12)
alt2=str.Node("Brooks", 13)
alt3=str.Node("Asics", 14)

print(alt1)
print(alt2)
print(alt3)

# making clusters
cluster0=str.Cluster("1_Goal", 1) 
cluster1=str.Cluster("2_Criteria", 2)
cluster2a=str.Cluster("3a_SubCriteria", 4)
cluster2b=str.Cluster("3b_SubCriteria", 5)
cluster2c=str.Cluster("3c_SubCriteria", 6)
cluster3=str.Cluster("4_Alternatives", 7)

print(cluster0, "\n", cluster1, "\n", cluster2a, "\n", cluster2b, "\n", cluster2c, "\n", cluster3)

# Add the goal node to Goal cluster
cluster0.addNode2Cluster(goal_node)

# Add 4 nodes to Criteria cluster
cluster1.addNode2Cluster(quality)
cluster1.addNode2Cluster(style)
cluster1.addNode2Cluster(weight)
cluster1.addNode2Cluster(price)

# Add 6 nodes to Sub Criteria cluster
cluster2a.addNode2Cluster(easy_of_putting_on)
cluster2a.addNode2Cluster(slip_resistance)
cluster2b.addNode2Cluster(design)
cluster2b.addNode2Cluster(color)
cluster2c.addNode2Cluster(easy_of_running)
cluster2c.addNode2Cluster(material)

# Add the alternative nodes to Alternatives cluster
cluster3.addNode2Cluster(alt1)
cluster3.addNode2Cluster(alt2)
cluster3.addNode2Cluster(alt3)

# check
cluster0.printWithNodes()
cluster1.printWithNodes()
cluster2a.printWithNodes()
cluster2b.printWithNodes()
cluster2c.printWithNodes()
cluster3.printWithNodes()

# Add the clusters to my model
shoesModel.addCluster2Model(cluster0)
shoesModel.addCluster2Model(cluster1)
shoesModel.addCluster2Model(cluster2a)
shoesModel.addCluster2Model(cluster2b)
shoesModel.addCluster2Model(cluster2c)
shoesModel.addCluster2Model(cluster3)

# connect the goal node and Criteria cluster
shoesModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2_Criteria")


# connect Quality node to 2 nodes
shoesModel.addNodeConnectionFromTo("Quality","EasyOfPuttingOn")
shoesModel.addNodeConnectionFromTo("Quality","SlipResistance")

# connect Style node to 2 nodes
shoesModel.addNodeConnectionFromTo("Style","Design")
shoesModel.addNodeConnectionFromTo("Style","Color")

# connect Weight node to 2 nodes
shoesModel.addNodeConnectionFromTo("Weight","EasyOfRunning")
shoesModel.addNodeConnectionFromTo("Weight","Material")

# connect Sub Criteria cluster to Alternatives cluster
shoesModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3a_SubCriteria","4_Alternatives")
shoesModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3b_SubCriteria","4_Alternatives")
shoesModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3c_SubCriteria","4_Alternatives")
shoesModel.addNodeConnectionFromNodeToAllNodesOfCluster("Price","4_Alternatives")

# connect Price node to 3 alternative nodes directly
shoesModel.addNodeConnectionFromTo("Price","Nike")
shoesModel.addNodeConnectionFromTo("Price","Brooks")
shoesModel.addNodeConnectionFromTo("Price","Asics")

# check all connections in the model
shoesModel.showAllNodeConnections()

input.genFullQuest(shoesModel,"important")

input.genFirstLineAboveDiagQuest(shoesModel,"dominant")

input.genFirstLineQuest(shoesModel,"likelihood")

input.export4ExcelQuestFull(shoesModel, "shoesModel__Excel_empty.xlsx")


inputFilePath="../../IO Files/shoesModel_Excel_filledin.xlsx"
outputFilepath = "../../IO Files/shoesModel_Results.xlsx"

calc.calcAHPMatricesSave2File(shoesModel,inputFilePath,outputFilepath,False,True,True)
calc.sensitivityCellSupermatrixPlot(shoesModel,"4_Alternatives",outputFilepath,"Quality","Weight","Style","Price")