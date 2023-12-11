from AhpAnpLib import ratings_AHPLib as rate
#create scale
scale1=rate.RatScale("ExampleScale1")
scale2=rate.RatScale("ExampleScale2")
scale3=rate.RatScale("ExampleScale2")
scale1.defineScaleByValue(None,True,
["High", 90],
["Medium",60], 
["Low",30]
)
scale2.defineScaleByValue(None,True,
"Excellent","Good","Poor"
)

scale3.defineScaleByValue([[1,2,3],[0.5,1,1.5],[0.3,0.67,1]],True,
"Below average","Average","Above average"
)