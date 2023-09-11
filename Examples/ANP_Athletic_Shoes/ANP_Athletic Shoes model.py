# import libraries that we need
from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc

# create the model
Shoesmodel=str.Model("Athletic Shoes model")
# create nodes, clusters
Alternatives=str.Cluster("1. Alternatives",0)
A1=str.Node("Adidas",0)
Alternatives.addNode2Cluster(A1)
A2=str.Node("Nike",1)
Alternatives.addNode2Cluster(A2)
A3=str.Node("Reebok",2)
Alternatives.addNode2Cluster(A3)
Shoesmodel.addCluster2Model(Alternatives)

Advertising=str.Cluster("2. Advertising",1)
brand=str.Node("Brand Image",3)
creativity=str.Node("Creativity",4)
frequncy=str.Node("Frequency",5)
printAd=str.Node("Print Ad.",6)
television=str.Node("Television",7)
Advertising.addMultipleNodes2Cluster(brand,creativity,frequncy,printAd,television)
Shoesmodel.addCluster2Model(Advertising)

Product=str.Cluster("3. Product Characteristics",2)
comfort=str.Node("Comfort",8)
innovation=str.Node("Innovation",9)
productline=str.Node("Product Line",10)
quality=str.Node("Quality",11)
style=str.Node("Style",12)
Product.addMultipleNodes2Cluster(comfort,innovation,productline,quality,style)
Shoesmodel.addMultipleClusters2Model(Product)

Customers=str.Cluster("4. Customers",3)
others=str.Node("Others",13)
professional=str.Node("Professional athletes",14)
students=str.Node("Students",15)
teenagers=str.Node("Teenagers",16)
urbanmale=str.Node("Urban male",17)
Customers.addMultipleNodes2Cluster(others,professional,students,teenagers,urbanmale)
Shoesmodel.addCluster2Model(Customers)

#add connections
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("1. Alternatives","2. Advertising")
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("1. Alternatives","3. Product Characteristics")
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("1. Alternatives","4. Customers")

Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Brand Image","1. Alternatives")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Brand Image","4. Customers")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Creativity","1. Alternatives")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Creativity","3. Product Characteristics")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Creativity","4. Customers")
Shoesmodel.addNodeConnectionFromTo("Creativity","Television",False)
Shoesmodel.addNodeConnectionFromTo("Creativity","Print Ad.",False)
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Frequency","1. Alternatives")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Frequency","4. Customers")
Shoesmodel.addNodeConnectionFromTo("Frequency","Television",False)
Shoesmodel.addNodeConnectionFromTo("Frequency","Print Ad.",False)

Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Print Ad.","1. Alternatives")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Print Ad.","3. Product Characteristics")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Print Ad.","4. Customers")
Shoesmodel.addNodeConnectionFromTo("Print Ad.","Creativity",False)
Shoesmodel.addNodeConnectionFromTo("Print Ad.","Frequency",False)

Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Television","1. Alternatives")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Television.","3. Product Characteristics")
Shoesmodel.addNodeConnectionFromNodeToAllNodesOfCluster("Television","4. Customers")
Shoesmodel.addNodeConnectionFromTo("Television","Creativity",False)
Shoesmodel.addNodeConnectionFromTo("Television","Frequency",False)

Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3. Product Characteristics","1. Alternatives")
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("3. Product Characteristics","4. Customers")

Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4. Customers","1. Alternatives")
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4. Customers","2. Advertising")
Shoesmodel.addNodeConnectionFromAllNodesToAllNodesOfCluster("4. Customers","3. Product Characteristics")

#professional athelets and students are not connected to Production line
Shoesmodel.remNodeConnectionFromTo("Professional athletes","Product Line")
Shoesmodel.remNodeConnectionFromTo("Students","Product Line")
#urban male is not connected to Production line and Comfort
Shoesmodel.remNodeConnectionFromTo("Urban male","Comfort")
Shoesmodel.remNodeConnectionFromTo("Urban male","Product Line")

#export questionnaires
input.export4ExcelQuestFull(Shoesmodel,"Athletic Shoes model_empty.xlsx",verb=False)
#calc.calcAHPMatricesSave2File(Shoesmodel,"Athletic Shoes model_filledIn.xlsx","Athletic Shoes model_results.xlsx",inputFileUse=True,normalbar=False,idealbar=True,verbal=False)