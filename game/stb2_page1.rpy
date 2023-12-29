#Deanna looks through the foliage
#page 1 of storybook 2

label stb2_page1:

#$ renpy.movie_cutscene("images/sample_movie_pp.webm")
scene bg_stb2_page1 with fade
pause 1
window show dissolve
play sound 'audio/storybook 2/Sounds + Music/Narrator Dialogues/Narrator-SB2_d1_v3.mp3'
n "Deanna peeked through the foliage"
pause 0.5
stop sound
pause 0.5
window hide dissolve

call stb2_page2 from _call_stb2_page2

