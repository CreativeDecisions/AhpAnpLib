from AhpAnpLib import ratings_AHPLib as rate
#create scale
scale1=rate.RatScale("ExampleScale1")
scale2=rate.RatScale("ExampleScale2")
scale1.defineScaleByValue(None,True,
["High", 90],
["Medium",60], 
["Low",30]
)
scale2.defineScaleByValue(None,True,
"Excellent","Good","Poor"
)