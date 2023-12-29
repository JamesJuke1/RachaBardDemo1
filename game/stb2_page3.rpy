#storybook 2 page 3

label stb2_page3:
scene bg_stb2_page3 with speedFlash
show stb2_page4_scarry_figure1 with speedFlash
pause 0.3
show stb2_page4_scarry_figure2 with hpunch
pause 0.3
show stb2_page4_scarry_figure2 with hpunch
show stb2_d_screaming at deanna_worried_left
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p1_d1.mp3'
d "“Aaaaaaaaaaaah!”"
window hide
stop sound
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d5_v3.mp3'
n "A monster! A monster spotted her!"
window hide
stop sound
pause 0.5
call stb2_page4 from _call_stb2_page4