from AhpAnpLib import ratings_AHPLib as rate
#create scale
scale1=rate.RatScale("ExampleScale")
print(scale1)

scale1.defineScaleByValue(None,False,
["More than 30 K", 51],
["Between 25K and 30K",100], 
["Between 20K and 25K",39],
["Less than 20K",9]
)
print(scale1.val_mat)