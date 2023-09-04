#Deanna looks through the foliage
#page 1 of storybook 2

label stb2_page1:

$ renpy.movie_cutscene("images/sample_movie_pp.webm")
scene bg stb2_page 1 with fade
pause 1
window show dissolve
n "Deanna peeked through the foliage"
pause 1
window hide dissolve

call stb2_page2

