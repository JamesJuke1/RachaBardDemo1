#for the explorer mode 1 Deanna explored herself and crosses a pond
label exp1_page1:

scene bg exp1_page 1
stop music 
n 'This is 1st page of the Explore Mode 1'
play audio 'audio/Explore 1/Sounds + Music/Music/Explore 1-Background Musicv2.mp3' loop volume 0.75
n 'Music should be playing in the background'
show deanna_animation_right at deanna_right_page1
show  down_arrow_animation at down_arrow_placement
window hide
pause 2.0
call screen exp1_page1_down_arrow

label exp1_page2:
scene bg exp1_page 2
window hide 
call screen clickable_dew_drop

label exp1_page2_part2:
    scene bg exp1_page 2
    n 'This is second page of the second page of Explore mode 1, Deanna should be just right of center, looking left'
    window hide
    call screen after_clickable_dew_drop

label deanna_talk_to_dew_drop:
    scene bg exp1_page 3
    play sound 'audio/explore 1/Sounds + Music/Narrator Dialogues/Narrator-EX1_d1_v3.mp3' volume 1.25
    n 'Deanna peers into her bloated cockroach figure in the dew drop.'
    play sound 'audio/explore 1/Sounds + Music/Deanna Explore 1/Deanna_EX1_p3_d1.mp3' volume 1.5
    d 'Cockroaches can\'t be heroes'
    call exp1_page4 from _call_exp1_page4

label exp1_page4:
scene bg exp1_page 4
n "the Rock Pond Start of the explore mode"
window hide
pause 2.0
call screen exp1_page4_rock_pond_start

label exp1_page4_rock1:
    call screen exp1_page4_rock_pond_rock1

label exp1_page4_rock2:
    call screen exp1_page4_rock_pond_rock2

label exp1_page4_rock3:
    call screen exp1_page4_rock_pond_rock3

label exp1_page5_rock_pond_middle:
    call screen exp1_page5_rock_pond_rock1

label exp1_page5_rock_pond_middle_rock2:
    call screen exp1_page5_rock_pond_rock2

label exp1_page5_rock_pond_middle_rock3: #fish animation rock #1
    call screen exp1_page5_rock_pond_rock3

label exp1_page5_rock_pond_middle_rock4: 
    call screen exp1_page5_rock_pond_rock4

label exp1_page5_rock_pond_middle_rock5:
    call screen exp1_page5_rock_pond_rock5

label exp1_page5_rock_pond_middle_rock6: 
    call screen exp1_page5_rock_pond_rock6

label exp1_page5_rock_pond_middle_rock7: 
    call screen exp1_page5_rock_pond_rock7

label exp1_page5_rock_pond_middle_rock8: #fish animation rock #2
    call screen exp1_page5_rock_pond_rock8

label exp1_page6: # just a test sound
    call screen deanna_after_pond

label exp1_page7:
    # this is the close up shot of deanna and the cricket
    show bg_stb1_page7
    play sound 'audio/explore 1/Sounds + Music/Deanna Explore 1/Deanna_EX1_p7_d1.mp3' 
    d 'Oh, hello! You’re a bug, too! Can you tell me where—'

    play sound 'audio/explore 1/Sounds + Music/Deanna Explore 1/Deanna_EX1_p7_d2.mp3'
    d 'That\’s right. Bugs can\’t normally talk. I wonder if the rest of the world sees me that way.'
    call screen exp1_page5_rock_pond_rock8

label deanna_exp1_animation:
    show bg exp1_page 6
    n 'this is the animation for deanna walking across the image'


label rock_fish_animation_left_pond:
    scene bg exp1_page 4
    #show 'images/explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
    pause 2.0
    call screen exp1_page4_rock_pond_start

label bad_rock_1:
    scene bg exp1_page 4
    #show  "images/Explore 1/images/close up shots/deanna_close_tense.png" at deanna_rock_fish_animation
    pause 0.5
    show spitting_fish at rock_fish_pos_1
    call screen exp1_page4_rock_pond_rock1

screen clickable_dew_drop():
    #can add elements as needed with the add command
    window:
        style "transparent_window"
        add "bg exp1_page 2"
        add 'deanna_animation_right' at deanna_right_page2
        text "inside the click screen"

    imagebutton:
        idle  "images/Explore 1/images/props/animation_water droplet/animation_water droplet_idle.png"
        hover "images/Explore 1/images/props/animation_water droplet/animation_water droplet_hover.png"
        xalign 0.58
        yalign 0.65
        action Jump('exp1_page2_part2')

screen after_clickable_dew_drop():
    window:
        style 'transparent_window'
        add 'bg exp1_page 2'
        add 'deanna_animation_right' at deanna_right_page2_2
        text 'second page of second page of explore mode, Deanna just right of center of screen'

    imagebutton:
        idle "images/Explore 1/images/props/animation_arrows/animation_arrow right/animation_arrow right 1.png"
        hover "images/Explore 1/images/props/animation_arrows/animation_arrow right/animation_arrow right 2.png"
        pos(1800, 520)
        action Jump('exp1_page4')

screen exp1_page1_down_arrow():
    window:
        style "transparent_window"
        add "bg exp1_page 1"
        add "images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle looking 5.png" at deanna_right_page1
        text "This is clickable Explorer page 1"

    imagebutton:
        idle "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 1.png"
        hover "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 2.png"
        xpos 1200
        ypos 700
        action Jump ('exp1_page2')

screen exp1_page4_rock_pond_start():
    window:
        style "transparent_window"
        add 'bg exp1_page4'
        text 'This is the start of the Rock Pond of Explore Mode 1'

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
            xpos 250
            ypos 550

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 925
            ypos 825
            action Jump('exp1_page4_rock1')

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1300
            ypos 650
            action Jump('exp1_page4') 
        
        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1600
            ypos 800
            action Jump('exp1_page4') 
        
        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            xpos 1300
            ypos 950
            action Jump('bad_rock_1')

screen exp1_page4_rock_pond_rock1():
    window:
        style "transparent_window"
        add 'bg exp1_page4'
        text 'This is the 1st page of the pond Rock 1'

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
            xpos 925
            ypos 850

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1300
            ypos 650
            action Jump('exp1_page4_rock2') 
        
        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1600
            ypos 800
            action Jump('exp1_page4') 

screen exp1_page4_rock_pond_rock2():
    window:
        style "transparent_window"
        add 'bg exp1_page4'
        text 'This is the 1st page of the pond Rock 2'

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
            xpos 1300
            ypos 650
        
        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1600
            ypos 800
            action Jump('exp1_page4_rock3') 

screen exp1_page4_rock_pond_rock3():
    window:
        style "transparent_window"
        add 'bg exp1_page4'
        text 'This is 1st page of the pond Rock 3'

        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
            xpos 925
            ypos 850
        
        imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1800
            yalign 0.5
            action Jump('exp1_page5_rock_pond_middle') 

#these are for the second half of the pond screen in the explore mode 1, this starts with 8 images and each progression loses 1 image
screen exp1_page5_rock_pond_rock1():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 50
        ypos 625

    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 450
            yalign 0.8
            action Jump('exp1_page5_rock_pond_middle_rock2')
    
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 575
            yalign 0.99
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 750
            yalign 0.8
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1000
            yalign 0.8
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 975
            yalign 0.99
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1250
            yalign 0.9
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1500
            yalign 0.85
    imagebutton:
            idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
            hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
            xpos 1800
            yalign 0.35

screen exp1_page5_rock_pond_rock2():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 450
        yalign 0.8
    
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 575
        yalign 0.99
        action Jump('exp1_page5_rock_pond_middle_rock3')
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 750
        yalign 0.8
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1000
        yalign 0.8
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 975
        yalign 0.99
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1250
        yalign 0.9
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock3():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 575
        yalign 0.99

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 750
        yalign 0.8
        action Jump('exp1_page5_rock_pond_middle_rock4')
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1000
        yalign 0.8
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 975
        yalign 0.99
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1250
        yalign 0.9
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock4():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 750
        yalign 0.8
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1000
        yalign 0.8
        action Jump('exp1_page5_rock_pond_middle_rock5')

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 975
        yalign 0.99
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1250
        yalign 0.9
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock5():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 1000
        yalign 0.8

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 975
        yalign 0.99
        action Jump('exp1_page5_rock_pond_middle_rock6')

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1250
        yalign 0.9
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock6():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 975
        yalign 0.99

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1250
        yalign 0.9
        action Jump('exp1_page5_rock_pond_middle_rock7')

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock7():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 1250
        yalign 0.9
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1500
        yalign 0.85
        action Jump('exp1_page5_rock_pond_middle_rock8')

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35

screen exp1_page5_rock_pond_rock8():
    window:
        style "transparent_window"
        add "bg exp1_page 5"
        text 'This is explore mode 1 middle of the pond'

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xpos 1500
        yalign 0.85

    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 1.png'
        hover 'images/Explore 1/images/character animation cycles/animation_rock fish/animation_rock fish 2.png'
        xpos 1800
        yalign 0.35
        action Jump('exp1_page6')

# these screens are for after Deanna crosses the rock pond.
screen deanna_after_pond():
    window:
        style 'transparent_window'
        add 'bg exp1_page 6'
        text 'deanna has crossed the rock pond safely. '
    
    imagebutton:
        idle 'images/Explore 1/images/character animation cycles/animation_deanna/animation_deanna idle/animation_deanna right idle cycle/animation_deanna right idle 0.png'
        xalign 0.25
        yalign 0.75

    imagebutton: #cricket on rock
        idle 'images/Explore 1/images/props/animation_cricket icon/animation_cricket icon 1.png'
        hover 'images/Explore 1/images/props/animation_cricket icon/animation_cricket icon 2.png'
        xalign 0.5
        yalign 0.5
        #action Jump('') # call to scene of deanna walking across the image, that calls to a close up image of deanna and cricket
    
    imagebutton: #back arrow, if player did not skip the pond
        idle "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 1.png"
        hover "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 2.png"
        xalign 0.33
        yalign 0.1
        #action Jump('deanna animation') # return to rock pond, but where in around the rock pond

    imagebutton: # up arrow to move to next page, near far side of screen closer to bottom of page
        idle "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 1.png"
        hover "images/Explore 1/images/props/animation_arrows/animation_arrow down/animation_arrow down 2.png"
        xalign 0.8
        yalign 0.75
        #action Jump('') # jump to next page in explore mode 1

    
