#storybook 1 page 4

label stb1_page3:

scene bg_stb1_page_3_1 with zoomin
pause 0.5
show bg_stb1_page_3_2 with dissolve
pause 0.25

show deanna forest blinks at deanna_forest_transform
pause 4.0
hide bg_stb1_page_3_1 with dissolve
hide deanna forest blinks
scene bg_stb1_page_3_2 with dissolve
show deanna_awake at deanna_wake_up_forest_floor with dissolve
#window auto dialog_textbox
n "Deanna finally awoke among the ruins of what was left of their getaway wagon. She immediately realized something amiss." 
window hide
pause 0.25
n "Her friends weren\’t with her!"
window hide
pause 0.25
n "Deana listened for any signs of her friends…"
window hide
pause 0.25
hide deanna_awake
pause 0.25
show deanna_calling_out at deanna_worried_left
d "“Lethabo! Athos! Where are you?”"
window hide
pause 0.5

call stb1_page4

