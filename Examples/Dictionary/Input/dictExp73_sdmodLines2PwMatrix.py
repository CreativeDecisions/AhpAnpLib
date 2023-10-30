from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str

with open("Exp73_CarModel.sdmod", 'r') as file:
        file_contents = file.read()
raw_lines = file_contents.split('\n')
my_model= str.Model("Example 73 Car Model")
input.sdmodLines2PwMatrix (my_model,raw_lines,218,False,True)