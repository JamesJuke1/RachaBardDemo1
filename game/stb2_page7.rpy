
label stb2_page7:

scene bg_stb2_page6
pause 0.5
show stb2_d_look_1_page6  with vpunch
window hide 
pause 0.5
show stb2_d_look_2_page6 with dissolve
hide stb2_d_look_1_page6
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Sound FX/Story Book 2-Twig Snap.mp3'
n "Athos tumbles back to solid ground"
window hide 
stop sound
scene bg_stb2_page7
pause 0.5
show stb2_d_look_3_page6
pause 1.0

call stb2_page8