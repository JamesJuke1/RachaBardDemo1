#storybook2 page 5, slide 4, Athos stuck hanging from tree

label stb2_page5:

scene bg_stb2_page5 with pushdown

show stb2_athos_hanging
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d8_v2.mp3'
n "And there was Athos stuck in  a tree! All tangled up in vines!\n He didn\'t look pleased in the slightest"
window hide
stop sound
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Lethabo Storybook 2/Lethabo_SB2_p5_d3.mp3'
l "Look on the bright side, Athos! At least we were lucky enough to have the vines break our fall!"
window hide
stop sound
pause 0.5
play audio 'audio/storybook 2/Sounds + Music/Athos Storybook 2/Athos SB2-p8-1.mp3'
a "{i}Luckly?!{/i} We've been imprisoned  by a crazy monkey-who just left us to die to a nightmarish monster of legend\n-which is apperently {i}real!{/i}"
window hide 
pause 0.5
#athos is swinging in the tangled vines with Lethabo climbing the tree
play sound 'audio/storybook 2/Sounds + Music/Athos Storybook 2/Athos SB2-p8-2.mp3'
a "Ooooh, if ever I see that monkey again, I swear I will... I will..\n {i}Sua faccio un mazzo cosi!{/i}"
window hide
stop sound
pause 0.5
play sound 'audio/storybook 2/Sounds + Music/Lethabo Storybook 2/Lethabo_SB2_p5_d1.mp3'
l "Athos... Watch your tongue.There are children present."
window hide 
stop sound
pause 2.0

show lethabo_climb
window hide
#Lerthabo climbs the tree with claws ready to cut athos down
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d9_v2.mp3'
n "Lethabo had climbed the tree, readied his claw and-"
window hide 
stop sound
hide athos_hang_swing with dissolve
hide lethabo_climb with dissolve


#jump to next scene of just Lethabo's claws animation to symbolize athos being cut out of the tree
call stb2_page6 from _call_stb2_page6
