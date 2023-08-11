#dialog and images for the intro scene for the demo.
label introScene:

n "Here is how the character names look on the screen"
d "this is mine"
a "and mine"
l "well I suppose so"

show bg page_floor

n "As Deanna came to, she first sensed the rainforest\’\s song of chirping crickets and chattering cicadas. "

show deanna_sleepForest at deanna_forestTransform

n "The air, perfumed with rich earth and tropical flowers,"

n "suppressed the forest floor with heavy humidity."

hide deanna_sleepForest


show deanna forest blinks at deanna_forestTransform

n "Deanna finally awoke among the ruins of what was left of their getaway wagon." 
 
n  "She immediately realized something amiss."


n "Her friends weren\’t with her\!​"

n "Deana listened for any signs of her friends…​"

hide deanna forest blinks

show bg page_4

show deanna_calling_out at left

d "“Lethabo! Athos! Where are you?”"

#return to the script.rpy to end the game.
jump finish