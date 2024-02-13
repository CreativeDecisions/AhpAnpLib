# from AHPLib import *
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

#Hamburger model
hamburger=str.Model("Hamburger Marketshare")

#1 Alternatives
clusterAlternatives=str.Cluster("1 Alternatives",0)
a1 = str.Node("1 McDonald's",1)
a2 = str.Node("2 Burger King",2)
a3 = str.Node("3 Wendy's",3)

#2 Advertising Group
clusterAdvertising=str.Cluster("2 Advertising",1)
ad1 = str.Node("1 Creativity",4)
ad2 = str.Node("2 Promotion",5)
ad3 = str.Node("3 Frequency",6)

#3 Quality of Food
clusterQualityofFood=str.Cluster("3 Quality of Food",2)
q1 = str.Node("1 Nutrition",7)
q2 = str.Node("2 Taste",8)
q3 = str.Node("3 Portion",9)

#4 Other
clusterOther=str.Cluster("4 Other",3)
o1 = str.Node("1 Price",10)
o2 = str.Node("2 Location",11)
o3 = str.Node("3 Service",12)
o4 = str.Node("4 Speed",13)
o5 = str.Node("5 Cleanliness",14)
o6 = str.Node("6 Menu Item",15)
o7 = str.Node("7 Take-out",16)
o8 = str.Node("8 Reputation",17)

clusterAlternatives.addNode2Cluster(a1) 
clusterAlternatives.addNode2Cluster(a2) 
clusterAlternatives.addNode2Cluster(a3) 

clusterAdvertising.addMultipleNodes2Cluster(ad1,ad2,ad3)
clusterQualityofFood.addMultipleNodes2Cluster(q1,q2,q3)
clusterOther.addMultipleNodes2Cluster(o1,o2,o3,o4,o5,o6,o7,o8)

hamburger.addMultipleClusters2Model(clusterAlternatives,clusterAdvertising,clusterQualityofFood,clusterOther)

#alternative nodes connects to all nodes except themselves in Alternatives cluster
hamburger.addNodeConnectionFromTo("1 McDonald's","2 Burger King")
hamburger.addNodeConnectionFromTo("1 McDonald's","3 Wendy's")
hamburger.addNodeConnectionFromTo("2 Burger King","1 McDonald's")
hamburger.addNodeConnectionFromTo("2 Burger King","3 Wendy's")
hamburger.addNodeConnectionFromTo("3 Wendy's","1 McDonald's")
hamburger.addNodeConnectionFromTo("3 Wendy's","2 Burger King")


#alternative nodes connect to all nodes in all other clusters
hamburger.addNodeConnectionFromAllNodesToAllNodesOfCluster("1 Alternatives","2 Advertising")
hamburger.addNodeConnectionFromAllNodesToAllNodesOfCluster("1 Alternatives","3 Quality of Food")
hamburger.addNodeConnectionFromAllNodesToAllNodesOfCluster("1 Alternatives","4 Other")

#Nodes in 2 Adversiting connect to
hamburger.addNodeConnectionFromAllNodesToAllNodesOfCluster("2 Advertising","1 Alternatives")
hamburger.addNodeConnectionFromTo("1 Creativity","2 Promotion")
hamburger.addNodeConnectionFromTo("1 Creativity","3 Frequency")
hamburger.addNodeConnectionFromTo("1 Creativity","2 Location")
hamburger.addNodeConnectionFromTo("1 Creativity","6 Menu Item")
hamburger.addNodeConnectionFromTo("1 Creativity","8 Reputation")

hamburger.addNodeConnectionFromTo("2 Promotion","2 Promotion")
hamburger.addNodeConnectionFromTo("2 Promotion","3 Frequency")
hamburger.addNodeConnectionFromTo("2 Promotion","1 Price")
hamburger.addNodeConnectionFromTo("2 Promotion","6 Menu Item")

hamburger.addNodeConnectionFromTo("3 Frequency","2 Promotion")
hamburger.addNodeConnectionFromTo("3 Frequency","1 Creativity")
hamburger.addNodeConnectionFromTo("3 Frequency","2 Location")
hamburger.addNodeConnectionFromTo("3 Frequency","6 Menu Item")
hamburger.addNodeConnectionFromTo("3 Frequency","8 Reputation")

#Nodes in 3 Quality of Food connect to
hamburger.addNodeConnectionFromAllNodesToAllNodesOfCluster("3 Quality of Food","1 Alternatives")
hamburger.addNodeConnectionFromTo("3 Portion","1 Price")
hamburger.addNodeConnectionFromTo("3 Portion","7 Take-out")

#price node connect alternatives and ..
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("1 Price","1 Alternatives")

hamburger.addNodeConnectionFromTo("1 Price","2 Promotion")
hamburger.addNodeConnectionFromTo("1 Price","3 Frequency")
hamburger.addNodeConnectionFromTo("1 Price","1 Nutrition")
hamburger.addNodeConnectionFromTo("1 Price","3 Portion")
hamburger.addNodeConnectionFromTo("1 Price","2 Location")
hamburger.addNodeConnectionFromTo("1 Price","7 Take-out")

#location node connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("2 Location","1 Alternatives")

#3 Service connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("3 Service","1 Alternatives" )
hamburger.addNodeConnectionFromTo("3 Service","2 Location" )
hamburger.addNodeConnectionFromTo("3 Service","4 Speed" )
hamburger.addNodeConnectionFromTo("3 Service","5 Cleanliness" )
hamburger.addNodeConnectionFromTo("3 Service","8 Reputation" )

#4 Speed connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("4 Speed","1 Alternatives" )
hamburger.addNodeConnectionFromTo("4 Speed","3 Service" )
hamburger.addNodeConnectionFromTo("4 Speed","7 Take-out" )
hamburger.addNodeConnectionFromTo("4 Speed","8 Reputation" )

#5 Cleanliness connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("5 Cleanliness","1 Alternatives" )
hamburger.addNodeConnectionFromTo("5 Cleanliness","3 Service" )
hamburger.addNodeConnectionFromTo("5 Cleanliness","2 Location" )
hamburger.addNodeConnectionFromTo("5 Cleanliness","4 Speed" )

#6 Menu Item connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("6 Menu Item","1 Alternatives" )
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("6 Menu Item","2 Advertising" )
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("6 Menu Item","3 Quality of Food" )
hamburger.addNodeConnectionFromTo("6 Menu Item","1 Price" )
hamburger.addNodeConnectionFromTo("6 Menu Item","2 Location" )
hamburger.addNodeConnectionFromTo("6 Menu Item","4 Speed" )
hamburger.addNodeConnectionFromTo("6 Menu Item","5 Cleanliness" )

#7 Take-out connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("7 Take-out","1 Alternatives" )
hamburger.addNodeConnectionFromTo("7 Take-out","3 Service" )
hamburger.addNodeConnectionFromTo("7 Take-out","2 Location" )
hamburger.addNodeConnectionFromTo("7 Take-out","4 Speed" )

#8 Reputation connects to
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("8 Reputation","1 Alternatives" )
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("8 Reputation","2 Advertising" )
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("8 Reputation","3 Quality of Food" )
hamburger.addNodeConnectionFromNodeToAllNodesOfCluster("8 Reputation","4 Other" )

# Excel questionnaire
input.export4ExcelQuestFull(hamburger,"HamburgerModel_Excel_empty.xlsx",False)

#Import Excel with filledin questionnaire, calculate results and export to Excel file
calc.calcAHPMatricesSave2File(hamburger,"HamburgerModel_Excel_filledIn.xlsx","HamburgerModel_Excel_results.xlsx",True,False,True,False)


