#Deanna realizes her friends are not around
#she begins to look  for them in a panic
       
label deannaAlertWakeup:

show bg deanna_wakeup with zoomin

show deanna forest blinks at deanna_forestTransform

n "Deanna finally awoke among the ruins of what was left of their getaway wagon." 
 
n  "She immediately realized something amiss."

hide deanna forest blinks with dissolve

show deanna_awake at deanna_forestTransform

n "Her friends weren\’t with her\!​"

hide deanna_awake with fade

show deanna_calling_out at deanna_forestTransform

d "“Lethabo! Athos! Where are you?”"

n "Deana listened for any signs of her friends…​"

hide deanna_calling_out

show deanna forest blinks at deanna_forestTransform
pause 0.2
d "The pause works"
hide deanna forest blinks
pause 0.2  
d "the pause works again"
show deanna_calling_out at deanna_forestTransform
pause 0.2
d "This is the way to do it. "

call worried_deanna