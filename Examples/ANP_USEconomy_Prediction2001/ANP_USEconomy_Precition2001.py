# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

# initialize model
economy2001 = str.Model("US Economy Prediction 2001")

# clusters
primary = str.Cluster("1 Primary Factors",0)
demand = str.Cluster("2 Aggregate Demand Factors",1)
supply = str.Cluster("3 Aggregate Supply Factors", 2)
geopolitical = str.Cluster("4 Geopolitical Contexts", 3)
alternatives = str.Cluster("4Alternatives",4)

# primary nodes
demandN = str.Node("1 Aggregate Demand",1)
supplyN = str.Node("2 Aggregate Supply", 2)
geopoliticalN = str.Node("3 Geopolitical Contexts", 3)
primary.addMultipleNodes2Cluster(demandN,supplyN,geopoliticalN)

# demand nodes
consumption = str.Node("1 Consumption",1)
exports = str.Node("2 Exports",2)
investment = str.Node("3 Investment",3)
confidence = str.Node("4 Confidence",4 )
fiscalp = str.Node("5 Fiscal Policy",5)
monetaryp = str.Node("6 Monetary Policy",6)
expectations = str.Node("7 Expectations", 7)
demand.addMultipleNodes2Cluster(consumption,exports,investment,confidence, fiscalp, monetaryp,expectations)

# supply nodes
labor = str.Node("1 Labor Costs",1)
natural = str.Node("2 Natural Resources Costs",2)
expectations = str.Node("3 Expectations",3)
supply.addMultipleNodes2Cluster(labor,natural,expectations)

# geopolitical contexts
political = str.Node("1 Major International Political Relationships",1)
ecomonic = str.Node("2 Major International Economic Relationships",2)
geopolitical.addMultipleNodes2Cluster(political,ecomonic)

# alternatives
threeM = str.Node("1 Three months",1)
sixM = str.Node("2 Six months",2)
twelveM = str.Node("3 Twelve months",3)
twentyFourM = str.Node("4 Twenty four months",4)
alternatives.addMultipleNodes2Cluster(threeM,sixM,twelveM,twentyFourM)

# add all clusters in the model
economy2001.addMultipleClusters2Model(primary,demand,supply,geopolitical,alternatives)
# add connections
economy2001.addNodeConnectionFromNodeToAllNodesOfCluster("1 Aggregate Demand","2 Aggregate Demand Factors")
economy2001.addNodeConnectionFromNodeToAllNodesOfCluster("2 Aggregate Supply","3 Aggregate Supply Factors")
economy2001.addNodeConnectionFromNodeToAllNodesOfCluster("3 Geopolitical Contexts","4 Geopolitical Contexts")
economy2001.addNodeConnectionFromAllNodesToAllNodesOfCluster("2 Aggregate Demand Factors","4Alternatives")
economy2001.addNodeConnectionFromAllNodesToAllNodesOfCluster("3 Aggregate Supply Factors","4Alternatives")
economy2001.addNodeConnectionFromAllNodesToAllNodesOfCluster("4 Geopolitical Contexts","4Alternatives")

economy2001.addNodeConnectionFromAllNodesToAllNodesOfCluster("4Alternatives","1 Primary Factors")

#validate the model structure
economy2001.printStruct()

#export questionnaire
input.export4ExcelQuestFull(economy2001,"USEconomy_Excel_Full_empty.xlsx")

#import the filledin qurstionnaire and get results
calc.calcAHPMatricesSave2File(economy2001,"USEconomy_Excel_Full_Filledin.xlsx","USEconomy_Excel_Full_results.xlsx",True,False,True,True)








