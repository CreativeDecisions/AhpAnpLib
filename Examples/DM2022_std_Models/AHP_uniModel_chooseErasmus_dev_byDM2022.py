# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc


UniModel = str.Model("ChooseErasmus") 

print(UniModel)

#create nodes
goal_node = str.Node("GoalNode",0)

academical = str.Node("1Academical",1)
language = str.Node("2Language",2)
financial = str.Node("3Financial",3)
cultural = str.Node("4Cultural", 4)
city = str.Node("5City",5)

dataCourses = str.Node("6DataCourses",6)
prestige = str.Node("7Prestige",7)
preparatoryCosts = str.Node("8PreparatoryCosts",8)
livingExpenses = str.Node("9LivingExpenses",9)

print(academical,"\n",language,"\n",financial,"\n",cultural,"\n",city)

print(dataCourses,"\n",prestige,"\n",preparatoryCosts,"\n",livingExpenses)

alt1 = str.Node("Pittsburgh",10)
alt2 = str.Node("Seoul",11)
alt3 = str.Node("Eindhoven",12)

print(alt1,"\n",alt2,"\n",alt3)

#create clusters
cluster0 = str.Cluster("1Goal",0)
cluster1 = str.Cluster("2Criteria",1)
cluster2 = str.Cluster("3SubCriteria",2)
cluster3 = str.Cluster("4SubCriteria",3)
cluster4 = str.Cluster("5Alternatives",4)

print(cluster0,"\n",cluster1,"\n",cluster2,"\n",cluster3,"\n",cluster4)

cluster0.addNode2Cluster(goal_node)   
#Cluster goal

cluster1.addNode2Cluster(academical)  
cluster1.addNode2Cluster(language)
cluster1.addNode2Cluster(financial)
cluster1.addNode2Cluster(cultural)
cluster1.addNode2Cluster(city)
#Cluster criteria

cluster2.addNode2Cluster(dataCourses)
cluster2.addNode2Cluster(prestige)
cluster3.addNode2Cluster(preparatoryCosts)
cluster3.addNode2Cluster(livingExpenses)
#Cluster subcriteria


cluster4.addNode2Cluster(alt1)
cluster4.addNode2Cluster(alt2)
cluster4.addNode2Cluster(alt3)
#Cluster Alternatives

cluster0.printWithNodes()
cluster1.printWithNodes()
cluster2.printWithNodes()
cluster3.printWithNodes()
cluster4.printWithNodes()

UniModel.addCluster2Model(cluster0)
UniModel.addCluster2Model(cluster1)
UniModel.addCluster2Model(cluster2)
UniModel.addCluster2Model(cluster3)
UniModel.addCluster2Model(cluster4)

#connections
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("GoalNode","2Criteria")
#creat all the connections from the given Node name"GoalNode" to given Cluster name="2Criteria"
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("1Academical","3SubCriteria")
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("3Financial","4SubCriteria")
UniModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3SubCriteria","5Alternatives")
UniModel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4SubCriteria","5Alternatives")
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("2Language","5Alternatives")
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("4Cultural","5Alternatives")
UniModel.addNodeConnectionFromNodeToAllNodesOfCluster("5City","5Alternatives")
print(UniModel)

UniModel.showAllClusterConnections()

UniModel.showAllNodeConnections()


# questionnaire
# mac path
input.export4ExcelQuestFull(UniModel,'/Users/Shared/PythonAHP/Examples/IO Files/uniModel.xlsx')
inputFilePath="/Users/Shared/PythonAHP/Examples/IO Files/uniModel_Filledin.xlsx"
outputFilepath="/Users/Shared/PythonAHP/Examples/IO Files/uniModel_Results.xlsx"

#windows path
#input.export4ExcelQuestFull(UniModel,'C:/Users/Public/PythonAHP/Examples/IO Files/uniModel.xlsx')
#inputFilePath="C:/Users/Public/PythonAHP/Examples/IO Files/uniModel_Filledin.xlsx"
#outputFilepath="C:/Users/Public/PythonAHP/Examples/IO Files/uniModel_Results.xlsx"

calc.calcAHPMatricesSave2File(UniModel,inputFilePath,outputFilepath,True,False,True,True)

calc.sensitivityCellSupermatrixPlot(UniModel,"5Alternatives",outputFilepath,"1Academical","2Language","3Financial","4Cultural")
