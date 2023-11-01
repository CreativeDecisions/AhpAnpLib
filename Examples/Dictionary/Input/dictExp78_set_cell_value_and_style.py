from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import functions_AHPLib as reqLib

workbook = reqLib.openpyxl.load_workbook("Exp78_Excel_set cell values.xlsx")
workbook.active = workbook.sheetnames.index("Sheet1")
worksheet = workbook.active

row=2
col=2

fill = reqLib.PatternFill(start_color="accbe8", end_color="accbe8", fill_type="solid")
border = reqLib.Border(left=reqLib.Side(style='thin'), right=reqLib.Side(style='thin'), top=reqLib.Side(style='thin'), bottom=reqLib.Side(style='thin'))
font_color = "ff0000"
input.set_cell_value_and_style(worksheet.cell(row,col),"Exp78",fill,border,font_color, True)
input.set_cell_value_and_style(worksheet.cell(row+1,col+1),"Python")
workbook.save("Exp78_Excel_set cell values.xlsx")