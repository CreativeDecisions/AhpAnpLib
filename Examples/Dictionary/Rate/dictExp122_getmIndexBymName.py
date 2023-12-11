from AhpAnpLib import ratings_AHPLib as rate
#create scale
scale=rate.RatScale("ExampleScale")
scale.defineScaleByValue(None,False,
["High", 90],
["Medium",60], 
["Low",30]
)

indexofHigh = scale.getmIndexBymName("High")
print("index of High value in the scale: ",indexofHigh)
indexofLow = scale.getmIndexBymName("Low",True)
print("index of Low value in the scale: ",indexofLow)
