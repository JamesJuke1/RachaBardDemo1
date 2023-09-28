#storybook 3 page 2

label stb3_page2:
scene bg_stb3_page_2
n "start stb3_page2"

show stb3_smeared_charge #this likely needs to be an animation

show stb3_deanna_scarred
pause 5.0
n ""
show stb3_page 2_spear
pause 5.0
n ""
hide stb3_page 2_spear with speedDissolve
hide stb3_smeared_charge
show stb3_smeared_spear_jump
show stb3_page 2_spear with speedDissolve
n ""
show stb3_deanna_spear_scarred
hide stb3_deanna_scarred
pause 1.0
show stb3_page 2_blur swipe
hide stb3_smeared_spear_jump
hide stb3_deanna_spear_scarred
show stb3_blue_swoop with speedDissolve
hide stb3_blue_swoop with speedFlash
show stb3_page2_smear_jump_spear
show stb3_blue_swoop with speedDissolve
pause 5.0


pause 1.0
pause 1.0
n "end stb3_page2"
call stb3_page3