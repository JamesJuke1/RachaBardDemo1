#storybook 3 page 1

label stb3_page1:

scene bg_stb3_page1
show strb3_deanna_kneel_before_alert with dissolve
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d1_v3.mp3'
n "Deanna pondered the Aesop's tale."
pause 1.0
window hide
stop sound
pause 2.0
show stb3_page1_darkened with dissolve
pause 1.0
pause 0.5
window hide
pause 0.5
hide strb3_deanna_kneel_before_alert with speedDissolve
show stb3_deanna_kneel_floor with speedDissolve
pause 1.0
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d2_v1.mp3'
n "Suddenly Deanna sensed evil magic-{i}yellow{/i} magic." 
pause 0.5
window hide
stop sound
pause 0.5
show  stb3_page1_smeared_fall_down
pause 1.0
show stb3_deanna_kneel_floor_2

hide stb3_deanna_kneel_floor with dissolve 
pause 5.2
scene bg stb3_page 1
pause 1.0
call stb3_page2 from _call_stb3_page2 