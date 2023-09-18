# import the required components
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

# Create a model
jobOfferModel = str.Model("Choose an offer")


# Create goal node
goalNode = str.Node("Goal", 0) # Name, Order
print("Goal:\n", goalNode)


# Create criteria nodes
compensationNode = str.Node("Total Compensation", 1)
benefitsNode = str.Node("Benefits", 2)
projectsNode = str.Node("Projects", 3)
advancementNode = str.Node("Career Advancement", 4)
remoteNode = str.Node("Remote", 5)
print("Criteria:\n",compensationNode, "\n", benefitsNode, "\n", projectsNode, "\n", advancementNode, "\n", remoteNode)
print("Criteria:\n",compensationNode, "\n", benefitsNode, "\n", projectsNode, "\n", advancementNode, "\n", remoteNode)

# Create compensation subcriteria nodes
salaryNode = str.Node("Base Salary", 6)
bonusNode = str.Node("Bonus", 7)
stocksNode = str.Node("Stock Options", 8)
savingsNode = str.Node("401K", 9)

# Create benefits subcriteria nodes
costNode = str.Node("Cost", 10)
coverageNode = str.Node("Coverage", 11)

# Create alternative nodes
aws = str.Node("AWS", 12)
fti = str.Node("FTI", 13)
ogilvy = str.Node("Ogilvy", 14)
print("Alternatives:\n", aws, "\n", fti, "\n", ogilvy)

# Create clusters: Goal, Critera, Alternatives
goalCluster = str.Cluster("Goal", 1)
criteriaCluster = str.Cluster("Criteria", 2)
compSubcriteriaCluster = str.Cluster("Total Comp Subcriteria", 3)
benefitsSubcriteriaCluster = str.Cluster("Benefits Subcriteria", 4)
altCluster = str.Cluster("Alternatives", 5)

# Add nodes to clusters
goalCluster.addNode2Cluster(goalNode)

criteriaCluster.addNode2Cluster(compensationNode)
criteriaCluster.addNode2Cluster(benefitsNode)
criteriaCluster.addNode2Cluster(projectsNode)
criteriaCluster.addNode2Cluster(advancementNode)
criteriaCluster.addNode2Cluster(remoteNode)

compSubcriteriaCluster.addNode2Cluster(salaryNode)
compSubcriteriaCluster.addNode2Cluster(bonusNode)
compSubcriteriaCluster.addNode2Cluster(stocksNode)
compSubcriteriaCluster.addNode2Cluster(savingsNode)

benefitsSubcriteriaCluster.addNode2Cluster(costNode)
benefitsSubcriteriaCluster.addNode2Cluster(coverageNode)

altCluster.addNode2Cluster(aws)
altCluster.addNode2Cluster(fti)
altCluster.addNode2Cluster(ogilvy)

# Add clusters to model
jobOfferModel.addCluster2Model(goalCluster)
jobOfferModel.addCluster2Model(criteriaCluster)
jobOfferModel.addCluster2Model(compSubcriteriaCluster)
jobOfferModel.addCluster2Model(benefitsSubcriteriaCluster)
jobOfferModel.addCluster2Model(altCluster)

# Setup node connections

# Create all connections from the given node named Goal to given cluster named Criteria
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Goal", "Criteria")


# Create all connections from the given node named Total Compensation to given cluster named Total Comp Subcriteria
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Total Compensation", "Total Comp Subcriteria")
# Create all connections from given cluster named Total Comp Subcriteria to given cluster named Alternatives
jobOfferModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Total Comp Subcriteria", "Alternatives")

# Create all connections from given node named Benefits to given cluster named Benefits Subcriteria
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Benefits", "Benefits Subcriteria")
# Create all connections from given cluster named Benefits Subcriteria to given cluster named Alternatives
jobOfferModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("Benefits Subcriteria", "Alternatives")

# Create all connections from the given node named Projects to given cluster named Alternatives
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Projects", "Alternatives")

# Create all connections from given node named Career Advancement to given cluster named Alternatives
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Career Advancement", "Alternatives")

# Create all connections from given node named Remote to given cluster named Alternatives
jobOfferModel.addNodeConnectionFromNodeToAllNodesOfCluster("Remote", "Alternatives")

# Create Excel survey and import results
input.export4ExcelQuestFull(jobOfferModel, "AHP_JobOffer_DM2022_Excel_Empty.xlsx")
inputFilePath="AHP_JobOffer_DM2022_Excel_filledin.xlsx"
outputFilepath = "AHP_JobOffer_DM2022_Results.xlsx"
# Import filledin jugments to calculate resuts
calc.calcAHPMatricesSave2File(jobOfferModel,inputFilePath,outputFilepath,True,False,True,True)
# sensitivity analysis
calc.sensitivityCellSupermatrixPlot(jobOfferModel,"Alternatives",outputFilepath,"Total Compensation","Benefits","Career Advancement","Remote")