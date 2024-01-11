from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate
# Create AHP model
CarRatings = str.Model("CarJan24")

GoalCL=str.Cluster("1Goal",1)
GoalND = str.Node("CarPurchase",1)
GoalCL.addNode2Cluster(GoalND)

CritCL=str.Cluster("2Criteria",2)
CritPrestigeND=str.Node("1Prestige",1)
CritPriceND=str.Node("2Price",2)
CritMPGND=str.Node("3MPG",3)
CritComftND=str.Node("4Comfort",4)
CritCL.addMultipleNodes2Cluster(CritPrestigeND,CritPriceND,CritMPGND,CritComftND)

CarRatings.addMultipleClusters2Model(GoalCL,CritCL)

CarRatings.addNodeConnectionFromNodeToAllNodesOfCluster("CarPurchase","2Criteria")

input.export4ExcelQuestFull(CarRatings,"Criteria PC.xlsx",True)
calc.calcAHPMatricesSave2File(CarRatings,"Criteria PC filledin.xlsx","Criteria PC results.xlsx",True,True,True,False)

# #########################
# setup Ratings model
# #########################
# Set model as ratings

# add criteria to ratings

# add alternative to ratings

# create scales

# add scales to the model

# assign scales to criteria

# export ratings setup

# fill in ratings scales judgment and ratings setup

# import and calculate ratings results