from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import functions_AHPLib as reqLib

workbook = reqLib.openpyxl.load_workbook("Exp79_Excel_addDropDown2Excel.xlsx")
workbook.active = workbook.sheetnames.index("Sheet2")
worksheet = workbook.active

worksheet=input.addDropDown2ExcelCell(worksheet,"B2","B5","Sheet1","B2")
workbook.save("Exp79_Excel_addDropDown2Excel.xlsx")