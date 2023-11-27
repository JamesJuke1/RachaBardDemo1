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


#these need to be fixed and more inline with the powerpoint
image deanna forest blinks:
    stb3_page1_deanna_1 
    pause 0.5
    stb1_deanna_wake_up_2
    pause 1.0
    stb3_page1_deanna_1
    pause .75
    stb1_deanna_wake_up_2
    pause 0.5
    stb3_page1_deanna_1
    pause .75
    stb1_deanna_wake_up_2
    pause 0.25
    repeat
        
image nosie_flasher:
    stb1_scarry_sound_sfx1  
    pause 0.25
    stb1_scarry_sound_sfx1 
    pause 0.25
    repeat 

#trying thought bubble as the click-to-continue button
image ctc_blink:
    "images/arrow_1.png"
    zoom 0.2
    linear 0.5 alpha 1.0
    "images/arrow_2.png"
    linear 0.5 alpha 1.0
    zoom 0.1
    "images/arrow_1.png"
    zoom 0.2
    repeat

style window_place:
    xalign 1.0
    yalign 1.0
    background Image("images/vines_textbox.png")


image athos_hang_swing:
    stb2_athos_swinging1
    pause 0.7
    stb2_athos_swinging2
    pause 0.7
    repeat

image  lethabo_climb:
    stb2_letho_climb_tree1
    xpos 0.75 ypos 1.5
    pause 0.5
    stb2_letho_climb_tree2
    xpos 0.75 ypos 1.1
    pause 0.5
    stb2_letho_climb_tree1
    xpos 0.75 ypos 0.7
    pause 0.5
    stb2_letho_climb_tree2
    xpos 0.65 ypos 0.7
    pause 0.5
    stb2_letho_climb_tree1
    xpos 0.75 ypos 0.7
    

image lethabo_claw:
    stb2_letho_claw_swipe_tree1
    pause 0.5
    stb2_letho_claw_swipe_tree2
    pause 0.5
    repeat

image athosswingfromtree:
    stb2_athos_falling_tree1
    xpos 0.5 ypos 0.8

image lethabo_after_claw:
    stb2_letho_claw_swipe_tree2
    xpos 0.7 ypos 0.8

image athos_on_ground:
    stb2_page8_athos_floor1
    xpos 0.75 ypos 0.9

image athos_on_ground2:
    stb2_page8_athos_floor2
    xpos 0.75 ypos 0.9
    pause 2.0

image athos_on_ground3:
    stb2_page8_athos_floor3
    xpos 0.75 ypos 0.9

image athos_on_ground4:
    stb2_page8_athos_floor4
    xpos 0.54 ypos 0.91

image deanna_glasses_drag:
    stb2_page8_d_1
    xpos 0.1 ypos 0.999

image deanna_glasses_drag2:
    stb2_page8_d_2
    xpos 0.29 ypos 0.9

image deanna_glasses_drag3:
    stb2_page8_d_3
    xpos 0.35 ypos 0.9

image deanna_magic_sense:
    stb2_page9_aesop_vfx1
    xpos 0.43 ypos 0.42
    pause 0.25
    stb2_page9_aesop_vfx2
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
    stb2_page10_d_2

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
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.31
    pause 2.0
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.315
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.32
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.325
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.335
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.345
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.35
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.375
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.425
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.45
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.475
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.5
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.525
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.55
    pause 0.33
    stb3_page1_smeared_mask
    xpos 0.5 ypos 0.575
    pause 0.33

image stb3_deanna_kneel_floor:
    stb3_page1_deanna_1
    xpos 0.5 ypos 0.85
    pause 1.0
    stb3_page1_deanna_2
    xpos 0.5 ypos 0.85
    pause 1.0

image strb3_deanna_kneel_before_alert:
    stb3_page1_deanna_1
    xpos 0.5 ypos 0.85
    pause 1.0
image stb3_deanna_kneel_floor_2:
    stb3_page1_deanna_2
    xpos 0.5 ypos 0.85

image stb3_smeared_charge:
    stb3_page2_smeared_1
    xpos 0.45 ypos 0.9

image stb3_deanna_scarred:
    stb3_page2_deanna_1
    xpos 0.65 ypos 0.9

image stb3_deanna_spear_scarred:
    stb3_page2_deanna_2
    xpos 0.65 ypos 0.9

image stb3_smeared_spear_jump:
    stb3_page2_smeared_2
    xpos .3 ypos 0.9

image stb3_blue_swoop:
    stb3_page2_blur_swipe

image stb3_page2_smear_jump_spear:
    stb3_page2_smeared_3
    xpos 0.5 ypos 0.99999999999

image athos_let_grab_deanna:
    stb3_page3_leth_athos
    xpos 0.3 ypos 0.95

image smearerd_chase:
    stb3_page3_smeared
    xpos 0.65 ypos 0.9

image stb3_page5_smog:
    stb3_page5_smog1
    xpos 0.95 ypos 0.9

image letho_page9:
    stb3_page9_letho
    anchor(0.5, 0.5)
    xpos 0.35 ypos 0.6

image athos_page9:
    stb3_page9_athos
    anchor(0.5, 0.5)
    xpos .65 ypos 0.6

image leth_page10:
    stb3_page10_letho
    anchor(0.5, 0.5)
    xpos .18 ypos .8

image atho_page10:
    stb3_page10_athos
    anchor(0.5, 0.5)
    xpos 0.4 ypos 0.7

image deanna_getsAngry_page13:
    stb3_page13_deanna1
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.5

image deanna_getsAngry_page13_2:
    stb3_page13_deanna2
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.6

image deanna_getsAngry_page13_3:
    stb3_page13_deanna3
    anchor(0.5, 0.5)
    xpos 0.5
    ypos 0.6

image deanna_lyre_page13:
    stb3_page13_lyre
    anchor(0.5, 0.5)
    xpos 0.38
    ypos 0.76

image deanna_page10:
    stb3_page10_deanna
    anchor(0.5, 0.5)
    xpos 0.82 ypos 0.58

image deanna_flyToFight_page14:
    stb3_page14_deanna1
    anchor(0.5, 0.5)
    xpos 0.79
    ypos 0.74

image smearedFight:
    stb3_page15_smeared
    anchor(0.5, 0.5)
    xpos 0.57
    ypos 0.6

image leth_atho_smearedWin:
    stb3_page15_letho_athos
    anchor(0.5,0.5)
    xpos 0.3
    ypos 0.8

image deannaStandTall_smearedFight:
    stb3_page15_deanna
    anchor(0.5,0.5)
    xpos 0.325 
    ypos 0.5
image deannaShieldMagic:
    stb3_page15_shield
    anchor(0.5,0.5)
    xpos 0.5
    ypos 0.515
    zoom 1.1

image shieldSplinter:
    stb3_page16_shield1
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5

image shieldSplinterSmearedAttack:
    stb3_page16_shield2
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5
    alpha 0.5

image shieldSplinterSmearedAttack2:
    stb3_page16_shield2
    anchor(0.5, 0.5)
    xpos 0.45
    ypos 0.5
    alpha 1.0

image smearedAttacking:
    stb3_page16_smeared
    anchor(0.5,0.5)
    xpos 0.65
    ypos 0.525
    alpha 0.25

image smearedAttack:
    stb3_page16_smeared
    anchor(0.5,0.5)
    xpos 0.65
    ypos 0.525
    alpha 1.5

image deannaLoaseShield:
    stb3_page17_deanna1
    pause 0.25
    stb3_page17_deanna2
    pause 0.5
    stb3_page17_deanna3
    pause 2.0

image lethoAthosSlowStand:
   stb3_page17_letho_athos_behind
    

image athosActionPop:
    stb3_page17_athos_action_pop with easeinright
    anchor(0.5,0.5)
    xpos 0.28 
    ypos 0.58

image lethoActionPop:
    stb3_page17_letho_action_pop with easeinleft
    anchor(0.5,0.5)
    xpos 0.7
    ypos 0.53

image deannaPreActionPop:
    stb3_page17_d_action_pop1
    anchor(0.5,0.5)
    xpos 0.5 
    ypos 0.53

image deannaActionPop:
    stb3_page17_d_action_pop2
    anchor(0.5,0.5)
    xpos 0.5 
    ypos 0.53

# image deanna_wakes_up:
#    "deanna_sleep.png"
#    pause 0.3
#    "deanna_eyes_opening.png"
#    pause 0.3
#    "deanna_sleep.png"
#    pause 0.3
#   "deanna_eyes_opening.png"
#n "Deanna finally awoke"
#    pause 0.3
#n "She immediately realized something amiss"
#    pause 0.3
#    "deanna_awake.png"
#    pause 0.5
#    "deanna_calling_out.png"

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
