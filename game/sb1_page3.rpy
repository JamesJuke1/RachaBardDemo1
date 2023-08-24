#storybook 1 page 4

label sb1_page3:

scene bg sb1_page_3 with flash

show deanna forest blinks at deanna_forest_transform
pause 1.5
hide deanna forest blinks
pause 0.5
show deanna_awake at deanna_wake_up_forest_floor
#window auto dialog_textbox
n "Deanna finally awoke among the ruins of what was left of their getaway wagon. She immediately realized something amiss." 
window hide
pause 0.25
n "Her friends weren’t with her!"
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

call sb1_page4

