# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#create model
damModel=str.Model("Choose Dam Level")

#create the nodes and clusters, and add nodes to clusters
goal_cluster=str.Cluster("1Goal cluster",1) #create first cluster: goal_cluster
goal_node=str.Node("Choose dam level",1) # create goal node to be placed in the goal cluster
goal_cluster.addNode2Cluster(goal_node) # add goal_node to goal_cluster
damModel.addCluster2Model(goal_cluster) # add goal_cluster to damModel 

#create the second level: decision criteria
criteria_cluster2=str.Cluster("2Decision Criteria cluster",2)
 #create nodes for criteria cluster
criteria_node21=str.Node("Financial",2)
criteria_node22=str.Node("Political",3)
criteria_node23=str.Node("Environment protection",4)
criteria_node24=str.Node("Social protection",5)
criteria_cluster2.addNode2Cluster(criteria_node21) #add nodes to criteria cluster
criteria_cluster2.addNode2Cluster(criteria_node22)
criteria_cluster2.addNode2Cluster(criteria_node23)
criteria_cluster2.addNode2Cluster(criteria_node24)
damModel.addCluster2Model(criteria_cluster2) #add decision criteria cluster to the model

#create the third level: decision makers
decisionmakers_cluster3=str.Cluster("3Decision Makers cluster",3)
decisionmakers_node31=str.Node("Congress",6) #create nodes for criteria cluster
decisionmakers_node32=str.Node("Dept of Interior",7)
decisionmakers_node33=str.Node("Courts",8)
decisionmakers_node34=str.Node("State",9)
decisionmakers_node35=str.Node("Lobbies",10)
decisionmakers_cluster3.addNode2Cluster(decisionmakers_node31) #add nodes to Decision Makers cluster
decisionmakers_cluster3.addNode2Cluster(decisionmakers_node32)
decisionmakers_cluster3.addNode2Cluster(decisionmakers_node33)
decisionmakers_cluster3.addNode2Cluster(decisionmakers_node34)
decisionmakers_cluster3.addNode2Cluster(decisionmakers_node35)
damModel.addCluster2Model(decisionmakers_cluster3) #add Decision Makers cluster to the model

#create the fourth level: factors
factors_cluster4=str.Cluster("4Factors cluster",4) 
factors_node41=str.Node("Clout",11) #create all nodes for Factors cluster 4 
factors_node42=str.Node("Legal Position",12)
factors_node43=str.Node("Irreversability Environment",13)
factors_node44=str.Node("Archeological Problems",14)
factors_node45=str.Node("Current Financial Resources",15)
factors_node46=str.Node("Potential Financial Loss",16)
factors_cluster4.addNode2Cluster(factors_node41) #add nodes to Factors cluster 4
factors_cluster4.addNode2Cluster(factors_node42)
factors_cluster4.addNode2Cluster(factors_node43)
factors_cluster4.addNode2Cluster(factors_node44)
factors_cluster4.addNode2Cluster(factors_node45)
factors_cluster4.addNode2Cluster(factors_node46)
damModel.addCluster2Model(factors_cluster4)#add Factors cluster to the model

#create the fifth level: Groups Affected
groupsaffected_cluster5=str.Cluster("5Groups Affected cluster",5)
groupsaffected_node51=str.Node("Farmers",17) #create nodes for Groups Affected cluster 5
groupsaffected_node52=str.Node("Recreationists",18)
groupsaffected_node53=str.Node("Power Users",19)
groupsaffected_node54=str.Node("Environmentalists",20)
groupsaffected_cluster5.addNode2Cluster(groupsaffected_node51) #add nodes to cluster 5
groupsaffected_cluster5.addNode2Cluster(groupsaffected_node52)
groupsaffected_cluster5.addNode2Cluster(groupsaffected_node53)
groupsaffected_cluster5.addNode2Cluster(groupsaffected_node54)
damModel.addCluster2Model(groupsaffected_cluster5) #add cluster 5 Groups Affected to the model

#create the sixth level: objectives
objectives_cluster6=str.Cluster("6Objectives cluster",6) 
objectives_node61=str.Node("Irrigation",21) #create nodes for Objectives Cluster 6
objectives_node62=str.Node("Flood Control",22)
objectives_node63=str.Node("Full Water in Dam",23)
objectives_node64=str.Node("Low Water in Dam",24)
objectives_node65=str.Node("Cheap Power",25)
objectives_node66=str.Node("Protect Environment",26)
objectives_cluster6.addNode2Cluster(objectives_node61) #add nodes to cluster 6
objectives_cluster6.addNode2Cluster(objectives_node62)
objectives_cluster6.addNode2Cluster(objectives_node63)
objectives_cluster6.addNode2Cluster(objectives_node64)
objectives_cluster6.addNode2Cluster(objectives_node65)
objectives_cluster6.addNode2Cluster(objectives_node66)
damModel.addCluster2Model(objectives_cluster6) #add cluster 6 objectives to the model

#create the seventh level: alternatives
alternatives_cluster7=str.Cluster("7Alternatives cluster",7)
alternative_node71=str.Node("Full dam",27) #create nodes for Alternatives cluster 7
alternative_node72=str.Node("Half-full dam",28)
alternatives_cluster7.addNode2Cluster(alternative_node71) #add alternative nodes to cluster 7
alternatives_cluster7.addNode2Cluster(alternative_node72)
damModel.addCluster2Model(alternatives_cluster7) # add the alternatives cluster to the model

#set up node connections from the goal node to all the nodes of the decision criteria cluster
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("1Goal cluster","2Decision Criteria cluster")
# set up node connections from all the nodes of the decision criteria cluster 
# to all the nodes of the decison makers cluster
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("2Decision Criteria cluster","3Decision Makers cluster")
# set up node connections from all the nodes of the decison makers cluster
# to all the nodes of the factors cluster
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3Decision Makers cluster","4Factors cluster")
# set up node connections from all the nodes of the factors cluster
# to all the nodes of the groups affected cluster
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4Factors cluster","5Groups Affected cluster")
# set up node connections from nodes in of the groups affected clusters
# to the corresponding nodes of the objectives cluster
# note that different group has different objectives, so not all the nodes connected to all the nodes of the objectives cluster
damModel.addNodeConnectionFromTo("Farmers","Irrigation")
damModel.addNodeConnectionFromTo("Farmers","Flood Control")
damModel.addNodeConnectionFromTo("Recreationists","Full Water in Dam")
damModel.addNodeConnectionFromTo("Recreationists","Low Water in Dam")
damModel.addNodeConnectionFromTo("Power Users","Cheap Power")
damModel.addNodeConnectionFromTo("Environmentalists","Protect Environment")
# set up node connections from all the nodes of the objectives cluster to all the nodes of the alternatives cluster
damModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("6Objectives cluster","7Alternatives cluster")

#print out the model

damModel.printStruct()

# export excel questionnair
# when set up export file name, if no path speficied it will export to your current working folder
# you can also export to a specific folder by specifying the path, e.g. C:/Users/Public/PythonAHP/Examples/IO Files/damModel_Excel_empty.xlsx
input.export4ExcelQuestFull(damModel,"damModel_Excel_empty.xlsx",True)

# inputFile will be the filledin questionnair Excel file
# in the questionnair you can use direct value or paire-wise comparisons 
inputFile="damModel_Excel_direct.xlsx"
# caculated results will be exported the the outputFile
outputFile = "damModel_Results.xlsx"

calc.calcAHPMatricesSave2File(damModel,inputFile,outputFile,True,False,True,True)

# we use the same output file to export sensitivity results
calc.sensitivityCellSupermatrixPlot(damModel,"7Alternatives cluster",outputFile,"Financial")




