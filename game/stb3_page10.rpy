#storybook 3 page 10

label stb3_page10:
scene bg stb3_page 10
pause 1.0
show atho_page10 with speedFlash
#these images need to be flipped as of 11/10/23 10 AM
show leth_page10 with Pause(0.25)
show deanna_page10 with easeinleft
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d17_v1.mp3'
n "But there was no time for debate. Athos threw Deanna clear over the chasm against her will."
stop sound 
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d18_v1.mp3'
n "The gravity twisted around her, confusing her briefly before she managed to buzz her wings and take flight."
pause 2.0
stop sound
call stb3_page11 from _call_stb3_page11