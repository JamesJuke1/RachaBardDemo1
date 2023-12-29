#dialog and images for the intro scene for the demo.
label intro_scene:


show bg page_intro with flash:

#beginning scene the show forest tree tops then
#scrolls to show Deanna asleep near a crashed wagon
#show bg page_intro with flashDelay
#hide bg page_intro with speedFlash  
#show bg page_intro with flashDelay
pause 0.5
n "As Deanna came to, she first sensed the rainforest\’\s song of chirping crickets and chattering cicadas. " with dissolve
window hide
window hide
pause 0.5
scene bg intro_scroll_down with pushup
pause 0.5
"The air, perfumed with rich earth and tropical flowers, \n suppressed the forest floor with heavy humidity."
window hide
pause 0.5
window hide
pause 0.5
window hide
pause 0.5
scene bg intro_scroll_down
pause 0.5

show deanna forest blinks at deanna_forestTransform

scene bg deanna_wakeup with zoomin

call deannaAlertWakeup from _call_deannaAlertWakeup