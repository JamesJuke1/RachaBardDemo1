#storybook 3 page 13

label stb3_page13:
scene bg stb3_page 13
pause 2.0

show deanna_getsAngry_page13
pause 1.5
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d23_v1.mp3'
n "Deanna hovered, hesitant. Yes, she had a duty as a bard to usher in world peace with the hero’s story, 
but could she really leave behind her friends? The only two animals in the world who accepted her as she was?"
window hide
hide deanna_getsAngry_page13 with dissolve
stop sound
show stb3_page 13_bg zoom in
pause 0.5
show deanna_getsAngry_page13_2
pause 0.5
window hide
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d24_v3.mp3'
n "No. No she would not. She ran away so many times before, but not today! Her friends need help!"
window hide
pause 1.0
stop sound
hide deanna_getsAngry_page13_2 with dissolve
show deanna_getsAngry_page13_3
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d25_v4.mp3'
n "Aesop magic pulsed inside Deanna like a beating heart. Her eyes glowed teal as she sung a poem. 
One of the tokens of her necklace began to radiate, when finally, she summons forth…."
window hide
pause 0.5
stop sound
show deanna_lyre_page13 with dissolve
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d26_v3.mp3'
n "…a golden lyre!"
pause 0.5
stop sound
call stb3_page14 from _call_stb3_page14