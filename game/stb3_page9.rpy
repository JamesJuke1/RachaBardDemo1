#storybook 3 page 9 

label stb3_page9:
scene bg stb3_page 9
pause 1.0
show letho_page9 with moveinright
hide letho_page9 with speedFlash
show athos_page9 with moveinleft
show letho_page9 with speedFlash
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d16_v2.mp3'
n "Lethabo went on the defensive with his ladybug shield as Athos edged backwards towards the cursed chasm."
window hide
pause 1.0
stop sound
play sound 'audio/storybook 3/Sounds + Music/Athos Storybook 3/Athos SB3-p21.mp3'
a "Deanna, you can fly. Get far away from here. We’ll distract it!"
window hide 
pause 1.0
stop sound
play sound 'audio/storybook 3/Sounds + Music/Deanna Storybook 3/Deanna_SB3_p9_d1.mp3'
d "What?? I can’t leave you guys!"
window hide
pause 1.0
stop sound
call stb3_page10