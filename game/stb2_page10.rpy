#stroybook 2 page 10

label stb2_page10:
scene bg_stb2_page10 with fade

show stb2_page10_atho_letho1
show stb2_page10_d_1
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p10_d1.mp3'
d "There's  wisps nearby!"

window hide
pause 0.5
hide stb2_page10_d_1 with dissolve
pause 0.5
show deanna_fly_off
show stb2_page10_atho_letho2 with dissolve
pause 0.5
hide deanna_fly_off
hide athos_letho_final_upright
pause 0.5
play sound '/audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d14_v2.mp3'
n "Off Deanna flew! She soarded through the branches and vines, following the enchancted wishpers without a second thought."
window hide
pause 0.5


scene bg_stb2_page11 with dissolve
pause 0.5

show stb2_page11_d
pause 0.25
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d15_v3.mp3'
n  "Deanna pushed herself thorugh layers of foliage until, finally, she discovered an oh-so magical sight\n that had her go starry-eyed."
window hide
stop sound
hide stb2_page11_d with dissolve
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p11_d1.mp3'
d "{i}Ya-ho! {/i}Look ath this, everyone!"
window hide
stop sound
pause 0.5

show stb2_page11_athos_letho
show stb2_page11_d
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d16_v2.mp3'
n "Lethabo and Athos bumbled through the branches before being stopped in their tracks,\n their jaws dropping to the ground."
window hide
stop sound
pause 0.5
scene bg_stb2_page12 with pixellate
scene bg_stb2_page12 with dissolve
pause 5
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d17_v2.mp3'
n "What a sight! They found Aesop wisps all right, a whole flock of them surrounding some old, \nforgotten ruins on the forest floor!"
window hide
stop sound 
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Deanna Storybook 2/Deanna_SB2_p12_d1.mp3'
d "This is great! We're sure to find a hero's story here somewhere! Let's go in!"
window hide
stop sound 
pause 0.5

call stb3_page1 from _call_stb3_page1




