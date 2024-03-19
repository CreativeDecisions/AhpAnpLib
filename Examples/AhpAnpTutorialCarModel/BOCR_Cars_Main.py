from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate

#create the main model
BOCR_Cars=str.Model("Hertz EV vs ICE")

#import structure of the main model
input.readStructFromExcel(BOCR_Cars,"BOCR_Cars.xlsx","Strategic",False)

#import connections of the main model
input.readConnectionsFromExcel(BOCR_Cars,"BOCR_Cars.xlsx","StrategicConnections",False)

BOCR_Cars.printStruct()
BOCR_Cars.drawGraphModel()

#set the model type to be ratings
BOCR_Cars.setModelTypeRatings()

#add ratings criteria
BOCR_Cars.rateModel.addCriteriaByName("Sustainability","Financial Viability","Customer Experience","Technological Innovation","Market Competitiveness")

#add ratings alternatives
BOCR_Cars.rateModel.addAlternativesByName("Benefits","Opportunities","Costs","Risks")

#ratings scales
scale1 = rate.RatScale("HML")
scale1.defineScaleByValue(None,False,
                          ["High",65],["Medium",25],["Low",10])
BOCR_Cars.rateModel.addScaleByVar(scale1)
BOCR_Cars.rateModel.assignScale2CriterionByName("Sustainability","HML")
BOCR_Cars.rateModel.assignScale2CriterionByName("Technological Innovation","HML")

scale2=rate.RatScale("Financial Viability Scale")
scale2.defineScaleByValue(None,False,["High",65],["Medium",25],["Low",10])
BOCR_Cars.rateModel.addScaleByVar(scale2)
BOCR_Cars.rateModel.assignScale2CriterionByName("Financial Viability","Financial Viability Scale")

scale3=rate.RatScale("Excellent2Poor")
scale3.defineScaleByValue(None,False,["Excellent",1],["Above Average",0.8],["Average",0.6],["Below Average",0.4],["Poor",0.3])
BOCR_Cars.rateModel.addScaleByVar(scale3)
BOCR_Cars.rateModel.assignScale2CriterionByName("Customer Experience","Excellent2Poor")

scale4=rate.RatScale("HighMedLow")
scale4.defineScaleByValue(None,False,"High","Medium","Low")
BOCR_Cars.rateModel.addScaleByVar(scale4)
BOCR_Cars.rateModel.assignScale2CriterionByName("Market Competitiveness","HighMedLow")

#export Excel questionnaire for strategic criteria priorities
input.export4ExcelQuestFull(BOCR_Cars,"BOCR_Cars_Strategic_empty.xlsx",True,False)  

#
calc.calcAHPMatricesSave2File(BOCR_Cars,"BOCR_Cars_Strategic_filledin.xlsx","BOCR_Cars_Strategic_priorities.xlsx",True,False,True)

#export ratings setup
input.export4ExcelRatingsSetup(BOCR_Cars,"BOCR_Ratings_empty.xlsx",True,False)

input.calcExcelRatings(BOCR_Cars,"BOCR_Ratings_filledin.xlsx","BOCR_Ratings_results.xlsx")
