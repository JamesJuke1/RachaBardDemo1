#storybook 3 page 3

label stb3_page3:
scene bg stb3_page 3

show athos_let_grab_deanna
pause 1.0
show smearerd_chase
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d5_v3.mp3'
n "Athos held dear to Deanna as he and Lethabo higtailed out of there"
window hide
stop sound
play sound 'audio/storybook 3/Sounds + Music/Athos Storybook 3/Athos SB3-p19.mp3'
a "How did that demon find us so quickly?!"
window hide
stop sound
pause 1.0
play sound 'audio/storybook 3/Sounds + Music/Deanna Storybook 3/Deanna_SB3_p3_d1.mp3' volume 0.5
d "It must have sensed my magic. I'm so sorry!"
window hide
stop sound
play sound 'audio/stroybook 3/Sounds + Music/The Smeared/Smeared Scream 4.mp3'
play sound 'audio/storybook 3/Sounds + Music/Lethabo Storybook 3/Lethabo_SB3_p3_d1.mp3'
l "No matter! We must head for sunlight. They can't stand it!"
window hide
stop sound
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d6_v2.mp3'
n "As they ran, the Smeared monster grates out a horrific, ear-piercing roar that shook even the leaves themselves."
stop sound
play sound 'audio/storybook 3/Sounds + Music/Sound FX/The Smeared/Smeared (Scared).mp3' volume 1.5
pause 0.5
stop sound
play sound 'audio/storybook 3/Sounds + Music/Sound FX/The Smeared/Smeared Growl (Long).mp3'
pause 2.0
stop sound
pause 0.5
call stb3_page4 from _call_stb3_page4
