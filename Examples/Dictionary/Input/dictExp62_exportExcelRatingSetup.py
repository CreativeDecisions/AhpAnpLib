from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import ratings_AHPLib as rate
from AhpAnpLib import calcs_AHPLib as calc

myModel=str.Model("my model")
# create nodes
GNode=str.Node("G",0)
ANode=str.Node("A",0)
BNode=str.Node("B",1)
CNode=str.Node("C",2)
DNode=str.Node("D",3)
XNode=str.Node("X",4)
YNode=str.Node("Y",5)
ZNode=str.Node("Z",6)
# create clusters
Cluster0=str.Cluster("Goal",0)
Cluster1=str.Cluster("One",0)
Cluster2=str.Cluster("Two",1)
#add nodes to clusters
#add nodes to clusters
Cluster0.addNode2Cluster(GNode)
Cluster1.addNode2Cluster(ANode) 
Cluster1.addNode2Cluster(BNode)
Cluster1.addNode2Cluster(CNode) 
Cluster1.addNode2Cluster(DNode) 
Cluster2.addNode2Cluster(XNode)
Cluster2.addNode2Cluster(YNode)
Cluster2.addNode2Cluster(ZNode)
#add clusters to the model 
myModel.addCluster2Model(Cluster0)
myModel.addCluster2Model(Cluster1)
myModel.addCluster2Model(Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","One")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")
#generate a full questionnaire of the model and export the pairwise comparison matrix to an Excel file
#we can set to show the estimated priorities in the excel using the third parameter show_estimates as True
#we can set the verb as True in the fourth parameter to see the process print out in the screen while export excel
input.export4ExcelQuestFull(myModel,"Example62_Excel_FullQuestionnaire_empty.xlsx",True,False)
#import the pairewise comparison for cirteria now or later
calc.calcAHPMatricesSave2File(myModel,"Example62_Excel_FullQuestionnaire_filledin.xlsx","Example62_Excel_CriteriaPriorities.xlsx",True,False,True)

myModel.setModelTypeRatings()

#add alternatives for ratings
myModel.rateModel.addAlternativesByName("I","II","III")
#add criteria for ratings
myModel.rateModel.addCriteriaByVar(YNode,ZNode)
#create scale
modelScale1=rate.RatScale("ModelScale1")
modelScale1.defineScaleByValue(None,False,["Good",1],["Fair",0.6],["Poor",0.3])
modelScale2=rate.RatScale("ModelScale2")
modelScale2.defineScaleByValue(None,False,["Excellent",0.7],["Good",0.2],["Average",0.1])
#add scale to the model
myModel.rateModel.addScaleByVar(modelScale1)
myModel.rateModel.addScaleByVar(modelScale2)
#assign scales to each criterion
myModel.rateModel.assignScale2CriterionByName("Y","ModelScale1")
myModel.rateModel.assignScale2CriterionByName("Z","ModelScale2")
#export ratings set up
input.export4ExcelRatingsSetup(myModel,"Exp62_RatingsSetup_empty.xlsx",True)