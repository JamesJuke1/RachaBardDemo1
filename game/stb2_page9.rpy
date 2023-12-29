#storybook 2 page 9

label stb2_page9:
scene bg_stb2_page9
show stb2_page9_d_1
show deanna_magic_sense
window hide
pause 3.0
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d12_v1.mp3'
n "Right then! Deanna sensed magic!"
window hide
stop sound
pause 2.0
hide deanna_magic_sense


show stb2_page9_d_2
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p10_d1.mp3'
d "Aesop is nearby! And there's a whole lot of them!"
window hide
stop sound
pause 2.0

call stb2_page10 from _call_stb2_page10
