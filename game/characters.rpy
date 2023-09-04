#define characters and the animations that they will/may use here

init:
    $flash = Fade(.5, 0, .75, color="#fff")
    $flashDelay = Fade(.1, 0,  .1, color="#000")
    $speedFlash = Fade(.01, .01, .01, color="#fff")


#character definition for the text box here.
define d = Character("Deanna", color="#00C7B6")
define n = Character("  ",)
define l = Character("Lethabo", color="#AD1400")
define a = Character("Athos", color="#4D802E")

#define the images to be used for the characters here. 

image deannaSleep = "deanna_sleep.png"
image deannaAwake = "deanne_awake.png"
image deannaBlink = "deanna_eyes_opening.png"
image deannaShout = "deanna_calling_out.png"
image noiseSignal1 = "noise_signifier_1.png"
image noiseSignale2 = "noise_signifier_2.png"

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