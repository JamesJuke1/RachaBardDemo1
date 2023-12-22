#storybook 2  page 8

label stb2_page8:

scene bg_stb2_page8
pause 0.5

show athos_on_ground
pause 0.5
show deanna_glasses_drag with dissolve
pause 0.5
n "Athos huffed with annoyance before Deanna dragged in a pair of spectacles."
window hide
pause 0.5
hide deanna_glasses_drag
show deanna_glasses_drag2
d "I found your glasses!"
window hide
pause 0.5

show athos_on_ground2
d "I am happy to see you're okay!"
window hide
pause 0.5

show deanna_glasses_drag2 with dissolve
show athos_on_ground3
a "{i}Grazie, topolina.{/i}"
window hide
pause 0.5
hide deanna_glasses_drag2 with dissolve
pause 0.5
show deanna_glasses_drag3
pause 1.0
show athos_on_ground4
pause 0.5
hide athos_on_ground
hide athos_on_ground2
pause 0.5
hide athos_on_ground3
hide deanna_glasses_drag3
hide athos_on_ground4
hide athos_on_ground3
n "What a relief! It seems everyone has made it okay from the big crash!\n Though waht are they to do now? Lost in this giant ranforest?"
window hide
pause 1.5

call stb2_page9



