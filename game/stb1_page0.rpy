#storybook 1 page 0 slide 1

label stb1_page0:

scene bg_stb1_page1 with flash
pause 0.5
play music 'audio/storybook 1/Music _ Sounds/Sound FX/SB1 Ambience SFX (Loop).mp3' loop volume 0.75
pause 0.5
play sound 'audio/storybook 1/Music _ Sounds/Narrator Dialogues/Narrator-SB1_d1_v3.mp3'
n "As Deanna came to, she first sensed the rainforest’s song of chirping crickets and chattering cicadas."
window hide
pause 0.5
stop sound
#there is a missing image, the pan down from the forest top to the forest bottom
scene bg_stb1_page2 with easeinbottom
pause 1.0

call stb1_page1 from _call_stb1_page1
