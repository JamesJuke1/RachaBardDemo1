#storybook 3 page 16

label stb3_page16:
scene bg stb3_page 16
n "start stb3_page16"
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
n "end stb3_page16"
call stb3_page17