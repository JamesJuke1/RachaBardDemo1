#storybook 3 page 18

label stb3_page18:
show stb3_page 18_gray bg
show stb3_page 18_deanna action pop 
pause 1.0
show stb3_page 18_smeared action pop
pause 0.5
show stb3_page 18_white out
hide stb3_page 18_gray bg
pause 1.0
hide stb3_page 18_white out with speedDissolve
pause 0.5
hide stb3_page 18_deanna action pop with dissolve
hide stb3_page 18_smeared action pop with dissolve
scene bg_stb3_page18
pause 1.0
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d37_v1.mp3'
n_second "Her little body burned brighter and brighter with teal light. 
Lethabo and Athos squeezed their eyes shut as they dug in their heels and kept her steady."
window hide
stop sound
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d38_v1.mp3'
n_second "The Smeared’s body chipped away from her power. It tried, oh how it tried to fight back, 
but even its mask was cracking even more from the pressure!"
window hide
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d39_v2.mp3'
n_second 'They pushed and pushed and pushed until... until... until!!!'
window hide
stop sound

n_second "With a small yet mighty cry, Deanna pushed back with all her might"
window hide
stop sound 
play sound 'audio/storybook 3/Sounds + Music/Deanna Storybook 3/Deanna_SB3_p19_d1.mp3'
dSecond "{i}“Yaaaaaaaah!”{/i}"
window hide
pause 1.0
stop sound
call finish from _call_finish