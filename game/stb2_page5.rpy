#storybook2 page 5, slide 4, Athos stuck hanging from tree

label stb2_page5:

scene bg stb2_page 5 with pushdown
pause 0.5
show athos_hang_swing
n "And there was Athos stuck in  a tree! All tangled up in vines!\n He didn\'t look pleased in the slightest"
window hide
pause 0.5

l "Look on the bright side, Athos! At least we were lucky enough to have the vines break our fall!"
window hide
pause 0.5

a "{i}Luckly?!{/i} We've been imprisoned  by a crazy monkey-who just left us to die to a nightmarish monster of legend\n-which is apperently {i}real!{/i}"
window hide 
pause 0.5
#athos is swinging in the tangled vines with Lethabo climbing the tree
a "Ooooh, if ever I see that monkey again, I swear I will... I will..\n {i}Sua faccio un mazzo cosi!{/i}"
window hide
pause 0.5

l "Athos... Watch your tongue.There are children present."
window hide 
pause 2.0

show lethabo_climb
window hide
#Lerthabo climbs the tree with claws ready to cut athos down
n "Lethabo had climbed the tree, readied his claw and-"
window hide 
hide athos_hang_swing with dissolve
hide lethabo_climb with dissolve


#jump to next scene of just Lethabo's claws animation to symbolize athos being cut out of the tree
call stb2_page6
