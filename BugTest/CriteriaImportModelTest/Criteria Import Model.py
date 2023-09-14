from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create model
criteriaimportModel=str.Model("Import Check")
print(criteriaimportModel)

#create nodes
goalnode=str.Node("GoalNode",0)

quality=str.Node("Quality",1)
price=str.Node("Price",2)
menu=str.Node("Menu",3)
speed=str.Node("Speed",4)

#create clusters and assign a name
goalcluster=str.Cluster("Goal",0)
criteriacluster=str.Cluster("Criteria",1)

#add nodes to clusters using variable names
goalcluster.addNode2Cluster(goalnode)


# The order of the nodes in any cluster is controlled by numbering above.
criteriacluster.addMultipleNodes2Cluster(quality,price,menu,speed)

#add clusters to model using variable name
criteriaimportModel.addCluster2Model(goalcluster)
criteriaimportModel.addCluster2Model(criteriacluster)


#print cluster contents to confirm that the assignment of nodes was the desired
goalcluster.printWithNodes()
criteriacluster.printWithNodes()


#create node connections from Goal Node to all criteria nodes
#we must use the names assigned to the variable, not the variable name
criteriaimportModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","Criteria")

# Print out model to validate the structure
criteriaimportModel.printStruct()

# Export empty pairwise comparison Excel spreadsheet

input.export4ExcelQuestFull(criteriaimportModel,"criteriaimportModel_Excel_empty.xlsx",True,False)

calc.calcAHPMatricesSave2File(criteriaimportModel,"criteriaimportModel_Excel_filledin.xlsx","Criteria Import Results.xlsx",True,False,True)