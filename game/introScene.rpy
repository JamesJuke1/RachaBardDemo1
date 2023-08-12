#dialog and images for the intro scene for the demo.
label introScene:
show bg page_intro with blinds 
#beginning scene the show forest tree tops then
#scrolls to show Deanna asleep near a crashed wagon

n "As Deanna came to, she first sensed the rainforest\’\s song of chirping crickets and chattering cicadas. "

show bg intro_scroll_down with pushup

show deanna_sleepForest at deanna_forestTransform

n "The air, perfumed with rich earth and tropical flowers,"

n "suppressed the forest floor with heavy humidity."

hide deanna_sleepForest

show deanna forest blinks at deanna_forestTransform

n "Deanna finally awoke among the ruins of what was left of their getaway wagon." 
 
n  "She immediately realized something amiss."

hide deanna forest blinks with dissolve

call deannaAlertWakeup

#return to the script.rpy to end the game.

jump finish