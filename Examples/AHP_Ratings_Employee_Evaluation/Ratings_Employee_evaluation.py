from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

# create the model using Model command, we can give the model a name here or leave it out
EmployEvaluation = str.Model("Employee Evaluation")

# we create cluster, nodes of the model and we add nodes to their coresponding clusters using the add node2cluster command
# the model has three clusters
Goal = str.Cluster("Goal",1)
Criteria = str.Cluster("Criteria",2)
subCriteria = str.Cluster("Work Subcriteria",3)

# we then create nodes in each cluster
GoalNode = str.Node("GoalNode",1)
Goal.addNode2Cluster(GoalNode)

Dependability = str.Node("Dependability",1)
Education = str.Node("Education",2)
Experience = str.Node("Experience",3)
Attitude = str.Node("Attitude",4)
Work = str.Node("Work",5)
Leadership = str.Node("Leadership",6)
# we can use addMultipleNodes2Cluster command to add multiple nodes to the cluster at once
Criteria.addMultipleNodes2Cluster(Dependability,Education,Experience,Attitude,Work,Leadership)

# two subcriteria for Work
Quantity = str.Node("Quantity",1)
Quality = str.Node("Quality",2)
subCriteria.addMultipleNodes2Cluster(Quality,Quantity)

# we created goal, criteria, subcriteria above
# node we add them to the model and add connections to them then we get the AHP structure
EmployEvaluation.addCluster2Model(Goal)
EmployEvaluation.addMultipleClusters2Model(Criteria,subCriteria)
# when add connections we use cluster or node name
# to use the name we can either use the object.name to get the name 
# or we can specify the node/cluster name directly 
EmployEvaluation.addNodeConnectionFromNodeToAllNodesOfCluster(GoalNode.name,Criteria.name)
EmployEvaluation.addNodeConnectionFromNodeToAllNodesOfCluster("Work","Work Subcriteria")

# when use printStruct command to display and valide the model structure
EmployEvaluation.printStruct()

# when create a model, the model by default is a pairewise compare model
# we use setModelTypeRatings command to change the model to a ratings model
EmployEvaluation.setModelTypeRatings()

# to set up the ratings model, we add Criteria first
# when add criteria model we add the bottom level criteria in the AHP model as criteria
# we can use addCriteriaByVar command by specifying criteria object name
# or we can use addCriteriaByName command by specifying criteria name
EmployEvaluation.rateModel.addCriteriaByVar(Dependability,Education,Experience,Attitude,Leadership)
EmployEvaluation.rateModel.addCriteriaByName("Quantity","Quality")

# We can create alternatives in advance 
# or add new alternatives when adding alternatives in the ratings model
# here we add new alternatives directly to the ratings model
# when the alternatives are not created, we use the addAlternativesByName and provide alternative names
# then the alternatives will be created automatically
EmployEvaluation.rateModel.addAlternativesByName("Jim Kendall","Sally Brown","John Carter","Mi Sung","Arturo Chavez")

# 1. Create a new scale (make pairewise comparisons in Excel questionnaire)
scale1=rate.RatScale("OutstandingtoUnsatisfactory")
scale1.defineScaleByValue(None,False,"Outstanding","Very Good","Good","Below Average","Unsatisfactory")
# add the scale to the model
EmployEvaluation.rateModel.addScaleByVar(scale1)
# 2. define scale by value 
scale2=rate.RatScale("EducationScale")
scale2.defineScaleByValue(None,False,["Doctorate",1],["Masters",0.433],["Bachelors",0.177],["High School",0.089])
EmployEvaluation.rateModel.addScaleByVar(scale2)
scale3=rate.RatScale("ExperienceScale")
scale3.defineScaleByValue(None,False,["More than 15 Years",1],["6 up to 15 years",0.428],["3 up to 6 years",0.168],["1 up to 3 years",0.07])
EmployEvaluation.rateModel.addScaleByVar(scale3)
scale4=rate.RatScale("AttitudeScale")
scale4.defineScaleByValue(None,False,["Enthused",1],["Above Average",0.359],["Average",0.153],["Negative",0.057])
EmployEvaluation.rateModel.addScaleByVar(scale4)
# 3. import from rcp file
scale5 = input.readRatScaleRPCfile("QuantityScale", "quantity.rcp")
scale6 = input.readRatScaleRPCfile("QualityScale", "quality.rcp")
EmployEvaluation.rateModel.addScaleByVar(scale5)
EmployEvaluation.rateModel.addScaleByVar(scale6)

# we assign each criterion a scale 
# and the first parameter is the criterion name and the second parameter is scale name
EmployEvaluation.rateModel.assignScale2CriterionByName("Dependability",scale1.name)
EmployEvaluation.rateModel.assignScale2CriterionByName("Education","EducationScale")
EmployEvaluation.rateModel.assignScale2CriterionByName("Experience","ExperienceScale")
EmployEvaluation.rateModel.assignScale2CriterionByName("Attitude","AttitudeScale")
EmployEvaluation.rateModel.assignScale2CriterionByName("Leadership","OutstandingtoUnsatisfactory")
EmployEvaluation.rateModel.assignScale2CriterionByName("Quality","QualityScale")
EmployEvaluation.rateModel.assignScale2CriterionByName("Quantity","QuantityScale")

# The command will export formated excel criteria pairwise compare file
input.export4ExcelQuestFull(EmployEvaluation,"Ratings_Employee_Eval_empty.xlsx",True)

# import judgment from Excel and then calculate criterion priorities then the results will be exported to an excel
calc.calcAHPMatricesSave2File(EmployEvaluation,"Ratings_Employee_Eval_withjudgments.xlsx","Ratings_Employee_Eval_criteriapriorities.xlsx",True,False,True)

# the command will export ratings scales pairwise comparison file in sheet 1
# and the ratings table will be export to the same Excel file in sheet 2
# we can then pairwise compare scale caterogies to get priorities of scales when needed
input.export4ExcelRatingsSetup(EmployEvaluation,"Ratings_Employee_Eval_ratingstable.xlsx",True)

# in this last step, we calculate ratings results and export it to an excel file
input.calcExcelRatings(EmployEvaluation,"Ratings_Employee_Eval_ratingstable_filled.xlsx","Ratings_Employee_Eval_ratingsresults.xlsx")