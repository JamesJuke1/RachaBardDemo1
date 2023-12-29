#storybook 2  page 8

label stb2_page8:

scene bg_stb2_page8
pause 0.5

show athos_on_ground
pause 0.5
show deanna_glasses_drag with dissolve
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d10_v1.mp3'
n "Athos huffed with annoyance before Deanna dragged in a pair of spectacles."
window hide
stop sound
pause 0.5
hide deanna_glasses_drag
show deanna_glasses_drag2
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p8_d1.mp3'
d "I found your glasses!"
window hide
stop sound
pause 0.5

show athos_on_ground2
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p8_d2.mp3'
d "I am happy to see you're okay!"
window hide
stop sound
pause 0.5

show deanna_glasses_drag2 with dissolve
show athos_on_ground3
play sound 'audio/storybook 2/Sounds + Music/Athos Storybook 2/Athos SB2-p9.mp3'
a "{i}Grazie, topolina.{/i}"
window hide
stop sound
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
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d11_v3.mp3'
n "What a relief! It seems everyone has made it okay from the big crash!\n Though waht are they to do now? Lost in this giant ranforest?"
window hide
stop sound
pause 1.5

call stb2_page9 from _call_stb2_page9



