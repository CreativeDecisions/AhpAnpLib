from AhpAnpLib import inputs_AHPLib as input
from AhpAnpLib import structs_AHPLib as str
from AhpAnpLib import calcs_AHPLib as calc
from AhpAnpLib import ratings_AHPLib as rate 

#When structuring objects assign a "name" and number in the parens:("name",#)
#When adding objects to other objects use the Var in the ()
#Best to preface cluster variables with CL

#Create the model
Economy2008=str.Model("Economy2008") 

#Create nodes for the Primary Factors
nAggDemand=str.Node("Agg Demand",1)
nAggSupply=str.Node("Agg Supply",2)
nGlobalFinancial=str.Node("Global Financial",3)
#Create a cluster to contain the primary factor nodes
CLPrimaryFactors=str.Cluster("Primary Factors",1)
#Add nodes to Primary Factors cluster (when adding objects use Var, not "name")
CLPrimaryFactors.addMultipleNodes2Cluster(nAggDemand,nAggSupply,nGlobalFinancial)
#Add cluster to model (when adding objects to an object use Var, not "names")
Economy2008.addCluster2Model(CLPrimaryFactors)

#Create aggregate demand factors (nodes)- make up "name" and include a number
nConsumption=str.Node("Consumption",1)
nExports=str.Node("Exports",2)
nInvestment=str.Node("Investment",3)
nConfidence=str.Node("Confidence",4)
nFiscalPolicy=str.Node("Fiscal Policy",5)
nMonetaryPolicy=str.Node("Monetary Policy",6)
nExpectedInflation=str.Node("Expected Inflation",7)
#Create an aggregate demand cluster (when structuring use "name" in parens)
CLAggregateDemandFactors=str.Cluster("Aggregate Demand",2)
#Add nodes (factors) to the aggregate demand cluster (use  Var not "name")
CLAggregateDemandFactors.addMultipleNodes2Cluster(nConsumption,nExports,nInvestment,nConfidence,nFiscalPolicy,nMonetaryPolicy,nExpectedInflation)
#Add aggregate demand factors cluster to model
Economy2008.addCluster2Model(CLAggregateDemandFactors)

#Create nodes for Fiscal Policy subfactors
nTaxPolicy=str.Node("Tax Policy", 1)
nGovtExpenditure=str.Node("Govt Expenditure",2)
#Create a fiscal policy cluster to contain the nodes 
CLFiscalPolicyIssues=str.Cluster("Fiscal Policy Issues",3)
#Add fiscal policy factors (nodes), using Var
CLFiscalPolicyIssues.addMultipleNodes2Cluster(nTaxPolicy,nGovtExpenditure)
#Add cluster to model (using Var, not "name")
Economy2008.addCluster2Model(CLFiscalPolicyIssues)

#Create the nodes (factors) for Aggregate Supply
nLaborCost=str.Node("Labor Cost",1)
nNaturalResourceCost=str.Node("Resource Cost",2)
nExpectations=str.Node("Expectations",3)
#Create an aggregate supply cluster to contain the factors
CLAggregateSupplyFactors=str.Cluster("Aggregate Supply",4)
#Add nodes to Aggregate Supply cluster
CLAggregateSupplyFactors.addMultipleNodes2Cluster(nLaborCost,nNaturalResourceCost,nExpectations)
#Add Aggregate Supply Factor cluster to model (use Var)
Economy2008.addCluster2Model(CLAggregateSupplyFactors)

#Create Nodes for Global Financial Contexts cluster
nInternationalRelations=str.Node("International Relations",1)
nGlobalFinancialIntegration=str.Node("Financial Integration",2)
nMortgageCrisis=str.Node("Mortgage Crisis",3)
nExpectationsOilPrices=str.Node("Oil Prices",4)
nFutureDollarValue=str.Node("Future Dollar",5)
#Create Cluster for Global Financial Context nodes and name it
CLGlobalFinancialContexts=str.Cluster("Global Financial",5)
#Add nodes to Global Financial cluster using Var
CLGlobalFinancialContexts.addMultipleNodes2Cluster(nInternationalRelations,nGlobalFinancialIntegration,nMortgageCrisis,nExpectationsOilPrices,nFutureDollarValue)
#Add Global Financial cluster to model using var
Economy2008.addCluster2Model(CLGlobalFinancialContexts)

#Create Nodes for Mortgage Crisis cluster
nUncertaintyHousingPrices=str.Node("Housing Prices",1)
nUncertaintyMortgageBackedSecurities=str.Node("Mortgage-backed Securities",2)
nCreditDefaultSwaps=str.Node("Credit Default Swaps",3)
nGovtIntervention=str.Node("Govt Intervention",4)
nFinancialReporting=str.Node("Financial Reporting",5)
#Create cluster for Mortgage Crisis nodes
CLMortgageCrisisIssues=str.Cluster("Mortgage Crisis Issues",6)
CLMortgageCrisisIssues.addMultipleNodes2Cluster(nUncertaintyHousingPrices,nUncertaintyMortgageBackedSecurities,nCreditDefaultSwaps,nGovtIntervention,nFinancialReporting)
#Add cluster to model using Var
Economy2008.addCluster2Model(CLMortgageCrisisIssues)

#Create Alternative Nodes
nSixMonths=str.Node("Six Months",1)
nTwelveMonths=str.Node("Twelve Months",2)
nTwentyfourMonths=str.Node("Twentyfour Months",3)
nThirtysixMonths=str.Node("Thirtysix Months",4)
#Create Alternative cluster with "name" and number
CLAlternatives=str.Cluster("Alternatives",7)
#Add nodes to cluster using Var
CLAlternatives.addMultipleNodes2Cluster(nSixMonths,nTwelveMonths,nTwentyfourMonths,nThirtysixMonths)
#Add cluster to model using Var
Economy2008.addCluster2Model(CLAlternatives)

#Make connections for upper level nodes that connect to all nodes of another cluster
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Agg Demand",CLAggregateDemandFactors.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Agg Supply",CLAggregateSupplyFactors.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Global Financial",CLGlobalFinancialContexts.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Fiscal Policy",CLFiscalPolicyIssues.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Mortgage Crisis",CLMortgageCrisisIssues.name)

#Make connections from nodes in Aggregate Demand nodes that go to alternatives
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Consumption",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Exports",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Investment",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Confidence",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Monetary Policy",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Expected Inflation",CLAlternatives.name)

Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Tax Policy",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Govt Expenditure",CLAlternatives.name)


#Make connections from Global Financial Contexts nodes down to Alts
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("International Relations",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Financial Integration",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Oil Prices",CLAlternatives.name)
Economy2008.addNodeConnectionFromNodeToAllNodesOfCluster("Future Dollar",CLAlternatives.name)

#Make connections from Aggregate Supply nodes to alternatives
Economy2008.addNodeConnectionFromAllNodesToAllNodesOfCluster (CLAggregateSupplyFactors.name,CLAlternatives.name)
Economy2008.addNodeConnectionFromAllNodesToAllNodesOfCluster(CLMortgageCrisisIssues.name,CLAlternatives.name)

#Make connections back from Alternatives to Primary Factors
Economy2008.addNodeConnectionFromAllNodesToAllNodesOfCluster(CLAlternatives.name,CLPrimaryFactors.name)

#Export Questionnaire for judgments
input.export4ExcelQuestFull(Economy2008,"Economy2008_empty.xlsx")
Economy2008.drawGraphModel()
Economy2008.printStruct()



