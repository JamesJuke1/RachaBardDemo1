#storybook 3 page 16

label stb3_page16:
scene bg stb3_page 16
pause 1.0
show shieldSplinter
pause 1.0
show smearedAttacking with easeinright
pause 1.0
show shieldSplinterSmearedAttack
hide smearedAttacking with dissolve
hide shieldSplinter
hide shieldSplinterSmearedAttack
show smearedAttack with speedFlash
show shieldSplinterSmearedAttack2 with speedFlash
pause 1.0
play sound 'audio/storybook 3/Sounds + Music/Narrator Dialogues/Narrator-SB3_d30_v3.mp3'
n_second "But the Smeared fought back! Despite Deanna’s magic sizzling its body, the monster  pushed against her shield with yellow magic—making it crack!"
window hide
pause 1.0
stop sound
call stb3_page17 from _call_stb3_page17