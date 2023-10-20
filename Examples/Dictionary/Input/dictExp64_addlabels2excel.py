from AhpAnpLib import inputs_AHPLib as input

columnlabellist = ["a","b","c","d"]
rowlabellist = ["x","y","z"]
input.addLabels2Excel(columnlabellist,"dictExp64_addLabels2excel.xlsx","Sheet1",2,1,0)
input.addLabels2Excel(rowlabellist,"dictExp64_addLabels2excel.xlsx","Sheet1",1,2,1)