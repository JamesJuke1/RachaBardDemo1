#storybook 3 page 15

label stb3_page15:
scene bg stb3_page 15
show smearedFight
pause 1.0
show leth_atho_smearedWin
pause 0.5
show deannaStandTall_smearedFight with dissolve
pause 0.5
show deannaShieldMagic with speedFlash
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d28_v2.mp3'
n_second "Deanna pushed the Smeared back with a magical shield of Aesop! "
window hide
pause 1.0
stop sound
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d29_v3.mp3'
n_second "Lethabo and Athos dropped their jaws at the sight of her hidden might. The Smeared showed a split second of morbid fear!"
window hide
pause 1.0
stop sound
call stb3_page16 from _call_stb3_page16