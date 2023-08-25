# from AhpAnpLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create model
lunchModel=str.Model("Where to order lunch")

#create goal and criteria nodes
# goal
goal_node=str.Node("GoalNode",0)
# criteria
quality=str.Node("1Quality",1)
price=str.Node("2Price",2)
menu=str.Node("3Menu",3)
speed=str.Node("4Speed",4)

# alternative nodes can be created here or later
#alt1=str.Node("1Primanti",5)
#alt2=str.Node("2Panera",6)
#alt3=str.Node("3Piada",7)

#create clusters
cluster0=str.Cluster("1Goal",0)
cluster1=str.Cluster("2Criteria",1)

#add nodes to clusters
cluster0.addNode2Cluster(goal_node) 

cluster1.addNode2Cluster(menu)
cluster1.addNode2Cluster(price)
cluster1.addNode2Cluster(quality)
cluster1.addNode2Cluster(speed)

#print cluster contents to confirm that the assignment of nodes was the desired
cluster0.printWithNodes()
cluster1.printWithNodes()

#add goal and criteria clusters to the model 
lunchModel.addCluster2Model(cluster0)
lunchModel.addCluster2Model(cluster1)

#set up node connections from Goal Node to all the nodes of the 2Criteria cluster
#we don't add connections to alternatives in the ratings model
lunchModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")

# Print out model to validate the structure
lunchModel.printStruct()

###########################################
# start to set up ratings model
###########################################
# set the model to be a ratings model using the setModelTypeRatings command
lunchModel.setModelTypeRatings()

# select all criteria from bottom level criteria (if you have subcriteria, then no need to add their parent criteria)
# we can use either rateModel.addCriteriaByVar command to add criteria using variable name
# or we can use rateModel.addCriteriaByName command to add criteria using names of criteria
lunchModel.rateModel.addCriteriaByVar(quality,price,menu)
lunchModel.rateModel.addCriteriaByName("4Speed")
# add ratings altenatives
lunchModel.rateModel.addAlternativesByName("1Primanti","2Panera","3Piada")

# Create scales to use for the evaluation of the alternatives with respect to the selected criteria
scaleEtoP=input.readRatScaleRPCfile("ExcellentToPoor","ExcellentToPoor.rcp")
# add the scale to the model
lunchModel.rateModel.addScaleByVar(scaleEtoP)
# assign the scale to criteria
# we can assign the same scale to multiple criteria
lunchModel.rateModel.assignScale2CriterionByName("1Quality","ExcellentToPoor")
lunchModel.rateModel.assignScale2CriterionByName("3Menu","ExcellentToPoor")

# scale for price
scalePrice=input.readRatScaleRPCfile("PriceScale","HitoLo.rcp")
lunchModel.rateModel.addScaleByVar(scalePrice)
lunchModel.rateModel.assignScale2CriterionByName("2Price","PriceScale")

# scale for speed
scaleSpeed=rate.RatScale("SpeedScale")
scaleSpeed.defineScaleByValue(None,False,["Fast",1],["Average",0.5],["Slow",0.2])
lunchModel.rateModel.addScaleByVar(scaleSpeed)
lunchModel.rateModel.assignScale2CriterionByName("4Speed","SpeedScale")

#Export Excel questionnaire for criteria
input.export4ExcelQuestFull(lunchModel,"lunchModel_Ratings_Criteria_empty.xlsx",True)
#Import Criteria questionnaire to calculate priorities 
input.importFromExcel(lunchModel,"lunchModel_Ratings_Criteria_filledin.xlsx","pairwise_comp",True)
calc.calcAHPMatricesSave2File(lunchModel,"lunchModel_Ratings_Criteria_filledin.xlsx","LunchModel_Ratings_Criteria_initialresults.xlsx",True,False,True)

#Export Excel questionnaire for ratings invluding ratings scale and ratings table
#We need to set third parameter as True
input.export4ExcelRatingsSetup(lunchModel,"LunchModel_Ratings_Table_empty.xlsx",True) 
#Import ratings table and calculate results
input.calcExcelRatings(lunchModel,"LunchModel_Ratings_Table_filledIn.xlsx","lunchModel_Ratings_Results.xlsx",True)