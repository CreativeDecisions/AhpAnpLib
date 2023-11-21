from AhpAnpLib import calcs_AHPLib as calc
inputFile = "Exp102_Excel_1.xlsx"
outputFile = "Exp102_Excel_2output with extras.xlsx"
outputFile2 = "Exp102_Excel_2output matrix.xlsx"
calc.copyExcelSheet(inputFile, outputFile, "pairwiseM1")
calc.copyExcelSheet(inputFile, outputFile2, "pairwiseM1",False)