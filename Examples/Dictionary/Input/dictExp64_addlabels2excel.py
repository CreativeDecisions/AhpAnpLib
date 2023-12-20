from AhpAnpLib import inputs_AHPLib as input

rowheading = ["a","b","c","d"]
columnheading = ["x","y","z"]
input.addLabels2Excel(rowheading,"dictExp64_addLabels2excel.xlsx","Sheet1",2,1,0)
input.addLabels2Excel(columnheading,"dictExp64_addLabels2excel.xlsx","Sheet1",1,2,1)