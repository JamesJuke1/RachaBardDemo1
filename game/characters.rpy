#define characters and the animations that they will/may use here
#if scene is called it clears all images that were displayed before.
init:
    $flash = Fade(.5, 0, .75, color="#fff")
    $flashDelay = Fade(.1, 0,  .1, color="#000")
    $speedFlash = Fade(.01, .01, .01, color="#fff")
    $slowFade =  Fade(2,0,2,color="#000")
    $speedDissolve = Dissolve(0.01)
    $slowDissolve = Dissolve(2.0)


#character definition for the text box here.
define d = Character("Deanna", color="#00C7B6", ctc="ctc_blink", ctc_position="nestled", window_style="window1")
define n = Character("  ", ctc="ctc_blink", ctc_position="nestled", window_style="window1")
define l = Character("Lethabo", color="#AD1400", ctc="ctc_blink", ctc_position="nestled", window_style="window1")
define a = Character("Athos", color="#4D802E", ctc="ctc_blink", ctc_position="nestled", window_style="window1")
define dSecond = Character("Deanna", window_style="window2", ctc="ctc_blink", ctc_position="nestled")
define n_second = Character(" ", window_style="window2", ctc="ctc_blink", ctc_position="nestled")
define letho_second = Character("Lethabo", window_style="window2", ctc="ctc_blink", ctc_position="nestled")
define athos_second = Character("Athos", window_style="window2", ctc="ctc_blink", ctc_position="nestled")

#storybook 1 custom images
image bg_stb1_page1 = "images/Storybook 1/bg stb1_page 1.png"
image bg_stb1_page2 = "images/Storybook 1/bg stb1_page 2.png"
image bg_stb1_page3_1 = "images/Storybook 1/bg stb1_page 3_1.png"
image bg_stb1_page3_2 = "images/Storybook 1/bg stb1_page 3_2.png"
image bg_stb1_page4 = "images/Storybook 1/bg stb1_page 4.png"
image bg_stb1_page5 = "images/Storybook 1/bg stb1_page 5.png"
image stb1_deanna_worried = "images/Storybook 1/deanna_close_worried.png"
image stb1_EXTRA = "images/Storybook 1/EXTRA.png"
image stb1_deanna_call_out = "images/Storybook 1/stb1_page 3_deanna calling out.png"
image stb1_deanna_wake_up = "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
image stb1_deanna_wake_up_2 = "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
image stb1_deanna_kneel_wake_up = "images/Strorybook 1/stb1_page 3_deanna waking up 3.png"
image stb1_scarry_sound_sfx1 = "images/Storybook 1/stb1_page4_sfx 1.png"
image stb1_scarry_sound_sfx2 = "images/Storybook 1/stb1_page4_sfx 2.png"


#these need to be fixed and more inline with the powerpoint
image deanna forest blinks:
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png" 
    pause 0.5
    "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
    pause 1.0
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
    pause .75
    "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
    pause 0.5
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
    pause .75
    "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
    pause 0.25
    repeat
        
image nosie_flasher:
    "images/Storybook 1/stb1_page4_sfx 1.png"  
    pause 0.25
    "images/Storybook 1/stb1_page4_sfx 2.png" 
    pause 0.25
    repeat 

#trying thought bubble as the click-to-continue button
image ctc_blink:
    "images/Misc_Text_GUI/arrow_1.png"
    zoom 0.2
    linear 0.5 alpha 1.0
    "images/Misc_Text_GUI/arrow_2.png"
    linear 0.5 alpha 1.0
    zoom 0.1
    "images/Misc_Text_GUI/arrow_1.png"
    zoom 0.2
    repeat

style window_place:
    xalign 1.0
    yalign 1.0
    background Image("images/Misc_Text_GUI/vines_textbox.png")


image athos_hang_swing:
    stb2_athos_swinging1
    pause 0.7
    stb2_athos_swinging2
    pause 0.7
    repeat

image lethabo_climb:
    "images/Storybook 2/stb2_page 5_lethabo on tree 1.png"
    xpos 0.75 ypos 1.5
    pause 0.5
    "images/Storybook 2/stb2_page 5_lethabo on tree 1.png"
    xpos 0.75 ypos 1.1
    pause 0.5
    "images/Storybook 2/stb2_page 5_lethabo on tree 1.png"
    xpos 0.75 ypos 0.7
    pause 0.5
    "images/Storybook 2/stb2_page 5_lethabo on tree 2.png"
    xpos 0.65 ypos 0.7
    pause 0.5
    "images/Storybook 2/stb2_page 5_lethabo on tree 2.png"
    xpos 0.75 ypos 0.7
    

image lethabo_claw:
    "images/Storybook 2/stb2_page 5_lethabo on tree 3.png"
    pause 0.5
    "images/Storybook 2/stb2_page 5_lethabo on tree 4.png"
    pause 0.5
    repeat

image athosswingfromtree:
    "images/Storybook 2/stb2_page 5_athos hanging 4.png"
    xpos 0.5 ypos 0.8

image lethabo_after_claw:
    "images/Storybook 2/stb2_page 5_lethabo on tree 4.png"
    xpos 0.7 ypos 0.8

image athos_on_ground:
    "images/Storybook 2/stb2_page 8_athos on floor 1.png"
    xpos 0.75 ypos 0.9

image athos_on_ground2:
    "images/Storybook 2/stb2_page 8_athos on floor 2.png"
    xpos 0.75 ypos 0.9
    pause 2.0

image athos_on_ground3:
    "images/Storybook 2/stb2_page 8_athos on floor 3.png"
    xpos 0.75 ypos 0.9

image athos_on_ground4:
    "images/Storybook 2/stb2_page 8_athos on floor 4.png"
    xpos 0.54 ypos 0.91

image deanna_glasses_drag:
    "images/Storybook 2/stb2_page 8_deanna 1.png"
    xpos 0.1 ypos 0.999

image deanna_glasses_drag2:
    "images/Storybook 2/stb2_page 8_deanna 2.png"
    xpos 0.29 ypos 0.9

image deanna_glasses_drag3:
    "images/Storybook 2/stb2_page 8_deanna 3.png"
    xpos 0.35 ypos 0.9

image deanna_magic_sense:
    "images/Storybook 2/stb2_page 9_aesop vfx 1.png"
    xpos 0.43 ypos 0.42
    pause 0.25
    "images/Storybook 2/stb2_page 9_aesop vfx 2.png"
    xpos 0.43 ypos 0.31
    pause 0.25
    repeat


image athos_letho_final_upright:
    stb2_page10_atho_letho1
    xpos 0.47 ypos 0.9

image athos_letho_final_upright2:
    stb2_page10_atho_letho2
    xpos 0.47 ypos 0.9

image deanna_fly_off:
    "images/Storybook 2/stb2_page 10_deanna 2.png"

image deanna_through_grass:
    stb2_page11_d
    xpos 0.51 ypos 0.61

image athos_letho_through_grass:
    stb2_page11_athos_letho
    xpos 0.45 ypos 0.88

image stb3_deanna_animation:
    stb3_page1_deanna_1
    pause 0.5
    stb3_page1_deanna_2
    pause 0.5

image stb3_page1_darkened:
    stb3_page1_darkened
    xpos 0.5335 ypos 0.64

image stb3_page1_smeared_fall_down:
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.31
    pause 2.0
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.315
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.32
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.325
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.335
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.345
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.35
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.375
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.425
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.45
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.475
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.5
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.525
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.55
    pause 0.33
    "images/Storybook 3/stb3_images/stb3_page 1_smeared mask.png"
    xpos 0.5 ypos 0.575
    pause 0.33

image stb3_deanna_kneel_floor:
    "images/Storybook 3/stb3_images/stb3_page 1_deanna 1.png"
    xpos 0.5 ypos 0.85
    pause 1.0
    "images/Storybook 3/stb3_images/stb3_page 1_deanna 2.png"
    xpos 0.5 ypos 0.85
    pause 1.0

image strb3_deanna_kneel_before_alert:
    "images/Storybook 3/stb3_images/stb3_page 1_deanna 1.png"
    xpos 0.5 ypos 0.85
    pause 1.0
image stb3_deanna_kneel_floor_2:
    "images/Storybook 3/stb3_images/stb3_page 1_deanna 1.png"
    xpos 0.5 ypos 0.85

image stb3_smeared_charge:
    "images/Storybook 3/stb3_images/stb3_page 2_smeared 1.png"
    xpos 0.45 ypos 0.9

image stb3_deanna_scarred:
    "images/Storybook 3/stb3_images/stb3_page 2_deanna 1.png"
    xpos 0.65 ypos 0.9

image stb3_deanna_spear_scarred:
    "images/Storybook 3/stb3_images/stb3_page 2_deanna 2.png"
    xpos 0.65 ypos 0.9

image stb3_smeared_spear_jump:
    "images/Storybook 3/stb3_images/stb3_page 2_smeared 2.png"
    xpos .3 ypos 0.9

image stb3_blue_swoop:
    "images/Storybook 3/stb3_images/stb3_page 2_blur swipe.png"

image stb3_page2_smear_jump_spear:
    "images/Storybook 3/stb3_images/stb3_page 2_smeared 3.png"
    xpos 0.5 ypos 0.99999999999

image athos_let_grab_deanna:
    "images/Storybook 3/stb3_images/stb3_page 3_athos lethabo and deanna.png"
    xpos 0.3 ypos 0.95

image smearerd_chase:
    "images/Storybook 3/stb3_images/stb3_page 3_smeared.png"
    xpos 0.65 ypos 0.9

image stb3_page5_smog:
    "images/Storybook 3/stb3_images/stb3_page 5_smog 1.png"
    xpos 0.95 ypos 0.9

image letho_page9:
    "images/Storybook 3/stb3_images/stb3_page 9_lethabo.png"
    anchor(0.5, 0.5)
    xpos 0.35 ypos 0.6

image athos_page9:
    "images/Storybook 3/stb3_images/stb3_page 9_athos.png"
    anchor(0.5, 0.5)
    xpos .65 ypos 0.6

image leth_page10:
    "images/Storybook 3/stb3_images/stb3_page 10_lethabo.png"
    anchor(0.5, 0.5)
    xpos .18 ypos .8

image atho_page10:
    "images/Storybook 3/stb3_images/stb3_page 10_athos.png"
    anchor(0.5, 0.5)
    xpos 0.4 ypos 0.7

image deanna_getsAngry_page13:
    "images/Storybook 3/stb3_images/stb3_page 13_deanna 1.png"
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.5

image deanna_getsAngry_page13_2:
    "images/Storybook 3/stb3_images/stb3_page 13_deanna 2.png"
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.6

image deanna_getsAngry_page13_3:
    "images/Storybook 3/stb3_images/stb3_page 13_deanna 3.png"
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.6

image deanna_lyre_page13:
    "images/Storybook 3/stb3_images/stb3_page 13_lyre.png"
    anchor(0.5, 0.5)
    xpos 0.38
    ypos 0.76

image deanna_page10:
    "images/Storybook 3/stb3_images/stb3_page 10_deanna.png"
    anchor(0.5, 0.5)
    xpos 0.82 ypos 0.58

image deanna_flyToFight_page14:
    "images/Storybook 3/stb3_images/stb3_page 14_deanna 1.png"
    anchor(0.5, 0.5)
    xpos 0.79
    ypos 0.74

image smearedFight:
    "images/Storybook 3/stb3_images/stb3_page 15_smeared.png"
    anchor(0.5, 0.5)
    xpos 0.57
    ypos 0.6

image leth_atho_smearedWin:
    "images/Storybook 3/stb3_images/stb3_page 15_lethabo and athos.png"
    anchor(0.5,0.5)
    xpos 0.3
    ypos 0.8

image deannaStandTall_smearedFight:
    "images/Storybook 3/stb3_images/stb3_page 15_deanna.png"
    anchor(0.5,0.5)
    xpos 0.325 
    ypos 0.5
image deannaShieldMagic:
    "images/Storybook 3/stb3_images/stb3_page 15_shield.png"
    anchor(0.5,0.5)
    xpos 0.5
    ypos 0.515
    zoom 1.1

image shieldSplinter:
    "images/Storybook 3/stb3_images/stb3_page 16_shield 1.png"
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5

image shieldSplinterSmearedAttack:
    "images/Storybook 3/stb3_images/stb3_page 16_shield 2.png"
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5
    alpha 0.5

image shieldSplinterSmearedAttack2:
    "images/Storybook 3/stb3_images/stb3_page 16_shield 2.png"
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5
    alpha 1.0

image smearedAttacking:
    "images/Storybook 3/stb3_images/stb3_page 16_smeared.png"
    anchor(0.5,0.5)
    xpos 0.65
    ypos 0.525
    alpha 0.25

image smearedAttack:
    "images/Storybook 3/stb3_images/stb3_page 16_smeared.png"
    anchor(0.5,0.5)
    xpos 0.65
    ypos 0.525
    alpha 1.5

image deannaLoaseShield:
    "images/Storybook 3/stb3_images/stb3_page 17_deanna 1.png"
    pause 0.25
    "images/Storybook 3/stb3_images/stb3_page 17_deanna 2.png"
    pause 0.5
    "images/Storybook 3/stb3_images/stb3_page 17_deanna 3.png"
    pause 2.0

image lethoAthosSlowStand:
    "images/Storybook 3/stb3_images/stb3_page 17_lethabo and athos behind.png"
    

image athosActionPop:
    "images/Storybook 3/stb3_images/stb3_page 17_athos action pop.png" with easeinright
    anchor(0.5,0.5)
    xpos 0.28 
    ypos 0.58

image lethoActionPop:
    "images/Storybook 3/stb3_images/stb3_page 17_lethabo action pop.png" with easeinleft
    anchor(0.5,0.5)
    xpos 0.7
    ypos 0.53

image deannaPreActionPop:
    "images/Storybook 3/stb3_images/stb3_page 17_deanna action pop 1.png"
    anchor(0.5,0.5)
    xpos 0.5 
    ypos 0.53

image deannaActionPop:
    "images/Storybook 3/stb3_images/stb3_page 17_deanna action pop 2.png"
    anchor(0.5,0.5)
    xpos 0.5 
    ypos 0.53

image deanna_wakes_up:
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
    pause 0.3
    "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
    pause 0.3
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
    pause 0.3
    "images/Storybook 1/stb1_page 3_deanna waking up 2.png"
    pause 0.3
    "images/Storybook 1/stb1_page 3_deanna waking up 1.png"
    pause 0.5
    "images/Storybook 1/stb1_page 3_deanna waking up 3.png"


#image diana fly: //this is an example for making an animation
#   "dianaFlap.png"
#   pause 0.4
#    "dianaBlink.png" with Dissolve(0.3)
#    #pause 0.4
#    "dianaFlap.png" with Dissolve(0.3)
#    pause 0.4
#    "dianaBlink.png" with Dissolve(0.3)
#    pause 0.4
#    repeat

#define transforms (position) and other image attributes here

transform deanna_forest_transform:
    anchor (0.5, 0.5) #to place the center point of the image in the center vs the top left corner
    pos(925, 675)
    zoom 1

transform deanna_wake_up_forest_floor:
    anchor(0.5, 0.5)
    pos(925, 425)

transform nosie_flasherRight:
    anchor(0.5, 0.5)
    pos(1400, 475)

transform deanna_worried_left:
    anchor(0.5, 0.5)
    pos(800, 650)
    zoom 0.85

transform dialog_textbox:
    xalign 0.5
    yalign 1.0

transform down_arrow_placement:
    anchor(0.5,0.5)
    pos(1300, 750)


style window1:
    xalign 0.5
    xfill True
    yalign 0.0
    ysize gui.textbox_height
    background Image("images/vines_textbox.png")


style window2:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize gui.textbox_height
    background Image("images/vines_textbox.png")

#Explorer Mode 1

image exp_mode_dew_drop = 'animation_water droplet 1.png'


