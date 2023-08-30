# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

damModel=str.Model("Dam Model") #create model

goal_cluster=str.Cluster("1Goal cluster",1) #create first cluster: cluster1
goal_node=str.Node("Choose dam level",1) # create goal node to be placed in cluster1
goal_cluster.addNode2Cluster(goal_node) # add goal_node to goal_cluster1
damModel.addCluster2Model(goal_cluster) #Add cluster1 to lunchModel 

criteria_cluster2=str.Cluster("2Decision Criteria",2) #create second cluster: cluster 2

criteria_node1=str.Node("Financial",21) #create nodes for criteria cluster
criteria_node2=str.Node("Political",22)
criteria_node3=str.Node("Environment protection",23)
criteria_node4=str.Node("Social protection",24)

criteria_cluster2.addMultipleNodes2Cluster(criteria_node1,criteria_node2,criteria_node3,criteria_node4)

damModel.addCluster2Model(criteria_cluster2) #add decision criteria cluster to model

criteria_cluster3=str.Cluster("3Decision Makers",3) #create third cluster: cluster 2

criteria_node31=str.Node("Congress",31) #create nodes for criteria cluster
criteria_node32=str.Node("Dept of Interior",32)
criteria_node33=str.Node("Courts",33)
criteria_node34=str.Node("State",34)
criteria_node35=str.Node("Lobbies",35)

criteria_cluster3.addMultipleNodes2Cluster(criteria_node31,criteria_node32,criteria_node33,criteria_node34,criteria_node35)

damModel.addCluster2Model(criteria_cluster3) #add Decision Makers cluster to model

criteria_cluster4=str.Cluster("4Factors",4) #create fourth cluster for Factors

criteria_node41=str.Node("Clout",41) #create all nodes for Factors cluster 4 
criteria_node42=str.Node("Legal Position",42)
criteria_node43=str.Node("Irreversability Environment",43)
criteria_node44=str.Node("Archeological Problems",44)
criteria_node45=str.Node("Current Financial Resources",45)
criteria_node46=str.Node("Potential Financial Loss",46)

criteria_cluster4.addMultipleNodes2Cluster(criteria_node41,criteria_node42,criteria_node43,criteria_node44,criteria_node45,criteria_node46)

damModel.addCluster2Model(criteria_cluster4)#add Factors cluster to model

criteria_cluster5=str.Cluster("5Groups Affected",5) #create cluster 5 Groups Affected 

criteria_node51=str.Node("Farmers",51) #create nodes for Groups Affected cluster 5
criteria_node52=str.Node("Recreationists",52)
criteria_node53=str.Node("Power Users",53)
criteria_node54=str.Node("Environmentalists",54)

criteria_cluster5.addMultipleNodes2Cluster(criteria_node51,criteria_node52,criteria_node53,criteria_node54)

damModel.addCluster2Model(criteria_cluster5) #add cluster 5 Groups Affected to model

criteria_cluster6=str.Cluster("6Objectives",6) #create cluster 6 objectives 

criteria_node61=str.Node("Irrigation",61) #create nodes for Objectives Cluster 6
criteria_node62=str.Node("Flood Control",62)
criteria_node63=str.Node("Full Water in Dam",63)
criteria_node64=str.Node("Low Water in Dam",64)
criteria_node65=str.Node("Cheap Power",65)
criteria_node66=str.Node("Protect Environment",66)

criteria_cluster6.addMultipleNodes2Cluster(criteria_node61,criteria_node62,criteria_node63,criteria_node64,criteria_node65,criteria_node66)


damModel.addCluster2Model(criteria_cluster6) #add cluster 5 Groups Affected to model

alternatives_cluster7=str.Cluster("7Alternatives",7) #create cluster 7 alterntives

alternative_node71=str.Node("Full dam",71) #create nodes for Alternatives cluster 7
alternative_node72=str.Node("Half-full dam",72)

alternatives_cluster7.addMultipleNodes2Cluster(alternative_node71,alternative_node72)

damModel.addCluster2Model(alternatives_cluster7)



damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("1Goal cluster","2Decision Criteria")
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Decision Criteria","3Decision Makers")
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3Decision Makers","4Factors")
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4Factors","5Groups Affected")
damModel.addNodeConnectionFromNodeToNodeList("Farmers","Irrigation","Flood Control")
damModel.addNodeConnectionFromNodeToNodeList("Recreationists","Full Water in Dam","Low Water in Dam")
damModel.addNodeConnectionFromTo("Power Users","Cheap Power")
damModel.addNodeConnectionFromTo("Environmentalists","Protect Environment")

damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("6Objectives","7Alternatives")

# # Show nodes and connections
damModel.showAllNodeConnections()
print("___________________________________________________________")
damModel.showAllClusterConnections()

# Print out model
damModel.printStruct()

# Excel questionnaire export
input.export4ExcelQuestFull(damModel,"damModel_Excel_empty.xlsx",True)

# Filledin questionnaire import
inputFilePath="damModel_Excel_FilledIn.xlsx"
outputFilepath = "damModel_Excel_Results.xlsx"
calc.calcAHPMatricesSave2File(damModel,inputFilePath,outputFilepath,True,False,True,False)

calc.sensitivityCellSupermatrixPlot(damModel,"7Alternatives",outputFilepath,"Financial","Political","Environment protection","Social protection")
