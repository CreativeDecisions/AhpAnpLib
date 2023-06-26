from AhpAnpLib import structs_AHPLib as str

myNode=str.Node("my node",0) 
print('my node before updating: ',myNode)

myNode.updateN_DisplayOrder(2)
print('my node after updating: ',myNode)