#storybook 1 page 5 slide 4

label stb1_page5:

scene bg_stb1_page5
pause 2.0
play sound 'audio/storybook 1/Music _ Sounds/Narrator Dialogues/Narrator-SB1_d8_v2.mp3'
n "Further down the hill, Deanna beheld a stretch of entangling vines and wild grass."
window hide
pause 0.5
stop sound
pause 0.5
show stb1_deanna_worried at deanna_worried_left
pause 1.0
play sound 'audio/storybook 1/Music _ Sounds/Deanna Dialogues/Deanna Storybook 1/Deanna_SB1_p5_d1.mp3'
d "“L-Lethabo? Athos? Is th-that you?”"
pause 0.25
stop sound
pause 0.25
hide stb1_deanna_worried with dissolve
window hide
pause 0.5
stop sound
play sound 'audio/storybook 1/Music _ Sounds/Narrator Dialogues/Narrator-SB1_d9_v1.mp3'
n "Deanna had no choice but to investigate. Her friends could be in trouble!"
pause 0.25
stop sound
stop music
call stb2_page1 from _call_stb2_page1