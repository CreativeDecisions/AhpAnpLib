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
Cluster0.addNode2Cluster(GNode)
Cluster1.addMultipleNodes2Cluster(ANode,BNode,CNode,DNode)  
Cluster2.addMultipleNodes2Cluster(XNode,YNode,ZNode)
#add clusters to the model 
myModel.addMultipleClusters2Model(Cluster0,Cluster1,Cluster2)
# add connections
myModel.addNodeConnectionFromNodeToAllNodesOfCluster("G","One")
myModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("One","Two")
#generate a full questionnaire of the model and export the pairwise comparison matrix to an Excel file
#we can set to show the estimated priorities in the excel using the third parameter show_estimates as True
#we can set the verb as True in the fourth parameter to see the process print out in the screen while export excel
input.export4ExcelQuestFull(myModel,"Exp68_Excel_FullQuestionnaire_empty.xlsx",True,False)
#import the pairwise comparison for criteria priorities
calc.calcAHPMatricesSave2File(myModel,"Exp68_Excel_FullQuestionnaire_filledin.xlsx","Exp68_Excel_CriteriaPriorities.xlsx",True,False,True)

myModel.setModelTypeRatings()

#add alternatives for ratings
myModel.rateModel.addAlternativesByName("I","II","III")
#add criteria for ratings
myModel.rateModel.addCriteriaByVar(XNode,YNode,ZNode)
#create scale
modelScale1=rate.RatScale("ModelScale1")
modelScale1.defineScaleByValue(None,False,["Good",1],["Fair",0.6],["Poor",0.3])
modelScale2=rate.RatScale("ModelScale2")
modelScale2.defineScaleByValue(None,False,"Excellent","Good","Average")
#add scale to the model
myModel.rateModel.addScaleByVar(modelScale1)
myModel.rateModel.addScaleByVar(modelScale2)
#assign scales to each criterion
myModel.rateModel.assignScale2CriterionByName("X","ModelScale1")
myModel.rateModel.assignScale2CriterionByName("Y","ModelScale2")
myModel.rateModel.assignScale2CriterionByName("Z","ModelScale2")
#export ratings set up
input.export4ExcelRatingsSetup(myModel,"Exp68_RatingsSetup_empty.xlsx",True)
input.importRatingsFromExcel(myModel,"Exp68_RatingsSetup_filledin.xlsx","rating_scales",False)
input.importRatTableFromExcel(myModel,"Exp68_RatingsSetup_filledin.xlsx","rating_table",False)
#calculate ratings results
input.calcRatResults(myModel,"Exp68_RatingsResults.xlsx",False)