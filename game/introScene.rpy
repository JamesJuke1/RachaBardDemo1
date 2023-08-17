#dialog and images for the intro scene for the demo.
label introScene:

init:
    $flash = Fade(.5, 0, .75, color="#fff")
    $flashDelay = Fade(.1, 0,  .1, color="#000")
    $speedFlash = Fade(.01, .01, .01, color="#fff")


show bg page_intro with flash 

#beginning scene the show forest tree tops then
#scrolls to show Deanna asleep near a crashed wagon
#show bg page_intro with flashDelay
#hide bg page_intro with speedFlash  
#show bg page_intro with flashDelay
n "As Deanna came to, she first sensed the rainforest\’\s song of chirping crickets and chattering cicadas. " with dissolve

show bg intro_scroll_down with pushup

n "The air, perfumed with rich earth and tropical flowers,"

n "suppressed the forest floor with heavy humidity."

show bg intro_scroll_down

hide deanna forest blinks with dissolve

call deannaAlertWakeup

#return to the script.rpy to end the game.

jump finish