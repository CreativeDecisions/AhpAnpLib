from AhpAnpLib import ratings_AHPLib as rate
#create scale
scale=rate.RatScale("ExampleScale")
scale.defineScaleByValue(None,False,
["High", 90],
["Medium",60], 
["Low",30]
)

indexofHigh = scale.getmValueBymName("High")
print("value of High in the scale: ",indexofHigh)
indexofLow = scale.getmValueBymName("Low",True)
print("value of Low in the scale: ",indexofLow)
