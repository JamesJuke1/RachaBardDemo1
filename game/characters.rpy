#define characters and the animations that they will/may use here

init:
    $flash = Fade(.5, 0, .75, color="#fff")
    $flashDelay = Fade(.1, 0,  .1, color="#000")
    $speedFlash = Fade(.01, .01, .01, color="#fff")


#character definition for the text box here.
define d = Character("Deanna", color="#00C7B6", ctc="ctc_blink", ctc_position="nestled")
define n = Character("  ", ctc="ctc_blink", ctc_position="nestled")
define l = Character("Lethabo", color="#AD1400", ctc="ctc_blink", ctc_position="nestled")
define a = Character("Athos", color="#4D802E", ctc="ctc_blink", ctc_position="nestled")

#define the images to be used for the characters here. 

image deannaSleep = "deanna_sleep.png"
image deannaAwake = "deanne_awake.png"
image deannaBlink = "deanna_eyes_opening.png"
image deannaShout = "deanna_calling_out.png"
image noiseSignal1 = "noise_signifier_1.png"
image noiseSignale2 = "noise_signifier_2.png"
image athosswingfromtree = "images/stb2_page 5_athos hanging 4.png"
image athosswingfromtree2 = "images/stb2_page 5_athos hanging 5.png"

#define the animations for the characters here

image deanna_sleepForest:
    "deannaSleep"

#these need to be fixed and more inline with the powerpoint
image deanna forest blinks:
    "deanna_sleep.png" 
    pause 0.5
    "deanna_eyes_opening.png"
    pause 1.0
    "deanna_sleep.png"
    pause .75
    "deanna_eyes_opening.png"
    pause 0.5
    repeat
        
image nosie_flasher:
    "noise_signifier1.png"  
    pause 0.25
    "noise_signifier2.png" 
    pause 0.25
    repeat 

#trying thought bubble as the click-to-continue button
image ctc_blink:
    "gui/thoughtbubble.png"
    linear 0.5 alpha 1.0
    "gui/window_icon.png"
    linear 0.5 alpha 0.25
    "gui/thoughtbubble.png"
    xpos 0.5 ypos 0.5
    xanchor 0.5 yanchor 0.5
    repeat

style window_place:
    xalign 1.0
    yalign 1.0
    background Image("images/vines_textbox.png")


image athos_hang_swing:
    "images/stb2_page 5_athos hanging 1.png"
    pause 0.7
    "images/stb2_page 5_athos hanging 2.png"
    pause 0.7
    "images/stb2_page 5_athos hanging 3.png"
    pause 0.7
    repeat

image  lethabo_climb:
    "images/stb2_page 5_lethabo on tree 1.png"
    xpos 0.75 ypos 1.5
    pause 0.5
    "images/stb2_page 5_lethabo on tree 1.png"
    xpos 0.75 ypos 1.1
    pause 0.5
    "images/stb2_page 5_lethabo on tree 2.png"
    xpos 0.75 ypos 0.7
    pause 0.5
    "images/stb2_page 5_lethabo on tree 3.png"
    xpos 0.65 ypos 0.7
    pause 0.5
    "images/stb2_page 5_lethabo on tree 4.png"
    xpos 0.75 ypos 0.7
    repeat

image lethabo_claw:
    "images/stb2_page 5_slash 1.png"
    pause 0.5
    "images/stb2_page 5_slash 2.png"
    pause 0.5
    repeat

image athosswingfromtree:
    "images/stb2_page 5_athos hanging 4.png"
    xpos 0.5 ypos 0.8

image lethabo_after_claw:
    "images/stb2_page 5_lethabo on tree 4.png"
    xpos 0.7 ypos 0.8

image athos_on_ground:
    "images/stb2_page 8_athos on floor 1.png"
    xpos 0.75 ypos 0.9

image athos_on_ground2:
    "images/stb2_page 8_athos on floor 2.png"
    xpos 0.75 ypos 0.9
    pause 2.0

image athos_on_ground3:
    "images/stb2_page 8_athos on floor 3.png"
    xpos 0.75 ypos 0.9

image athos_on_ground4:
    "images/stb2_page 8_athos on floor 4.png"
    xpos 0.54 ypos 0.91

image deanna_glasses_drag:
    "images/stb2_page 8_deanna 1.png"
    xpos 0.1 ypos 0.999

image deanna_glasses_drag2:
    "images/stb2_page 8_deanna 2.png"
    xpos 0.29 ypos 0.9

image deanna_glasses_drag3:
    "images/stb2_page 8_deanna 3.png"
    xpos 0.35 ypos 0.9

image deanna_magic_sense:
    "images/stb2_page 9_aesop vfx 1.png"
    xpos 0.43 ypos 0.42
    pause 0.25
    "images/stb2_page 9_aesop vfx 2.png"
    xpos 0.43 ypos 0.31
    pause 0.25
    repeat

#this will have to work for now, but will need a new image to line up properly. 
image deanna_magic_sense2:
    "images/stb2_page 9_aesop vfx 1.png"
    xpos 0.5 ypos 0.5
    pause 0.25
    "images/stb2_page 9_aesop vfx 2.png"
    xpos 0.5 ypos 0.41
    pause 0.25
    repeat

image athos_letho_final_upright:
    "images/stb2_page 10_athos and lethabo 1.png"
    xpos 0.47 ypos 0.9

image athos_letho_final_upright2:
    "images/stb2_page 10_athos and lethabo 2.png"
    xpos 0.47 ypos 0.9

image deanna_fly_off:
    "images/stb2_page 10_deanna 2.png"

image deanna_through_grass:
    "images/stb2_page 11_deanna.png"
    xpos 0.51 ypos 0.61

image athos_letho_through_grass:
    "images/stb2_page 11_athos and lethabo.png"
    xpos 0.45 ypos 0.88
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
    pos(925, 450)

transform nosie_flasherRight:
    anchor(0.5, 0.5)
    pos(1400, 475)

transform deanna_worried_left:
    anchor(0.5, 0.5)
    pos(350, 650)
    zoom 1

transform dialog_textbox:
    xalign 0.5
    yalign 1.0