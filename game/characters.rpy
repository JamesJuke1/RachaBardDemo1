#define characters and the animations that they will/may use here


#character definition for the text box here.
define e = Character("Eileen")
define d = Character("Deanna", color="#00C7B6")
define n = Character("Narrator")
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


image deanna forest blinks:
    "deanna_sleep.png"
    pause 0.2
    "deanna_eyes_opening.png"
    pause 0.2
    repeat
        

#image diana fly:
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

transform deanna_forestTransform:
    anchor (0.5, 0.5) #to place the center point of the image in the center vs the top left corner
    pos(960, 600)
    zoom 0.45